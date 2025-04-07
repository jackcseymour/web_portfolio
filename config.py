"""
Configuration settings for the portfolio website.
"""

# Page settings
PAGE_TITLE = "Jack Seymour's Portfolio"
PAGE_ICON = "book"  # Using text instead of emoji
PAGE_LAYOUT = "wide"

# File paths
PROFILE_IMAGE_PATH = "assets/images/dp.jpg"
RESUME_PATH = "assets/documents/Profile.pdf"
OFFICE_ICON_PATH = "assets/images/office.png"
INDUO_IMAGE_PATH = "assets/images/induo1.png"
INDUO_GIF_PATH = "assets/images/induo.gif"
FRAUD_VIZ_PATH = "assets/images/proj2visualization.png"
FRAUD_PRESENTATION_PATH = "assets/documents/fraud_detection_presentation.pdf"
SENTIMENT_VIZ_PATH = "assets/images/sentiment_visualization.png"

# Contact information
EMAIL = "jack.seymour@comcast.net"
LINKEDIN_URL = "https://www.linkedin.com/in/jackcseymour/"

# Personal information
FULL_NAME = "Jack Seymour"
UNIVERSITY = "Loyola Marymount University"
MAJOR = "Computer Science"
MINOR = "Business Administration"
GRADUATION_DATE = "May 2025"
LOCATION = "Los Angeles"

# CSS file paths
CSS_FILES = [
    'static/styles/main.css',
    'static/styles/header.css',
    'static/styles/about.css',
    'static/styles/projects.css',
    'static/styles/skills.css',
    'static/styles/responsive.css',
    'static/styles/utilities.css'
]

# Skills data
SKILLS = [
    {"name": "Python", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"},
    {"name": "SQL", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png"},
    {"name": "R", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg"},
    {"name": "React.js", "icon_url": "https://upload.wikimedia.org/commons/a/a7/React-icon.svg"},
    {"name": "Scikit-learn", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg"},
    {"name": "PyTorch", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/9/96/Pytorch_logo.png"},
    {"name": "Google Cloud Platform", "icon_url": "https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg"},
    {"name": "Microsoft Office", "icon_path": OFFICE_ICON_PATH},
]

ADDITIONAL_SKILLS = ["Data Analysis", "Databases", "Public Speaking", "Effective Presentation"]

# Projects summary data
PROJECTS = [
    {
        "id": "sentiment-analysis-with-svm",
        "title": "Sentiment Analysis with SVM",
        "summary": "Analyzed movie reviews using Support Vector Machines with hyperparameter tuning."
    },
    {
        "id": "fraud-detection",
        "title": "Fraud Detection with Gaussian Processes",
        "summary": "Achieved 97% recall on credit card fraud detection using Gaussian Processes."
    },
    {
        "id": "induo-ai",
        "title": "Induō - AI Outfit Generator",
        "summary": "Led development of an LLM-powered iOS app for AI-driven outfit recommendations and virtual try-on."
    }
]
