import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np

from helpers import flatten_json,load_lottiefile

def main_page():
    st.markdown("# Main page 🎈")
    st.sidebar.markdown("# Main page 🎈")
    st.title("First Streamlit App")