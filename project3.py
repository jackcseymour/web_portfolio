import streamlit as st

def project3():
    st.title("Phoneme Classification for ASR")
    st.write("""
        Built validation from scratch by implementing k-fold cross-validation without external libraries, ensuring robust model evaluation for phoneme classification in Automatic Speech Recognition (ASR).
        Developed and compared Perceptron and Logistic Regression classifiers to distinguish vowel phonemes using TIMIT corpus audio data, processing 61-dimensional feature vectors.
        Applied data preprocessing techniques, including feature standardization, to enhance classifier performance and analyzed model accuracy across 10 trials of 10-fold cross-validation.
        Engineered a custom cross-validation pipeline, optimizing regularization techniques (L2) and hyperparameters to improve predictive accuracy and generalization.
    """)

if __name__ == "__main__":
    project3()