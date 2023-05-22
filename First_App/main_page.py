import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np

from helpers import flatten_json,load_lottiefile,load_lottieurl

def main_page():
    st.sidebar.markdown("# Main page 🎈")
    st.title("First Streamlit App")

    st.markdown('''
                Hi :wave ,\n
                My name is Nicholas McFadden, welcome to my first Streamlit app! 
    
                ''')


if __name__ == '__main__':
    main_page()