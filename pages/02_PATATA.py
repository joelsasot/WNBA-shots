import streamlit as st
st.set_page_config(page_title="Plotting Demo", page_icon="📈")
c_logo,c_title = st.columns([0.03,0.97])
with c_logo:
    st.image('logo.png',use_container_width=True)
with c_title:
    st.header("WNBA Player Comparator")