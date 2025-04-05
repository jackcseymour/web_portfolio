import streamlit as st

def project1():
    st.title("Sentiment Analysis with SVM")
    st.write("""
        Gathered and preprocessed 330 movie review tweets to create a labeled dataset for training.
        Tested sentiment classification with 70 held-out tweets, analyzing accuracy and misclassifications.
        Applied Scikit-learn Support Vector Machine (SVM) with hyperparameter tuning to balance class distribution.
        Reported results, highlighting most frequently used words in positive vs. negative reviews for additional insights.
    """)

if __name__ == "__main__":
    project1()