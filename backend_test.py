#!/usr/bin/env python3
"""
Backend API Testing Suite for Portfolio Application
Tests all backend endpoints with comprehensive validation
"""

import requests
import json
import sys
from datetime import datetime
import io

# Backend URL from frontend environment
BACKEND_URL = "https://bi-analyst-port.preview.emergentagent.com/api"

class PortfolioAPITester:
    def __init__(self):
        self.results = []
        self.session = requests.Session()
        
    def log_result(self, test_name, success, message, details=None):
        """Log test result"""
        result = {
            'test': test_name,
            'success': success,
            'message': message,
            'timestamp': datetime.now().isoformat(),
            'details': details or {}
        }
        self.results.append(result)
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} {test_name}: {message}")
        if details and not success:
            print(f"   Details: {details}")
    
    def test_contact_form_valid_data(self):
        """Test POST /api/contact with valid data"""
        test_name = "Contact Form - Valid Data"
        
        try:
            payload = {
                "name": "Ali Mansouri",
                "email": "ali.mansouri@example.com", 
                "subject": "Portfolio Inquiry",
                "message": "Hello, I am interested in your portfolio and would like to discuss potential collaboration opportunities."
            }
            
            response = self.session.post(f"{BACKEND_URL}/contact", json=payload)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success') and data.get('id'):
                    self.log_result(test_name, True, "Contact form submission successful", {
                        'response_data': data,
                        'status_code': response.status_code
                    })
                    return data.get('id')  # Return message ID for later verification
                else:
                    self.log_result(test_name, False, "Response missing success flag or ID", {
                        'response_data': data,
                        'status_code': response.status_code
                    })
            else:
                self.log_result(test_name, False, f"HTTP {response.status_code}", {
                    'response_text': response.text,
                    'status_code': response.status_code
                })
                
        except Exception as e:
            self.log_result(test_name, False, f"Request failed: {str(e)}")
        
        return None
    
    def test_contact_form_invalid_email(self):
        """Test POST /api/contact with invalid email format"""
        test_name = "Contact Form - Invalid Email"
        
        try:
            payload = {
                "name": "Test User",
                "email": "invalid-email-format",
                "subject": "Test Subject", 
                "message": "This is a test message with invalid email format."
            }
            
            response = self.session.post(f"{BACKEND_URL}/contact", json=payload)
            
            # Should return 422 for validation error
            if response.status_code == 422:
                self.log_result(test_name, True, "Correctly rejected invalid email format", {
                    'status_code': response.status_code,
                    'response_data': response.json()
                })
            else:
                self.log_result(test_name, False, f"Expected 422, got {response.status_code}", {
                    'response_text': response.text,
                    'status_code': response.status_code
                })
                
        except Exception as e:
            self.log_result(test_name, False, f"Request failed: {str(e)}")
    
    def test_contact_form_missing_fields(self):
        """Test POST /api/contact with missing required fields"""
        test_name = "Contact Form - Missing Fields"
        
        try:
            payload = {
                "name": "Test User",
                "email": "test@example.com"
                # Missing subject and message
            }
            
            response = self.session.post(f"{BACKEND_URL}/contact", json=payload)
            
            # Should return 422 for validation error
            if response.status_code == 422:
                self.log_result(test_name, True, "Correctly rejected missing required fields", {
                    'status_code': response.status_code,
                    'response_data': response.json()
                })
            else:
                self.log_result(test_name, False, f"Expected 422, got {response.status_code}", {
                    'response_text': response.text,
                    'status_code': response.status_code
                })
                
        except Exception as e:
            self.log_result(test_name, False, f"Request failed: {str(e)}")
    
    def test_cv_download(self):
        """Test GET /api/download-cv endpoint"""
        test_name = "CV Download"
        
        try:
            response = self.session.get(f"{BACKEND_URL}/download-cv")
            
            if response.status_code == 200:
                # Check Content-Type
                content_type = response.headers.get('Content-Type', '')
                content_disposition = response.headers.get('Content-Disposition', '')
                
                if content_type == 'application/pdf':
                    if 'filename=' in content_disposition:
                        # Check if response contains PDF data
                        if len(response.content) > 0 and response.content[:4] == b'%PDF':
                            self.log_result(test_name, True, "CV PDF download successful", {
                                'content_type': content_type,
                                'content_disposition': content_disposition,
                                'content_size': len(response.content),
                                'status_code': response.status_code
                            })
                        else:
                            self.log_result(test_name, False, "Response is not a valid PDF", {
                                'content_type': content_type,
                                'content_size': len(response.content),
                                'first_bytes': response.content[:20].hex() if response.content else 'empty'
                            })
                    else:
                        self.log_result(test_name, False, "Missing filename in Content-Disposition header", {
                            'content_disposition': content_disposition
                        })
                else:
                    self.log_result(test_name, False, f"Wrong Content-Type: {content_type}", {
                        'expected': 'application/pdf',
                        'actual': content_type
                    })
            else:
                self.log_result(test_name, False, f"HTTP {response.status_code}", {
                    'response_text': response.text,
                    'status_code': response.status_code
                })
                
        except Exception as e:
            self.log_result(test_name, False, f"Request failed: {str(e)}")
    
    def test_get_contact_messages(self):
        """Test GET /api/contact-messages endpoint"""
        test_name = "Get Contact Messages"
        
        try:
            response = self.session.get(f"{BACKEND_URL}/contact-messages")
            
            if response.status_code == 200:
                data = response.json()
                
                if isinstance(data, list):
                    # Check if messages have required fields
                    required_fields = ['name', 'email', 'subject', 'message', 'created_at']
                    
                    if len(data) > 0:
                        sample_message = data[0]
                        missing_fields = [field for field in required_fields if field not in sample_message]
                        
                        if not missing_fields:
                            self.log_result(test_name, True, f"Retrieved {len(data)} contact messages", {
                                'message_count': len(data),
                                'sample_fields': list(sample_message.keys()),
                                'status_code': response.status_code
                            })
                        else:
                            self.log_result(test_name, False, f"Messages missing required fields: {missing_fields}", {
                                'missing_fields': missing_fields,
                                'available_fields': list(sample_message.keys())
                            })
                    else:
                        self.log_result(test_name, True, "Retrieved empty message list (no messages yet)", {
                            'message_count': 0,
                            'status_code': response.status_code
                        })
                else:
                    self.log_result(test_name, False, "Response is not an array", {
                        'response_type': type(data).__name__,
                        'response_data': data
                    })
            else:
                self.log_result(test_name, False, f"HTTP {response.status_code}", {
                    'response_text': response.text,
                    'status_code': response.status_code
                })
                
        except Exception as e:
            self.log_result(test_name, False, f"Request failed: {str(e)}")
    
    def test_mongodb_storage_verification(self, message_id=None):
        """Verify MongoDB storage by checking if submitted message appears in list"""
        test_name = "MongoDB Storage Verification"
        
        if not message_id:
            self.log_result(test_name, False, "No message ID available for verification")
            return
        
        try:
            # Get all messages
            response = self.session.get(f"{BACKEND_URL}/contact-messages")
            
            if response.status_code == 200:
                messages = response.json()
                
                # Look for our test message
                found_message = None
                for msg in messages:
                    if msg.get('_id') == message_id or msg.get('id') == message_id:
                        found_message = msg
                        break
                
                if found_message:
                    # Verify timestamp is recent (within last 5 minutes)
                    created_at = found_message.get('created_at')
                    if created_at:
                        self.log_result(test_name, True, "Message successfully stored in MongoDB", {
                            'message_id': message_id,
                            'created_at': created_at,
                            'message_fields': list(found_message.keys())
                        })
                    else:
                        self.log_result(test_name, False, "Message found but missing timestamp", {
                            'message_id': message_id,
                            'message_data': found_message
                        })
                else:
                    self.log_result(test_name, False, f"Submitted message not found in database", {
                        'searched_id': message_id,
                        'total_messages': len(messages)
                    })
            else:
                self.log_result(test_name, False, f"Could not retrieve messages for verification: HTTP {response.status_code}")
                
        except Exception as e:
            self.log_result(test_name, False, f"Verification failed: {str(e)}")
    
    def run_all_tests(self):
        """Run all test cases"""
        print(f"🚀 Starting Portfolio Backend API Tests")
        print(f"📍 Backend URL: {BACKEND_URL}")
        print("=" * 60)
        
        # Test contact form with valid data first (to get message ID)
        message_id = self.test_contact_form_valid_data()
        
        # Test contact form validation
        self.test_contact_form_invalid_email()
        self.test_contact_form_missing_fields()
        
        # Test CV download
        self.test_cv_download()
        
        # Test getting contact messages
        self.test_get_contact_messages()
        
        # Verify MongoDB storage
        if message_id:
            self.test_mongodb_storage_verification(message_id)
        
        # Print summary
        self.print_summary()
    
    def print_summary(self):
        """Print test summary"""
        print("\n" + "=" * 60)
        print("📊 TEST SUMMARY")
        print("=" * 60)
        
        passed = sum(1 for r in self.results if r['success'])
        failed = len(self.results) - passed
        
        print(f"Total Tests: {len(self.results)}")
        print(f"✅ Passed: {passed}")
        print(f"❌ Failed: {failed}")
        print(f"Success Rate: {(passed/len(self.results)*100):.1f}%")
        
        if failed > 0:
            print("\n🔍 FAILED TESTS:")
            for result in self.results:
                if not result['success']:
                    print(f"  • {result['test']}: {result['message']}")
        
        print("\n" + "=" * 60)
        return failed == 0

if __name__ == "__main__":
    tester = PortfolioAPITester()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)