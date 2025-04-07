"""
Helper functions for the portfolio website.
"""

import streamlit as st
from base64 import b64encode
import config

def load_css():
    """
    Load and combine all CSS files defined in the config.
    """
    combined_css = ''
    for css_file in config.CSS_FILES:
        try:
            with open(css_file) as f:
                combined_css += f.read() + '\n'
        except FileNotFoundError:
            st.error(f"Could not find CSS file: {css_file}")
            
    st.markdown(f'<style>{combined_css}</style>', unsafe_allow_html=True)

def get_image_base64(image_path):
    """
    Convert an image file to base64 encoding.
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        str: Base64 encoded image data
    """
    try:
        with open(image_path, "rb") as img_file:
            return "data:image/jpeg;base64," + b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Could not find image file: {image_path}")
        return ""

def get_pdf_base64(pdf_path):
    """
    Convert a PDF file to base64 encoding.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        str: Base64 encoded PDF data
    """
    try:
        with open(pdf_path, "rb") as pdf_file:
            return b64encode(pdf_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Could not find PDF file: {pdf_path}")
        return ""
