import streamlit as st

def homepage_header():
    c_logo,c_title = st.columns([0.03,0.97])
    with c_logo:
        st.image('logo.png',use_container_width=True)
    with c_title:
        st.header("WNBA Shots")

def  homepage_body():
    c_text,c_image = st.columns([0.35,0.65])
    with c_text:
        st.write("In bibendum sagittis tortor, at scelerisque est facilisis at. Suspendisse massa nisl, consectetur eu mattis pellentesque, commodo in lacus. Sed vitae egestas nunc. Pellentesque convallis, lacus id venenatis laoreet, orci arcu pulvinar dolor, nec rhoncus ipsum ipsum at leo. Nam tincidunt ex eu ultricies pretium. Etiam vulputate maximus urna sed aliquet. Mauris efficitur tincidunt laoreet.")
        st.write("In bibendum sagittis tortor, at scelerisque est facilisis at. Suspendisse massa nisl, consectetur eu mattis pellentesque, commodo in lacus. Sed vitae egestas nunc. Pellentesque convallis, lacus id venenatis laoreet, orci arcu pulvinar dolor, nec rhoncus ipsum ipsum at leo. Nam tincidunt ex eu ultricies pretium. Etiam vulputate maximus urna sed aliquet. Mauris efficitur tincidunt laoreet.")
    with c_image:
        with st.container(border=True):
            st.write("Here goes an animated image displaying some chart")
    
    with st.container(border=False):
        c1,c2,c3 = st.columns([0.45,0.1,0.45])
        with c2:
            if st.button(label='Go to Dashboard',type="primary"):
                return True

def print_homepage():
    homepage_header()
    dashboard = homepage_body()
    return dashboard