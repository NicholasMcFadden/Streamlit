import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np

from helpers import flatten_json,load_lottiefile,load_lottieurl

def main_page():
    st.sidebar.markdown("# Main 🛬")
    st.title("First Streamlit App")

    st.markdown('''
                Hi 👋, \n''')

    st.markdown("My name is Nicholas McFadden \n")
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