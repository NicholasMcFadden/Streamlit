import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
import helpers


def about_page():

    st.sidebar.markdown("# About 🚀💻")
    st.markdown("# About 🚀💻")

    st.image('media\st_teresa_cafe.jpg',use_column_width=True)

    st.title('Seeking Data Science/Analtyics opportunities')
    st.markdown('''
                Data and analytics have always been a large part of my career. However, my time in corporate strategy/consulting has solidified that the requirements for long term growth 
                will be highly correlated with oneself's ability to adopted new technology. When I started out in finance, having advanced Microsoft Excel ability made you ahead of the rest, then it was knowing SQL. 
                I saw this digital skills inflation happening right before my eyes.  \n''')
                
    st.markdown('''\nI asked myself "How can I capitalize on combining my business/finance/strategy background with this realization?". \n ''')
    
    st.image('media\kelley-school-of-business.jpeg',use_column_width=True)
    
    st.markdown('''My conclusion was that my niche will be as the liason between the business and the technical side.  "Walking a mile in someone else's shoes" can give someone unparalled perspective.
                That is why as a Data Scientist I can improve my technical and analytical skills while being able to leverage my extensive previous work history to translate business needs into technical
                analysis/requirements more effectively. \nThis is where I believe my talents will be best suited, at the interesection of: relationship building, communication, project management, and technical skills.  I am a naturally very curious person and Data Science in particular is exciting because at
                 its core it's using advanced methods/mathematics/technology to improve our understanding of the world around us. \n ''')

    
    col1,col2 = st.columns([3,1])

    with col1:
        st.image('media\Syracuse-University-logo.png',use_column_width=True)

    with col2:
        st.image('media\syracuse_seal_color.jpg',use_column_width=True)



    st.markdown('''

                That is when I chose to go to Syracuse University for their Masters of Science in Business Analytics(MSBA). I decided to complete the MSBA rather than just the MS in Data Science because at the forefront I wanted
                to make sure the skills I was learning tied back to bringing value to the business. While in the program, I really began to love and see the importance of learning the more advanced technical aspects of Data Science. 
                Luckily, the MSBA was a larger degree to achieve than the MS in Data Science degree at Syracuse. Therefore, I was able to arange the classes I took to take all of the same classes from the MS in Data Science degree
                in addition to the extra MSBA specific classes.\n
                ''')

    st.markdown('''But go figure....\n''')
    
    st.image('media\pico_malwee.jpg',use_column_width=True)

    st.markdown('''
                They wouldn't let me double major without paying for two degrees soooo.....the Certificate of Advanced Study(CAS) in Data Science is a fair consolation 😂!

                The Syracuse program gave me a great foundation in the Data Science/Business Analytics and now I want to apply these additional skills.  \n
                I am currently looking for opportunites in Data Science/Data & Business Analytics fields, ideally with a machine learning/artificial intelligence focus. 
                If you or someone you know, are looking to hire for a position in this field and/or need someone with my skill set PLEASE reach out --here--!! \n

                Please take the time to review the projects in this Streamlit Portfolio App and you can find more project at my --Github--.

                ''')


            #   graduated from Syracuse University with a Masters of Science in Business Analytics(MSBA) and a Certificate of Advanced Study(CAS) in Data Science. \n
                # Luckily, the MSBA was a larger degree to achieve than the MS in Data Science degree at Syracuse. Therefore, I was able to arrange the classes I took to 
                # take all of the same classes from the MS in Data Science degree when I realized tha ti . \n

if __name__=='__main__':
    about_page()




