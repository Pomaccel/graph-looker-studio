import streamlit as st

# Set page config to make it more mobile-friendly
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to reduce margins and make the app more responsive
st.markdown("""
    <style>
    .reportview-container .main .block-container {
        padding-top: 1rem;
        padding-right: 1rem;
        padding-left: 1rem;
        padding-bottom: 1rem;
    }
    iframe {
        width: 100%;
        height: 100vh;
        border: none;
    }
    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Embedded Looker Studio Dashboard")

# Embed the Looker Studio dashboard
dashboard_url = "https://lookerstudio.google.com/s/mzd1km1DtGU"
st.components.v1.iframe(dashboard_url, height=600, scrolling=True)

# Add some responsive design
st.markdown("""
    <script>
    function resizeIframe() {
        const iframe = document.querySelector('iframe');
        if (iframe) {
            iframe.style.height = window.innerHeight + 'px';
        }
    }
    window.addEventListener('load', resizeIframe);
    window.addEventListener('resize', resizeIframe);
    </script>
""", unsafe_allow_html=True)