# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 12:09:00 2022

@author: Arjun Sharma
🇿
Project: Hypothesis Testing on Streamlit
"""

# Importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy import stats

st.set_page_config(
    page_title="Z-test", page_icon="📊", initial_sidebar_state="expanded"
)


def main():
    
    # Introductory text and design
    
    st.title("📊 Hypothesis Testing Webapp")
    st.subheader("By Arjun Sharma")
    html_temp = '''
    <div style = 'background-color: tomato; padding: 50px>
    <h3 style = 'color: white; text-align: center;'></h3>
    <h2 style = 'color: white; text-align: center;'>Validate your hypothesis using this app!</h2>
    <h3 style = 'color: white; text-align: left; padding-left: 15px'>  You can perform hypothesis testing using these tests:</h3>
    <h4 style = 'color: white; text-align: left; padding-left: 30px'>1. Z-test</h4>
    <h4 style = 'color: white; text-align: left; padding-left: 30px'>2. t-test</h4>
    <h4 style = 'color: white; text-align: left; padding-left: 30px'>3. Chi-square test</h4>
    
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # Getting uploaded file from user
    st.header("")
    uploaded_file = st.file_uploader("Upload your dataset (only CSV files)")
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        


if __name__ == '__main__':
    main()
    st.write(f"You can find me on [LinkedIn](https://www.linkedin.com/in/as3152k)")
    st.write(f"Here is my [Personal Website](https://arjun-sc31.github.io)")
