"""
Project 3: Induō - AI Outfit Generator (iOS)
"""

import streamlit as st
import config
from utils.helpers import get_image_base64

def project3_details():
    """
    Render the detailed content for Project 3.
    """
    # Get images as base64
    induo_img = get_image_base64(config.INDUO_IMAGE_PATH)
    induo_gif = get_image_base64(config.INDUO_GIF_PATH)

    # Custom styling
    st.markdown("""
        <style>
            .tech-stack {
                color: #4a5568;
                font-size: 1.2rem;
                margin-bottom: 1rem;
            }
            .highlight-box {
                background-color: #f7fafc;
                border-left: 4px solid #4299e1;
                padding: 1rem;
                margin: 1rem 0;
            }
            .section-title {
                color: #2d3748;
                margin-top: 2rem;
                margin-bottom: 1rem;
            }
            .content-text {
                line-height: 1.6;
                color: #4a5568;
            }
        </style>
    """, unsafe_allow_html=True)

    # Project Title and Tech Stack
    st.markdown("""
        <h2 class="individual-project-title">Induō - AI Outfit Generator</h2>
        <p class="tech-stack">Swift • Firebase • AI/ML • iOS Development</p>
        <hr class="divider">
    """, unsafe_allow_html=True)


    # Project Overview
    st.markdown("""
        <div class="highlight-box">
            <em><strong>Senior Project presented to LMU Faculty</strong></em><br>
            Led the development of an LLM-powered iOS application that revolutionizes wardrobe management through AI-driven outfit recommendations and virtual try-on capabilities.
        </div>
    """, unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns(2)

    # Key Features in first column
    with col1:
        st.markdown("""
            <h3 class="section-title">Key Features</h3>
            <div class="content-text">
                • Personalized wardrobe management system<br>
                • Virtually displays outfit selections on a photo of you<br>
                • AI-driven outfit recommendations tailored to your style<br>
                • Swipe left or right to like or dislike outfit suggestions<br>
                • Save outfits and let the AI learn from your preferences
            </div>
        """, unsafe_allow_html=True)

    # Technical Implementation in second column
    with col2:
        st.markdown("""
            <h3 class="section-title">Technical Details</h3>
            <div class="content-text">
                • Built with Swift and Firebase for robust backend support<br>
                • Implemented advanced AI integration using CatVTON<br>
                • Designed secure data transmission via HTTPS<br>
                • Created comprehensive software documentation including SRS, SDP, and DB design<br>
                • Developed custom scripts for optimizing AI model performance
            </div>
        """, unsafe_allow_html=True)

    # Project Demo Images
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%;">
                <img src="{induo_gif}" alt="Induō App Demo" style="width: 50%; height: 50%;">
                <p style="text-align: center; font-style: italic;">Induō App Demo - AI-Powered Outfit Generation</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <h3 class="section-title">Project Goals & Impact</h3>
            <div class="content-text">
                <div class="highlight-box">
                    • Streamlined daily outfit decision-making process<br>
                    • Advanced fashion technology through virtual try-on capabilities<br>
                    • Promoted sustainable fashion by maximizing existing wardrobes<br>
                    • Demonstrated strong product development skills
                </div>
            </div>
        """, unsafe_allow_html=True)

    


# For standalone testing
if __name__ == "__main__":
    st.title("Induō - AI Outfit Generator")
    project3_details()
