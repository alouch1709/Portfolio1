import React, { useEffect, useRef } from 'react';
import { Github, Linkedin, Mail, MapPin, Download } from 'lucide-react';
import { Button } from './ui/button';
import { portfolioData } from '../mockData';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;

const Hero = () => {
  const { personal } = portfolioData;
  const titleRef = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('animate-fade-in');
          }
        });
      },
      { threshold: 0.1 }
    );

    if (titleRef.current) {
      observer.observe(titleRef.current);
    }

    return () => observer.disconnect();
  }, []);

  const handleDownloadCV = () => {
    window.open(`${BACKEND_URL}/api/download-cv`, '_blank');
  };

  return (
    <section id="hero" className="min-h-screen flex items-center pt-16">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          {/* Left Content */}
          <div ref={titleRef} className="space-y-6 opacity-0" style={{ animationDelay: '0.2s' }}>
            <div className="inline-block">
              <span className="text-sm font-mono text-primary tracking-wider uppercase">
                Portfolio 2025
              </span>
            </div>
            
            <h1 className="text-5xl sm:text-6xl lg:text-7xl font-bold text-foreground leading-tight">
              {personal.fullName}
            </h1>
            
            <h2 className="text-2xl sm:text-3xl text-foreground/70 font-light">
              {personal.title}
            </h2>
            
            <p className="text-lg text-foreground/60 leading-relaxed max-w-xl">
              {personal.profile}
            </p>

            {/* Contact Info */}
            <div className="flex flex-wrap gap-4 text-sm text-foreground/60">
              <div className="flex items-center gap-2">
                <MapPin size={16} className="text-primary" />
                <span>{personal.location}</span>
              </div>
              <div className="flex items-center gap-2">
                <Mail size={16} className="text-primary" />
                <a href={`mailto:${personal.email}`} className="hover:text-primary transition-colors">
                  {personal.email}
                </a>
              </div>
            </div>

            {/* CTA Buttons */}
            <div className="flex flex-wrap gap-4 pt-4">
              <Button
                size="lg"
                className="bg-primary text-primary-foreground hover:bg-primary/90"
                onClick={() => document.getElementById('contact').scrollIntoView({ behavior: 'smooth' })}
              >
                Me contacter
              </Button>
              <Button
                size="lg"
                variant="outline"
                onClick={handleDownloadCV}
                className="gap-2"
              >
                <Download size={18} />
                Télécharger CV
              </Button>
            </div>

            {/* Social Links */}
            <div className="flex gap-4 pt-4">
              <a
                href={personal.linkedin}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded border border-border hover:border-primary hover:text-primary transition-all"
              >
                <Linkedin size={20} />
              </a>
              <a
                href={personal.github}
                target="_blank"
                rel="noopener noreferrer"
                className="p-2 rounded border border-border hover:border-primary hover:text-primary transition-all"
              >
                <Github size={20} />
              </a>
            </div>
          </div>

          {/* Right Image */}
          <div className="relative">
            <div className="relative w-full max-w-md mx-auto">
              <div className="absolute inset-0 bg-primary/20 blur-3xl rounded-full"></div>
              <img
                src={personal.photo}
                alt={personal.fullName}
                className="relative rounded-2xl w-full h-auto object-cover shadow-2xl"
              />
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;