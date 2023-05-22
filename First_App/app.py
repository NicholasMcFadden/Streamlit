import streamlit as st
import requests

import pandas as pd
import numpy as np


def main():
    menu = ['Home',"About", "Tools"]
    Nav_Sel = st.sidebar.selectbox('Menu', menu)

    st.title("First Streamlit App")

    if Nav_Sel == "About":
        st.subheader('About')
   


    elif Nav_Sel == "Tools":
        st.subheader('Tools')

        col1,col2 = st.columns(1,3)

          
        with col1:
            st.subheader('Convert')
            st.title('Currency')
            st.selectbox('Pick ', ['', 'dogs'])








    else:
        st.subheader("Home")

if __name__ == '__main__':
    main()