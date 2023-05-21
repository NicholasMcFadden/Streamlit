import streamlit as st
import requests

def main():
    menu = ['Home',"About"]
    Nav_Sel = st.sidebar.selectbox('Menu', menu)

    st.title("AllJobs - Job Agreggator")

    if Nav_Sel == "Home":
        st.subheader('Home')

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()