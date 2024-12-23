import streamlit as st
from functions.header import print_header
st.set_page_config(layout='wide')


st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}

    /* This code gets the first element on the sidebar,
    and overrides its default styling */
    section[data-testid="stSidebar"] div:first-child {
        top: 0;
        height: 0vh;
    }
</style>
""",unsafe_allow_html=True)

print_header()
