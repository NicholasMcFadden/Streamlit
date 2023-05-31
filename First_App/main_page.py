import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import base64
import time
import boto3
import os

import components.authenticate as authenticate
# import components.db_conn as db_conn
from helpers import flatten_json,load_lottiefile,load_lottieurl


from botocore.exceptions import ClientError


# # S3 credentials
# S3_KEY= os.environ.get("S3_KEY")
# S3_SECRET=os.environ.get("S3_SECRET")
# region_bucket=os.environ.get("REGION_BUCKET")

# s3_bucket = 'first-streamlit-db'


# def create_presigned_url(bucket_name, object_name, expiration=3600):
#     """Generate a presigned URL to share an S3 object
#     :param bucket_name: string
#     :param object_name: string
#     :param expiration: Time in seconds for the presigned URL to remain valid
#     :return: Presigned URL as string. If error, returns None.
#     """
#     # Generate a presigned URL for the S3 object
#     s3_client = boto3.client('s3',aws_access_key_id = S3_KEY, aws_secret_access_key = S3_SECRET,region_name = region_bucket)
#     try:
#         response = s3_client.generate_presigned_url('get_object',
#                                                     Params={'Bucket': bucket_name,
#                                                             'Key': object_name},
#                                                     ExpiresIn=expiration)
#     except ClientError as e:
#         logging.error(e)
#         return None
#     # The response contains the presigned URL
#     return response


# # Connect to S3 DB object and retrieve object
# url = create_presigned_url(s3_bucket, 'tweet_data.csv')

# if url is not None:
#     response = requests.get(url)


# # Read in object
# df=pd.read_csv(url)

# st.dataframe(df.head())

# # Upload wdiget (up to 200MB but can increase in config)
# uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
# for i,uploaded_file in enumerate(uploaded_files):
#         db_conn.upload_to_aws(uploaded_file.name,s3_bucket,uploaded_file.name)
#         print('File {}: {} Upload Successful'.format(i,uploaded_file))

    


# Check authentication when user lands on the page.
# authenticate.set_st_state_vars()


def main_page():

    

    st.sidebar.markdown("# Main 🛬")
    st.sidebar.title('')

    # # Add login/logout buttons
    # if st.session_state["authenticated"]:
    #     authenticate.button_logout()
    # else:
    #     authenticate.button_login()


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