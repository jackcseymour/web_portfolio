import streamlit as st
from base64 import b64encode

def web_portfolio():
    # Page configs
    st.set_page_config(page_title="Jack Seymour's Portfolio", page_icon="🎓", layout="wide")

    # Custom CSS for styling
    st.markdown("""
        <style>
        body {
            font-family: 'Arial', sans-serif;
        }
        .header {
            background-color: #1a202c;
            padding: 1rem;
            color: white;
            text-align: center;
        }
        .nav-links {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin-top: 0.5rem;
        }
        .nav-links a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        .nav-links a:hover {
            text-decoration: underline;
        }
        .projects-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 50px;
        }
        .project-card {
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
            transition: transform 0.2s ease;
        }
        .project-card:hover {
            transform: translateY(-5px);
        }
        .project-card a {
            text-decoration: none;
            color: #1a202c;
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

    # Updated Header Section
    st.markdown("""
        <div class="header">
            <h1>Jack Seymour's Portfolio</h1>
            <div class="nav-links">
                <a href="#about-me">About Me</a>
                <a href="#projects">Projects</a>
                <a href="#resume">Resume</a>
                <a href="#contact">Contact</a>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Get Profile Image
    with open("dp.jpg", "rb") as img_file:
        img = "data:image/jpeg;base64," + b64encode(img_file.read()).decode()

    # Reading Profile
    with open("Profile.pdf", "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Updated About Me Section
    st.markdown(f"""
        <style>
        .about-me-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 50px;
            margin-bottom: 50px;
            animation: fadeIn 1s ease-in-out;
        }}
        .about-me-image {{
            border-radius: 50%;
            width: 150px;
            height: 150px;
            margin-right: 20px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            object-fit: cover;
            object-position: center 30%;
        }}
        .about-me-text {{
            max-width: 600px;
            font-size: 16px;
            line-height: 1.6;
        }}
        .linkedin-icon {{
            margin-left: 10px;
            vertical-align: middle;
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; }}
            to {{ opacity: 1; }}
        }}
        </style>
        <div class="about-me-container">
            <img src="{img}" alt="Profile Picture" class="about-me-image">
            <div class="about-me-text">
                <h2>About Me
                    <a href="https://www.linkedin.com/in/jackcseymour/" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" alt="LinkedIn" class="linkedin-icon" style="width: 25px; height: 25px;">
                    </a>
                </h2>
                <p>
                    🎓 I am a <strong>Senior</strong> at <strong>Loyola Marymount University</strong>, studying <strong>Computer Science</strong> with a minor in <strong>Business Administration</strong>, graduating in <strong>May 2025</strong>.
                </p>
                <p>
                    ❤️ I am passionate about <em>Machine Learning/Deep Learning, Data Science, Artificial Intelligence, Data Analytics, Automation,</em> and more!
                </p>
                <p>
                    🌟 I am looking for roles that combine my <strong>technical knowledge</strong> with a <strong>creative industry</strong> to share stories with the world. I am especially interested in positions that leverage my passion for <strong><em>public speaking</em></strong> and <strong><em>presentation</em></strong>, skills I will continue to hone.
                </p>
                <p>
                    🪧 You can reach me at <a href="mailto:jack.seymour@comcast.net">jack.seymour@comcast.net</a>.
                </p>
                <p>
                    🏠 Based in Los Angeles but willing to relocate.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Updated Projects Section
    st.markdown("""
        <h2 id="projects" style="text-align: center; margin-top: 50px;">Projects</h2>
        <div class="projects-container">
            <div class="project-card">
                <a href="https://example.com/project1" target="_blank">Sentiment Analysis with SVM</a>
                <p>Analyzed movie reviews using Support Vector Machines with hyperparameter tuning.</p>
            </div>
            <div class="project-card">
                <a href="https://example.com/project2" target="_blank">Fraud Detection with Gaussian Processes</a>
                <p>Achieved 97% recall on credit card fraud detection using Gaussian Processes.</p>
            </div>
            <div class="project-card">
                <a href="https://example.com/project3" target="_blank">Phoneme Classification for ASR</a>
                <p>Developed classifiers for phoneme recognition using Perceptron and Logistic Regression.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Download CV button
    st.download_button(label="📄 Download my Resume", data=pdf_bytes, file_name="Jack_Seymour_Resume.pdf", mime="application/pdf",)
    st.write("##")
    st.write(f"""<div class="subtitle" style="text-align: center;">🌟 Have A Wonderful Day!!! 🌟</div>""", unsafe_allow_html=True)

if __name__ == "__main__":
    web_portfolio()

