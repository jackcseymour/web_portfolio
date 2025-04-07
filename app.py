"""
Main application file for Jack Seymour's Data Science Portfolio.

This file serves as the entry point for the Streamlit web application.
It imports and renders all the components of the portfolio website.
"""

import streamlit as st
import config
from utils.helpers import load_css
from components.header import render_header
from components.about import render_about
from components.projects import render_projects_summary, render_project_details
from components.skills import render_skills
from components.resume import render_resume

def web_portfolio():
    """
    Main function to render the complete portfolio website.
    """
    # Page configuration
    st.set_page_config(
        page_title=config.PAGE_TITLE,
        page_icon=config.PAGE_ICON,
        layout=config.PAGE_LAYOUT
    )

    # Add custom CSS for main container
    st.markdown("""
        <style>
            .css-1d391kg,
            .css-18e3th9,
            .css-1r6slb0,
            .block-container {
                padding-left: 25% !important;
                padding-right: 25% !important;
                max-width: 100% !important;
            }
            @media (max-width: 768px) {
                .css-1d391kg,
                .css-18e3th9,
                .css-1r6slb0,
                .block-container {
                    padding-left: 5% !important;
                    padding-right: 5% !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # Load CSS
    load_css()

    # Render components
    render_header()
    render_about()
    render_projects_summary()
    render_skills()
    render_resume()
    render_project_details()

if __name__ == "__main__":
    web_portfolio()

