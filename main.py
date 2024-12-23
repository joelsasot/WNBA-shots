import streamlit as st
from functions.header import print_header
st.set_page_config(layout='wide')
st.write('''
         <style>
         div.block-container{padding-top:0.8rem;} 
         header {visibility: hidden;}
         </style>''', unsafe_allow_html=True   )

print_header()
