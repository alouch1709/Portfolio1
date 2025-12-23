import React from 'react';
import { Github, Linkedin, Mail, Heart } from 'lucide-react';
import { portfolioData } from '../mockData';

const Footer = () => {
  const { personal } = portfolioData;
  const currentYear = new Date().getFullYear();

  return (
    <footer className="bg-background border-t border-border py-12">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Logo & Description */}
          <div className="space-y-4">
            <h3
              className="text-xl font-semibold text-foreground"
              style={{ fontFamily: 'monospace', letterSpacing: '0.05em' }}
            >
              ALI MANSOURI
            </h3>
            <p className="text-sm text-foreground/60">
              Data Analyst / BI Analyst passionné par la transformation de données en insights exploitables.
            </p>
          </div>

          {/* Quick Links */}
          <div className="space-y-4">
            <h4 className="text-sm font-semibold text-foreground uppercase tracking-wider">
              Navigation rapide
            </h4>
            <ul className="space-y-2 text-sm">
              {['about', 'experience', 'projects', 'skills', 'contact'].map((section) => (
                <li key={section}>
                  <button
                    onClick={() => document.getElementById(section)?.scrollIntoView({ behavior: 'smooth' })}
                    className="text-foreground/60 hover:text-primary transition-colors capitalize"
                  >
                    {section === 'about' ? 'À propos' :
                     section === 'experience' ? 'Expérience' :
                     section === 'skills' ? 'Compétences' : section}
                  </button>
                </li>
              ))}
            </ul>
          </div>

          {/* Contact & Social */}
          <div className="space-y-4">
            <h4 className="text-sm font-semibold text-foreground uppercase tracking-wider">
              Restons connectés
            </h4>
            <div className="space-y-2 text-sm">
              <a
                href={`mailto:${personal.email}`}
                className="flex items-center gap-2 text-foreground/60 hover:text-primary transition-colors"
              >
                <Mail size={16} />
                {personal.email}
              </a>
              <div className="flex gap-3 pt-2">
                <a
                  href={personal.linkedin}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-2 rounded border border-border hover:border-primary hover:text-primary transition-all"
                >
                  <Linkedin size={18} />
                </a>
                <a
                  href={personal.github}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="p-2 rounded border border-border hover:border-primary hover:text-primary transition-all"
                >
                  <Github size={18} />
                </a>
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="mt-12 pt-8 border-t border-border">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4 text-sm text-foreground/60">
            <p className="flex items-center gap-1">
              © {currentYear} Ali Mansouri. Conçu avec <Heart size={14} className="text-red-500" /> et React
            </p>
            <p>Tous droits réservés.</p>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;