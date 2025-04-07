"""
About Me component for the portfolio website.
"""

import streamlit as st
from utils.helpers import get_image_base64
import config

def render_about():
    """
    Render the About Me section with profile image and personal information.
    """
    # Get profile image as base64
    img = get_image_base64(config.PROFILE_IMAGE_PATH)
    
    st.markdown(f"""
        <div class="about-me-container">
            <img src="{img}" alt="Profile Picture" class="about-me-image">
            <div class="about-me-text">
                <h2 style="color: #1a202c;">About Me
                    <a href="{config.LINKEDIN_URL}" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" 
                             alt="LinkedIn" 
                             class="linkedin-icon" 
                             style="width: 25px; height: 25px;">
                    </a>
                </h2>
                <p>
                    🎓 I am a <strong>Senior</strong> at <strong>{config.UNIVERSITY}</strong>, studying <strong>{config.MAJOR}</strong> with a minor in <strong>{config.MINOR}</strong>, graduating in <strong>{config.GRADUATION_DATE}</strong>.
                </p>
                <p>
                    ❤️ I am passionate about <em>Machine Learning/Deep Learning, Data Science, Artificial Intelligence, Data Analytics, Automation,</em> and more!
                </p>
                <p>
                    🌟 I am looking for roles that combine my <strong>technical knowledge</strong> with a <strong>creative industry</strong> to share stories with the world.
                </p>
                <p>
                    🎵 I enjoy music, singing, dancing, yoga, and cooking.
                </p>
                <p>
                    🪧 You can reach me at <a href="mailto:{config.EMAIL}">{config.EMAIL}</a>.
                </p>
                <p>
                    🏠 Based in {config.LOCATION} but willing to relocate.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)
