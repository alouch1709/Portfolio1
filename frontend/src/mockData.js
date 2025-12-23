export const portfolioData = {
  personal: {
    fullName: "Ali Mansouri",
    title: "Data Analyst / BI Analyst",
    email: "pro.amansouri@gmail.com",
    phone: "+212689616357",
    linkedin: "https://www.linkedin.com/in/alouch-mansouri/",
    github: "https://github.com/MansouriAli-1",
    location: "Morocco",
    photo: "https://customer-assets.emergentagent.com/job_eb2d47e9-a0ee-497a-86e1-f55afe4473f2/artifacts/o21n7aka_Gemini_Generated_Image_fupz77fupz77fupz.png",
    profile: "Data Analyst / BI Analyst spécialisé dans l'analyse de données, le développement de dashboards Power BI et la modélisation de Data Warehouse. Solide maîtrise de SQL, DAX, Power Query et Python pour transformer la donnée brute en indicateurs de performance exploitables. Capable de comprendre les besoins business, automatiser les flux et fournir des analyses fiables pour soutenir la prise de décision."
  },
  
  experience: [
    {
      id: 1,
      role: "BI Developer (Stage)",
      company: "COPAG",
      location: "Taroudant, Maroc",
      startDate: "Mars 2025",
      endDate: "Septembre 2025",
      current: false,
      responsibilities: [
        "Participation à la mise en place d'une architecture BI complète",
        "Conception et modélisation de Data Warehouse",
        "Développement de processus ETL",
        "Utilisation de SQL Server, SSIS, SSAS et Power BI pour le reporting",
        "Automatisation des flux et optimisation des performances"
      ]
    },
    {
      id: 2,
      role: "Data Analyst (Stage)",
      company: "PORTNET",
      location: "Casablanca, Maroc",
      startDate: "Août 2024",
      endDate: "Février 2025",
      current: false,
      responsibilities: [
        "Collecte et analyse des données logistiques et commerciales",
        "Développement de modèles prédictifs en Machine Learning",
        "Création de tableaux de bord interactifs",
        "Proposition de solutions pour réduire les inefficacités"
      ]
    },
    {
      id: 3,
      role: "Stage de Recherche - PFE",
      company: "Faculté Polydisciplinaire",
      location: "Taroudant, Maroc",
      startDate: "Février 2024",
      endDate: "Juillet 2024",
      current: false,
      responsibilities: [
        "Analyse comparative de l'apprentissage fédéré IoT vs centralisé",
        "Conception de prototypes distribués (edge computing)",
        "Évaluation des performances : latence, précision, inference time",
        "Technologies : Flower, TensorFlow Federated, Python"
      ]
    }
  ],
  
  projects: [
    {
      id: 1,
      name: "Analyse des accidents de la route",
      description: "Tableau de bord interactif pour analyser les tendances par région, moment de la journée et type de véhicule",
      tools: ["Power BI", "Power Query", "DAX"],
      category: "Business Intelligence"
    },
    {
      id: 2,
      name: "Maintenance prédictive",
      description: "Anticipation des pannes d'équipements industriels à partir de données capteurs",
      tools: ["Python", "Pandas", "Scikit-learn", "Matplotlib", "Seaborn"],
      category: "Machine Learning"
    },
    {
      id: 3,
      name: "Analyse de sentiments – HESPRESS",
      description: "Architecture Big Data pour l'ingestion et l'analyse en temps réel des commentaires",
      tools: ["Kafka", "Spark", "Hadoop", "MongoDB"],
      category: "Big Data"
    }
  ],
  
  skills: {
    businessIntelligence: {
      title: "Business Intelligence",
      items: ["Power BI", "DAX", "Power Query", "SSIS", "SSAS", "SQL Server", "Pentaho"]
    },
    databases: {
      title: "Bases de données",
      items: ["SQL Server", "MongoDB"]
    },
    programmingLanguages: {
      title: "Langages de programmation",
      items: ["SQL", "Python", "R", "Java", "C"]
    },
    bigData: {
      title: "Big Data",
      items: ["Hadoop", "Spark", "Kafka", "Hive"]
    },
    softSkills: {
      title: "Compétences interpersonnelles",
      items: ["Leadership", "Curiosité", "Motivation", "Rigueur", "Autonomie", "Esprit critique"]
    }
  },
  
  education: [
    {
      id: 1,
      degree: "Formation MS Power BI",
      institution: "JobInTech - Inovadex Consulting",
      startDate: "Septembre 2025",
      endDate: "En cours",
      current: true
    },
    {
      id: 2,
      degree: "Master Big Data et Intelligence Artificielle",
      institution: "Faculté Polydisciplinaire, Taroudant",
      startDate: "Septembre 2022",
      endDate: "Juillet 2024",
      current: false
    },
    {
      id: 3,
      degree: "Licence Professionnelle - Systèmes Informatiques Embarqués",
      institution: "Faculté des Sciences Appliquées, Ait Melloul",
      startDate: "Septembre 2018",
      endDate: "Juillet 2022",
      current: false
    }
  ],
  
  certifications: [
    {
      id: 1,
      name: "Data Analyst",
      provider: "DataCamp",
      status: "En cours"
    },
    {
      id: 2,
      name: "Power BI",
      provider: "Microsoft",
      status: "En cours"
    }
  ],
  
  languages: [
    { language: "Arabe", level: "Maternelle" },
    { language: "Français", level: "Intermédiaire (TCF B2)" },
    { language: "Anglais", level: "Intermédiaire" }
  ],
  
  activities: [
    {
      id: 1,
      organization: "ENACTUS",
      period: "2019-2023",
      role: "Team Leader"
    },
    {
      id: 2,
      organization: "REEIAM",
      period: "2021-2022",
      role: "Vice-Président"
    },
    {
      id: 3,
      organization: "Hult Prize",
      period: "2022-2024",
      role: "Mentor"
    }
  ]
};