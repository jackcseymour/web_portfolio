"""
Project 2: Fraud Detection with Gaussian Processes
"""

import streamlit as st
import config
from utils.helpers import get_image_base64, get_pdf_base64

def project2_details():
    """
    Render the detailed content for Project 2.
    """
    # Get visualization image and presentation as base64
    fraud_viz = get_image_base64(config.FRAUD_VIZ_PATH)
    presentation_base64 = get_pdf_base64(config.FRAUD_PRESENTATION_PATH)

    # Custom CSS
    st.markdown("""
        <style>
            .project-title {
                text-align: center;
                color: #1a202c;
                font-size: 2.5rem;
                margin-bottom: 2rem;
                margin-top: 50px;
            }
            
            .section-title {
                color: #2d3748;
                font-size: 1.5rem;
                margin-top: 2rem;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid #e2e8f0;
            }
            
            .content-text {
                color: #4a5568;
                line-height: 1.6;
                margin-bottom: 1rem;
            }
            
            .highlight-box {
                background-color: #f7fafc;
                padding: 1rem;
                margin-bottom: 1rem;
                border-radius: 4px;
                border-left: 4px solid #2d3748;
            }

            .tech-stack {
                font-weight: bold;
                color: #2d3748;
                font-size: 1.2rem;
            }

            .divider {
                margin: 2rem 0;
                border-top: 2px solid #e2e8f0;
            }

            .button-container {
                display: flex;
                justify-content: flex-start;
                margin-bottom: 2rem;
            }

            .back-button:hover {
                background-color: #4a5568;
            }
        </style>
    """, unsafe_allow_html=True)


    # Project Title and Tech Stack
    st.markdown("""
        <h2 class="tech-stack">Gaussian Processes | Fraud Detection System</h2>
        <hr class="divider">
    """, unsafe_allow_html=True)


    # # Add embedded PDF viewer
    # st.markdown(f"""
    #     <div style="display: flex; justify-content: center; margin: 20px 0;">
    #         <iframe 
    #             src="data:application/pdf;base64,{presentation_base64}" 
    #             width="100%" 
    #             height="500px" 
    #             style="border: 1px solid #ccc; border-radius: 5px;">
    #         </iframe>
    #     </div>
    # """, unsafe_allow_html=True)

    st.markdown("""
        <div class="highlight-box">
            <em><strong>Teaching Project in Machine Learning</strong></em><br>
            Applied <strong>Gaussian Processes</strong> to a credit card fraud dataset, achieving 97% recall. Independently studied the topic and taught the concept to a Machine Learning class while modeling the uncertainty and each predicted class probability with <strong>visualization</strong>.
        </div>
    """, unsafe_allow_html=True)

    # Create two columns for research questions and implementation
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <h3 class="section-title">Key Research Questions</h3>
            <div class="content-text">
                1. How can <strong>Gaussian Processes</strong> be applied to fraud detection?<br>
                2. What advantages do <strong>uncertainty estimates</strong> provide in fraud detection?<br>
                3. How does the model perform compared to traditional <strong>classification methods</strong>?
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <h3 class="section-title">Implementation Approach</h3>
            <div class="content-text">
                <strong>Dataset Characteristics (Source: Kaggle)</strong>:
                <ul>
                    <li><strong>284,807 transactions</strong> (492 fraudulent)</li>
                    <li><strong>28 feature variables</strong> (anonymized transaction features)</li>
                    <li><strong>Data preprocessing</strong> and binary fraud labels</li>
                </ul>
                <strong>Challenges Addressed</strong>:
                <ul>
                    <li>Highly <strong>imbalanced dataset</strong> (0.17% fraud rate)</li>
                    <li><strong>Feature engineering</strong> to reduce false positives</li>
                    <li><strong>Model optimization</strong> to prevent financial losses</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    # Create two more columns for model architecture and results
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
            <h3 class="section-title">Model Architecture</h3>
            <div class="content-text">
                <ul>
                    <li><strong>RBF kernel</strong> for capturing non-linear patterns</li>
                    <li>Implemented custom <strong>likelihood function</strong></li>
                    <li><strong>Hyperparameter optimization</strong></li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <h3 class="section-title">Results & Impact</h3>
            <div class="content-text">
                <div class="highlight-box">
                    • <strong>97% Recall Rate</strong><br>
                    • <strong>95% Precision</strong><br>
                    • <strong>Statistical analysis</strong> of uncertainty estimates
                </div>
            </div>
        """, unsafe_allow_html=True)

    # Add visualization
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 2rem 0;">
            <img src="{fraud_viz}" alt="Fraud Detection Visualization" style="width: 50%; height: auto;">
            <p style="text-align: center; font-style: italic; margin-top: 1rem;">Gaussian Process Classification Results</p>
        </div>
    """, unsafe_allow_html=True)


# For standalone testing
if __name__ == "__main__":
    st.title("Project 2: Fraud Detection with Gaussian Processes")
    project2_details()
