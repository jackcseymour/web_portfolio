"""
Header component for the portfolio website.
"""

import streamlit as st
import config

def render_header():
    """
    Render the header section with navigation links.
    """
    st.markdown(f"""
        <div class="header" style="background-color: #ffffff;">
            <h1 style=>Jack Seymour's Portfolio</h1>
            <div class="nav-links">
                <a href="#about-me" style="color: black;">About Me</a>
                <a href="#projects" style="color: black;">Projects</a>
                <a href="#resume" style="color: black;">Resume</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
