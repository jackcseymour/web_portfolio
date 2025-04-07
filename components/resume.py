"""
Resume component for the portfolio website.
"""

import streamlit as st
from utils.helpers import get_pdf_base64
import config

def render_resume():
    """
    Render the resume section with download button.
    """
    # Get resume PDF as base64
    pdf_base64 = get_pdf_base64(config.RESUME_PATH)
    
    st.markdown("""
        <h2 id="resume" style="text-align: center; color: #1a202c; margin-top: 50px;">Resume</h2>
        <hr style="width: 50%; margin: auto; border: 1px solid #1a202c;">
                <div style="text-align: center; margin-top: 20px;">
            <a href="data:application/pdf;base64,{pdf_base64}" download="Jack_Seymour_Resume.pdf" style="font-size: 18px; font-weight: bold; text-decoration: none; color: white; background-color: #1a202c; padding: 10px 20px; border-radius: 5px; display: inline-block;">
                📄 Download my Resume
            </a>
        </div>
    """, unsafe_allow_html=True)