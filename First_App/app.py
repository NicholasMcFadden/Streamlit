import streamlit as st
import requests

def main():
    menu = ['Home',"About"]
    choice = st.sidebar.selectbox('Menu', menu)

    st.title("AllJobs - Job Agreggator")

    if choice == "Home":
        st.subheader('Home')

    else:
        st.subheader("About")

if __name__ == '__main__':
    main()