import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import numpy as np
from helpers import flatten_json,load_lottiefile,load_lottieurl
import components.authenticate as authenticate

# Check authentication when user lands on the page.
authenticate.set_st_state_vars()

def contact_page():

    st.sidebar.markdown("# Contact Me 📞📇")
    
    # Add login/logout buttons
    if st.session_state["authenticated"]:
        authenticate.button_logout()
    else:
        authenticate.button_login()
        
    st.markdown("# Contact Me 📞📇")
    email = 'placeholder'
    cell_num = 'placeholder' 

    st.write("Email: ", email)
    st.write("Phone \#: ", cell_num)

if __name__=='__main__':
    contact_page()