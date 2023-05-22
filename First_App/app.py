import streamlit as st
import requests

import pandas as pd
import numpy as np

key = "6b49ba5510ccf54441a7af0498a76b563cc3a8d8"


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

            parameters = {"api_key": key, "format": "json",'from':'EUR','to':'GBP','amount':10}

            url = "https://api.getgeoapi.com/v2/currency/convert"

            response = requests.get(url, parameters)

            st.write(response.json())
            
            

            # GET: https://api.getgeoapi.com/v2/currency/convert
            # ?api_key=6b49ba5510ccf54441a7af0498a76b563cc3a8d8
            # &from=EUR
            # &to=GBP
            # &amount=10
           



    else:
        st.subheader("Home")

if __name__ == '__main__':
    main()