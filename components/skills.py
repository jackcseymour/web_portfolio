"""
Skills component for the portfolio website.
"""

import streamlit as st
from base64 import b64encode
from utils.helpers import get_image_base64
import config

img = get_image_base64(config.OFFICE_ICON_PATH)

def render_skills():
    st.markdown("""
        <style>
        body {
            font-family: 'DM Sans', sans-serif;
            background-color: #F2F2F2;
            margin: 0;
            padding: 0;
        }
        .header {
            background-color: #1a202c;
            padding: 1rem;
            color: white;
            text-align: center;
        }
        .skills-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
            margin-left: 25%;
            margin-right: 25%;
        }
        .additional-skills-container {
            text-align: center;
            margin-top: 40px;
            margin-bottom: 40px;
        }
        .additional-skills-grid {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }
        .additional-skill-item {
            background-color: #1a202c;
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 1.1em;
        }
        @media (max-width: 768px) {
            .skills-container {
                margin-left: 10%;
                margin-right: 10%;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # Main Skills Section
    st.markdown(f"""
        <h2 id="skills" style="text-align: center; margin-top: 50px;"><strong>Technical Skills</strong></h2>
        <hr style="width: 50%; margin: auto; border: 1px solid #1a202c;">
        <div class="skills-container">
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" alt="Python" style="width: 50px; height: 50px;">
                <p>Python</p>
            </div>
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png" alt="SQL" style="width: 75px; height: 40px; margin-top: 10px;">
                <p>SQL</p>
            </div>
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/R_logo.svg" alt="R" style="width: 50px; height: 50px;">
                <p>R</p>
            </div>
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" alt="React.js" style="width: 50px; height: 50px;">
                <p>React.js</p>
            </div>
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" alt="Scikit-learn" style="width: 75px; height: 50px;">
                <p>Scikit-learn</p>
            </div>
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/Pytorch_logo.png" alt="PyTorch" style="width: 100px; height: 30px; margin-top: 12px; margin-bottom: 8px;">
                <p>PyTorch</p>
            </div>
            <div style="text-align: center;">
                <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Google_Cloud_logo.svg" alt="Google Cloud Platform" style="width: 75px; height: 50px; transform: scale(1.75)">
                <p>Google Cloud Platform</p>
            </div>
            <div style="text-align: center;">
                <img src="{img}" alt="Microsoft Office" style="width: 50px; height: 50px;">
                <p>Microsoft Office</p>
            </div>
        </div>

        <!-- Additional Skills Section -->
        <div class="additional-skills-container">
            <h2 style="text-align: center; margin-top: 50px;"><strong>Additional Skills</strong></h2>
            <hr style="width: 50%; margin: auto; border: 1px solid #1a202c;">
            <div class="additional-skills-grid">
                <div class="additional-skill-item">Databases</div>
                <div class="additional-skill-item">Data Analysis</div>
                <div class="additional-skill-item">Effective Presentation</div>
                <div class="additional-skill-item">Public Speaking</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
