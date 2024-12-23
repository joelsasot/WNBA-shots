import streamlit as st
from functions.header import print_header
st.set_page_config(layout='wide')

st.markdown("""
<style>
    #MainMenu, header, footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)

print_header()
