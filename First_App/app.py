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

        col1,col2 = st.columns([1,3])

          
        with col1:
            st.subheader('Convert')
            st.title('Currency')
            st.selectbox('Pick ', ['AS', 'dogs'])

        with col2:
            st.subheader('Currency History')

         

            # st.dataframe()

            parameters = {"api_key":st.secrets["db_password"], "format": "json"}

            url = "https://api.getgeoapi.com/v2/currency/convert"

            response = requests.get(url, parameters)

            st.write(response.json())
            
            

  
           



    else:
        st.subheader("Home")

if __name__ == '__main__':
    main()