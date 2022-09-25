# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
st.title("Interactive Visualization With Streamlit") 

import pandas as pd
import plotly.express as px  
df = pd.read_csv("StudentsPerformance.csv")

if st.checkbox('Show Students Perfomance Dataset'):
   st.subheader('Students Perfomance Dataset') 
   st.write(df)
   
st.header("Math Score By Gender")
fig= px.box(df, y="math_score", color="gender")
st.plotly_chart(fig)

st.header("Reading Score By Gender")
option=st.selectbox("Gender",('All','Female','Male'))
if option=='All':
    fig8=px.histogram(df, x="reading_score", color = "gender")
    st.plotly_chart(fig8)
    
if option=='Female':
    Female=df[df["gender"]=='female']
    fig6=px.histogram(Female, x="reading_score", color_discrete_sequence=['blue'])
    st.plotly_chart(fig6)
    
if option=="Male":
    Male=df[df["gender"]=='male']
    fig7=px.histogram(Male, x="reading_score", color_discrete_sequence=['red'])
    st.plotly_chart(fig7)
      
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

