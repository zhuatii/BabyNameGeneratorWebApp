# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:47:36 2024

@author: Swati
"""

import streamlit as st
import NameGeneratorLLM

st.title('Baby Name Generator')

gender = st.sidebar.selectbox("Choose a gender", ('Girl', 'Boy'))

nationality = st.sidebar.selectbox("Choose a nationality", 
                                   ('American', 'Indian', 'Chinese',
                                    'Korean', 'French', 'German'))

if gender and nationality:
    response = NameGeneratorLLM.GenerateBabyNames(gender, nationality)
    baby_names = response['baby_names'].strip().split(",")
    st.write("** Top 5 Baby Names **")
    
    for name in baby_names:
        st.write("--", name)