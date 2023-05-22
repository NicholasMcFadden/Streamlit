import streamlit as st
import requests

import pandas as pd
import numpy as np

import helpers



def main():
    menu = ['Home',"About", "Tools"]
    Nav_Sel = st.sidebar.selectbox('Menu', menu)

    st.title("First Streamlit App")

    if Nav_Sel == "About":
        st.subheader('About')
   


    elif Nav_Sel == "Tools":

        tool_sel = st.selectbox('Select Tool:',['Currency Converter','Other'])

        if tool_sel == 'Currency Converter':
            
            st.title('Currency Converter')

            st.write('''Currency Conversion Rates from Currency API: 
                    https://currency.getgeoapi.com/''')
            
            col1,col2 = st.columns([1,3])

            with col1:

                st.subheader('Convert')

                cur_list = ['USD', 'EUR','GBP']

                parameters = {"api_key":st.secrets["db_password"], "format": "json"}

                url = "https://api.getgeoapi.com/v2/currency/list"

                response = requests.get(url, parameters)

                data_list = response.json()

                cur_list = data_list['currencies']

                start_cur = st.selectbox('From: ',cur_list.values())

                start_pos = [key for key, val in cur_list.items() if val == start_cur]
                
                if len(start_pos) > 0:
                    print("The key for the value", start_cur, "is", start_pos[0])
                else:
                    print("Value not found in dictionary")

                amount_base_cur = st.number_input('Amount: ',min_value=0)

                end_cur = st.selectbox('To: ', cur_list.values())

                end_pos = [key for key, val in cur_list.items() if val == end_cur]
                
                if len(end_pos) > 0:
                    print("The key for the value", end_cur, "is", end_pos[0])
                else:
                    print("Value not found in dictionary")

                              
    
            with col2:

                st.subheader('Currency Exchange Info')

                parameters = {"api_key":st.secrets["db_password"], "format": "json",
                            "from":start_pos[0],"to":end_pos[0],'amount':amount_base_cur}

                url = "https://api.getgeoapi.com/v2/currency/convert"

                response = requests.get(url, parameters)

                data_ext = response.json()

                # st.write(data_ext)

                flat_data = helpers.flatten_json(data_ext)

                conv_df = pd.DataFrame(flat_data,columns=flat_data.keys(),index=['API Response:'])

                conv_df_t = conv_df.transpose()

                st.write(conv_df_t)
                
                st.write('API JSON Response: ',data_ext)

                           
    else:
        st.subheader("Home")

if __name__ == '__main__':
    main()