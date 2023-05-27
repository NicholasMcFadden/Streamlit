import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import base64
import time
import boto3

import components.authenticate as authenticate
import components.db_conn as db_conn

from helpers import flatten_json,load_lottiefile,load_lottieurl


# S3 credentials
S3_KEY='----insert your access key here----'
S3_SECRET='----insert your secret key here----'
region_bucket='eu-central-1'



# Check authentication when user lands on the page.
authenticate.set_st_state_vars()

# Add login/logout buttons
if st.session_state["authenticated"]:
    authenticate.button_logout()
else:
    authenticate.button_login()



def main_page():
  

    st.sidebar.markdown("# Main 🛬")
    st.title("Hi 👋,")

    st.markdown('''### My name is **Nick**.\n
                ''')
    st.write("")
    st.markdown('''##### From the BIG GUY and I, WELCOME to my first Streamlit app!''')
    st.image('media\\rio_christ.jpg',use_column_width=True)

    st.markdown('''
                I created this Streamlit app to showcase some of my Data Science projects
                and ability deploy prototypes.\n

                Enjoy exploring the projects listed on this app and the Streamlit app itself.\n

                To find more information about me and other projects not showcased here; Take a look at these:\n
                
                LinkedIn:
                GitHub:
                                ''')
    
    st.markdown('''### Searching for Job Opportunites 🔎''')

    st.markdown('''Looking for opportunites in data and analytics.\n''')

   
if __name__ == '__main__':
    main_page()