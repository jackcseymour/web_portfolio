"""
Projects component for the portfolio website.
"""

import streamlit as st
import config
from projects.project1 import project1_details
from projects.project2 import project2_details
from projects.project3 import project3_details

# Centralized CSS for Projects
PROJECTS_CSS = """
<style>
/* General styling for the projects section */
.project-card {
    padding: 20px;
    text-align: center;
    transition: transform 0.2s ease;
    margin-bottom: 30px;
}

.project-card:nth-child(1) {
    background-color: #f8f9fa;
}

.project-card:nth-child(2) {
    background-color: #f1f3f5;
}

.project-card:nth-child(3) {
    background-color: #e9ecef;
}

.project-card:hover {
    transform: translateY(-5px);
}

.project-card a {
    text-decoration: none;
    color: #1a202c;
    font-weight: bold;
    font-size: 1.2em;
    display: block;
    margin-bottom: 10px;
}

.project-card a:hover {
    color: #FBD188;
}

.project-card p {
    color: #4a5568;
    line-height: 1.6;
}

/* Streamlit container overrides */
.stContainer {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 40px;  /* Increased from 20px */
    margin-top: 30px;
    margin-right: 25%;
    margin-left: 25%;
}

.individual-project-container {
    margin: 4rem auto;
    padding: 2rem;
}

</style>
"""

def render_projects_summary():
    """
    Render the projects summary section with links to individual projects.
    """
    # Inject CSS
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)

    # Create header
    st.markdown("""
        <h2 id="projects" style="text-align: center; margin-top: 50px; color: #1a202c; ">Projects</h2>
        <hr style="width: 50%; margin: auto; border: 1px solid #1a202c;">
    """, unsafe_allow_html=True)

    # Create main projects container
    projects_container = st.container()
    
    # Create columns for project cards
    num_projects = len(config.PROJECTS)
    cols = projects_container.columns(num_projects)

    # Create project cards dynamically from config
    for idx, (col, project) in enumerate(zip(cols, config.PROJECTS)):
        with col:
            project_card = st.container(border=False)
            with project_card:
                st.markdown(f"""
                    <div class="project-card">
                        <a href="#{project['id']}">{project['title']}</a>
                        <p>{project['summary']}</p>
                    </div>
                """, unsafe_allow_html=True)

def render_project_details():
    """
    Render the detailed project sections.
    """
    # Inject CSS
    st.markdown(PROJECTS_CSS, unsafe_allow_html=True)

    # Render individual project details
    projects = [
        {"id": "sentiment-analysis-with-svm", "details": project1_details},
        {"id": "fraud-detection", "details": project2_details},
        {"id": "induo-ai", "details": project3_details},
    ]

    for project in projects:
        st.markdown(f"""
            <div class="individual-project-container" id="{project['id']}">
        """, unsafe_allow_html=True)
        project["details"]()
        st.markdown("""
                <a href="#projects" class="back-to-top-link">
                    <span style="color: #ffffff; font-size: 24px;">↑</span>
                </a>
            </div>
        """, unsafe_allow_html=True)
