"""
Project 1: Sentiment Analysis with SVM
"""

import streamlit as st
import pandas as pd
import config
from utils.helpers import get_image_base64

def project1_details():
    """
    Render the detailed content for Project 1.
    """
    # Get visualization image as base64
    sentiment_viz = get_image_base64(config.SENTIMENT_VIZ_PATH)

    # Create metrics comparison table
    metrics_data = {
        'Metric': ['Accuracy', 'F1 Score', 'AUROC', 'Precision', 'Sensitivity', 'Specificity'],
        'Linear SVM': ['78.57%', '0.8454', '0.8184', '0.8913', '0.8039', '0.7368'],
        'RBF SVM': ['75.71%', '0.8283', '0.8204', '0.8542', '0.8039', '0.6316']
    }
    df = pd.DataFrame(metrics_data)
    metrics_table_html = df.style.set_properties(**{'text-align': 'center'}).to_html()

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
            
            .metrics-item {
                margin-bottom: 0.5rem;
                padding-left: 1rem;
            }
            
            .key-takeaway {
                background-color: #f7fafc;
                padding: 0.5rem 1rem;
                margin-bottom: 0.5rem;
                border-radius: 4px;
                border-left: 4px solid #2d3748;
            }

            .metrics-table {
                margin-top: 1rem;
                margin-bottom: 2rem;
            }
        </style>

        <h2 class="project-title">Movie Review Sentiment Analysis with SVM</h2>

    """, unsafe_allow_html=True)

    # Create two columns
    col1, col2 = st.columns(2)

    # Research Questions in first column
    with col1:
        st.markdown("""
            <h3 class="section-title">Research Questions</h3>
            <div class="content-text">
                • Can ML effectively perform <strong>sentiment analysis</strong> on movie reviews?<br>
                • How can model optimization maximize performance?<br>
                • What neutral words appear frequently in reviews that tilt to positive or negative?<br>
                • Which plot elements correlate with positive/negative sentiment?<br>
                • What additional <strong>business insights</strong> can be extracted?
            </div>
        """, unsafe_allow_html=True)

    # Analysis Methodology in second column
    with col2:
        st.markdown("""
            <h3 class="section-title">Analysis Methodology</h3>
            <div class="content-text">
                1. <strong>Preprocessed</strong> 330 movie review tweets for training<br>
                2. Implemented 70-tweet holdout validation set<br>
                3. Applied SVM with <strong>hyperparameter optimization</strong><br>
                4. Conducted word frequency analysis for sentiment correlation<br>
                5. Visualized word clouds to analyze positive and negative words based on frequency, providing insights into sentiment trends and business implications
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<h3 class='section-title'>Performance Metrics</h3>", unsafe_allow_html=True)
    # Display the metrics table
    st.table(df.style.set_properties(**{'text-align': 'center'}).hide(axis="index"))
    
    # Insert visualization here
    st.markdown(f"""
        <div style="display: flex; flex-direction: column; justify-content: center; align-items: center; margin: 2rem 0;">
            <img src="{sentiment_viz}" alt="Sentiment Analysis Visualization" style="width: 100%; height: auto;">
            <p style="text-align: center; font-style: italic; margin-top: 1rem;">Word Frequency Analysis in Positive & Negative Reviews</p>
        </div>
    """, unsafe_allow_html=True)

    # Create two more columns for takeaways and business insights
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
            <h3 class="section-title">Key Technical Takeaways</h3>
            <div class="content-text">
                <div class="key-takeaway">• Linear SVM outperformed RBF kernel, suggesting simpler model sufficiency</div>
                <div class="key-takeaway">• <strong>High precision</strong> indicates reliable negative review detection</div>
                <div class="key-takeaway">• Model demonstrates robust classification despite varied review language</div>
            </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
            <h3 class="section-title">Business Insights</h3>
            <div class="content-text">
                <div class="key-takeaway">• <strong>"Pirate"</strong> theme correlates with positive sentiment, suggesting audience interest</div>
                <div class="key-takeaway">• Temporal analysis reveals potential quality dip in <strong>2012</strong> releases</div>
                <div class="key-takeaway">• <strong>"Boring"</strong> frequently appears in negative reviews, indicating need for engaging content</div>
            </div>
        """, unsafe_allow_html=True)

# For standalone testing
if __name__ == "__main__":
    st.title("Project 1: Sentiment Analysis with SVM")
    project1_details()
