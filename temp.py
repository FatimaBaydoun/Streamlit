# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
st.title("Interactive Visualization With Streamlit") 

import pandas as pd
import plotly.express as px  
df = pd.read_csv("/Users/mac/Desktop/StudentsPerformance.csv")

if st.checkbox('Show Students Perfomance Dataset'):
   st.subheader('Students Perfomance Dataset') 
   st.write(df)
   
st.header("Math Score By Gender")
fig= px.box(df, y="math_score", color="gender")
st.plotly_chart(fig)

st.header("Reading Score By Gender")
fig2= px.histogram(df, x="reading_score", color = "gender")
st.plotly_chart(fig2)

st.subheader("Gender")
z=["Male","Female"]
y=st.radio('Navigation',z)

st.subheader("What is your reading score?")
x=st.slider('A number between 0-100', min_value=(0), max_value=(100))
st.write('Grade:',x)

st.header("Reading and writting score By gender")
fig3= px.scatter(df, x="reading_score", y="writing_score", color="gender")
st.plotly_chart(fig3)

st.header("Writting Score By Race")
fig4= px.pie(df, values="writing_score", names="race")
st.plotly_chart(fig4)

st.header("Reading and writting score By gender and parental education")
fig5= px.scatter(df, x="reading_score", y="writing_score", color="gender", animation_frame="parental_education",range_x=[20,100], range_y=[20,100])
st.plotly_chart(fig5)

