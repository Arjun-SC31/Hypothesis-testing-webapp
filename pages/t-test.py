# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 12:09:00 2022

@author: Arjun Sharma
🇹
Project: Hypothesis Testing on Streamlit
"""

# Importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy import stats

st.set_page_config(
    page_title="t-test", page_icon="📊", initial_sidebar_state="expanded"
)


def main():
    
    # Introductory text and design
    
    st.title("📊 Hypothesis testing: t-test")
    st.subheader("By Arjun Sharma")
    html_temp = '''
    <div style = 'background-color: tomato; padding: 50px>
    <h3 style = 'color: white; text-align: center;'></h3>
    <h2 style = 'color: white; text-align: center;'>Use the t-test to validate your hypothesis</h2>
    
    
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html = True)
    
    # Getting uploaded file from user
    st.header("")
    uploaded_file = st.file_uploader("Upload your dataset here (only CSV files)")
    if uploaded_file is not None:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)
        


if __name__ == '__main__':
    main()
    st.write(f"You can find me on [LinkedIn](https://www.linkedin.com/in/as3152k)")
    st.write(f"Here is my [Personal Website](https://arjun-sc31.github.io)")
