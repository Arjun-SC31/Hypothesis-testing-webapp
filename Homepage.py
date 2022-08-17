# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 12:09:00 2022

@author: Arjun Sharma

Project: Hypothesis Testing on Streamlit
"""

# Importing necessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from scipy import stats

st.set_page_config(
    page_title="Hypothesis Testing Webapp", page_icon="📊", initial_sidebar_state="expanded"
)

def main():
    
    # Introductory text and design
    
    st.title("📊 Hypothesis Testing Webapp")
    st.subheader("By Arjun Sharma")
    html_temp = '''
    <div style = 'background-color: tomato; padding: 50px>
    <h3 style = 'color: white; text-align: center;'></h3>
    <h2 style = 'color: white; text-align: center;'>Validate your hypothesis using this app!</h2>
    <h3 style = 'color: white; text-align: left; padding-left: 15px'>You can perform hypothesis testing using these tests:</h3>
    <h4 style = 'color: white; text-align: left; padding-left: 30px'>i. Z-test   - 🔗</h4>
    <h4 style = 'color: white; text-align: left; padding-left: 30px'>ii. t-test   - 🔗</h4>
    <h4 style = 'color: white; text-align: left; padding-left: 30px'>iii. Chi-Square test   - 🔗</h4>
    
    </div>
    '''
    st.markdown(html_temp, unsafe_allow_html = True)
    
   
        


if __name__ == '__main__':
    main()
    st.write(f"You can find me on [LinkedIn](https://www.linkedin.com/in/as3152k)")
    st.write(f"Here is my [Personal Website](https://arjun-sc31.github.io)")
