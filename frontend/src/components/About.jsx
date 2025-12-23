import React, { useEffect, useRef } from 'react';
import { GraduationCap, Award, Globe, Trophy } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Tabs, TabsContent, TabsList, TabsTrigger } from './ui/tabs';
import { portfolioData } from '../mockData';

const About = () => {
  const { education, certifications, languages, activities } = portfolioData;
  const sectionRef = useRef(null);

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

    if (sectionRef.current) {
      observer.observe(sectionRef.current);
    }

    return () => observer.disconnect();
  }, []);

  return (
    <section id="about" className="py-20" ref={sectionRef}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="text-center mb-16">
          <span className="text-sm font-mono text-primary tracking-wider uppercase">
            En savoir plus
          </span>
          <h2 className="text-4xl sm:text-5xl font-bold text-foreground mt-4">
            À propos
          </h2>
        </div>

        <Tabs defaultValue="education" className="w-full">
          <TabsList className="grid w-full grid-cols-2 lg:grid-cols-4 mb-8">
            <TabsTrigger value="education" className="gap-2">
              <GraduationCap size={16} />
              Formation
            </TabsTrigger>
            <TabsTrigger value="certifications" className="gap-2">
              <Award size={16} />
              Certifications
            </TabsTrigger>
            <TabsTrigger value="languages" className="gap-2">
              <Globe size={16} />
              Langues
            </TabsTrigger>
            <TabsTrigger value="activities" className="gap-2">
              <Trophy size={16} />
              Engagements
            </TabsTrigger>
          </TabsList>

          <TabsContent value="education" className="space-y-4">
            {education.map((edu) => (
              <Card key={edu.id} className="hover:shadow-lg transition-shadow">
                <CardHeader>
                  <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2">
                    <CardTitle className="text-xl">{edu.degree}</CardTitle>
                    {edu.current && (
                      <Badge className="w-fit">En cours</Badge>
                    )}
                  </div>
                  <p className="text-primary font-semibold">{edu.institution}</p>
                </CardHeader>
                <CardContent>
                  <p className="text-sm text-foreground/60">
                    {edu.startDate} - {edu.endDate}
                  </p>
                </CardContent>
              </Card>
            ))}
          </TabsContent>

          <TabsContent value="certifications" className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {certifications.map((cert) => (
                <Card key={cert.id} className="hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <CardTitle className="text-lg">{cert.name}</CardTitle>
                    <p className="text-primary font-semibold">{cert.provider}</p>
                  </CardHeader>
                  <CardContent>
                    <Badge variant="secondary">{cert.status}</Badge>
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="languages" className="space-y-4">
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              {languages.map((lang, index) => (
                <Card key={index} className="hover:shadow-lg transition-shadow">
                  <CardHeader>
                    <CardTitle className="text-lg">{lang.language}</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <p className="text-foreground/70">{lang.level}</p>
                  </CardContent>
                </Card>
              ))}
            </div>
          </TabsContent>

          <TabsContent value="activities" className="space-y-4">
            {activities.map((activity) => (
              <Card key={activity.id} className="hover:shadow-lg transition-shadow">
                <CardHeader>
                  <div className="flex flex-col sm:flex-row sm:items-start sm:justify-between gap-2">
                    <CardTitle className="text-xl">{activity.organization}</CardTitle>
                    <span className="text-sm text-foreground/60">{activity.period}</span>
                  </div>
                  <p className="text-primary font-semibold">{activity.role}</p>
                </CardHeader>
              </Card>
            ))}
          </TabsContent>
        </Tabs>
      </div>
    </section>
  );
};

export default About;