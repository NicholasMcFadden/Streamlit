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
            start_cur = st.selectbox('From: ', ['USD', 'EUR','GBP'])

            amount_base_cur = st.number_input('Amount: ',min_value=0)

            end_cur = st.selectbox('To: ',['USD', 'EUR','GBP'])
        with col2:
            st.subheader('Currency Exchange Info')

 

            parameters = {"api_key":st.secrets["db_password"], "format": "json",
                          "from":start_cur,"to":end_cur,'amount':amount_base_cur}

            url = "https://api.getgeoapi.com/v2/currency/convert"

            response = requests.get(url, parameters)

            st.write(response.json())

        

  
           
    else:
        st.subheader("Home")

if __name__ == '__main__':
    main()