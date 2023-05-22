import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import numpy as np
from helpers import flatten_json,load_lottiefile,load_lottieurl

def currency_converter_app():

    st.sidebar.markdown("# Currency 💱")

    lottie_file = load_lottiefile('media\cur_exchange_lottie.json')

    st_lottie(lottie_file,
            speed=.95,
            reverse=False,
            loop=True,
            quality="low",
            height=225,
            width=None,
            key=None,
            )                            


    # lottie_url = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_ikaawl5v.json')

    # st_lottie(lottie_url,
    #           speed=.95,
    #           reverse=False,
    #           loop=True,
    #           quality="low",
    #           height=225,
    #           width=None,
    #           key=None,
    #           )

    st.title('Currency Converter')

    st.write('''Currency Conversion Rates from Currency API: 
            https://currency.getgeoapi.com/''')



    col1,col2,col3 = st.columns([3,1,6])
    with col1:

        st.subheader('Convert')

        parameters = {"api_key":st.secrets["db_password"], "format": "json"}

        url = "https://api.getgeoapi.com/v2/currency/list"

        response = requests.get(url, parameters)

        data_list = response.json()

        cur_list = data_list['currencies']

        start_cur = st.selectbox('From (Type to Search): ',cur_list.values())

        start_pos = [key for key, val in cur_list.items() if val == start_cur]
        
        if len(start_pos) > 0:
            print("The key for the value", start_cur, "is", start_pos[0])
        else:
            print("Value not found in dictionary")

        amount_base_cur = st.number_input('Amount: ',min_value=0)

        end_cur = st.selectbox('To: (Type to Search)', cur_list.values())

        end_pos = [key for key, val in cur_list.items() if val == end_cur]
        
        st.markdown('##\n##')

        # lottie_file = load_lottiefile('media\cur_exchange_lottie.json')

        # st_lottie(lottie_file,
        #       speed=.95,
        #       reverse=False,
        #       loop=True,
        #       quality="low",
        #       height=225,
        #       width=None,
        #       key=None,
        #       ) 
        lottie_url = load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_ikaawl5v.json')

    

        st_lottie(lottie_url,
            speed=.95,
            reverse=False,
            loop=True,
            quality="low",
            height=225,
            width=None,
            key=None,
            )                           

    with col3:

        st.subheader('Currency Exchange Info')

        parameters = {"api_key":st.secrets["db_password"], "format": "json",
                    "from":start_pos[0],"to":end_pos[0],'amount':amount_base_cur}

        url = "https://api.getgeoapi.com/v2/currency/convert"

        response = requests.get(url, parameters)

        data_ext = response.json()

        # st.write(data_ext)

        flat_data = flatten_json(data_ext)

        conv_df = pd.DataFrame(flat_data,columns=flat_data.keys(),index=['API Response:'])

        conv_df_t = conv_df.transpose()

        st.table(conv_df_t)
        
        st.write('API JSON Response: ',data_ext)

    with col2:
        st.markdown('')

if __name__=='__main__':
    currency_converter_app()





