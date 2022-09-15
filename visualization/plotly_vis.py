import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px

data = pd.read_csv('tips.csv')

#1. draw histogram for total bill

#2.draw histogram for total bill and colr by sex.

#3. draw scatter plot bw total_bill and tips and color by ("sex",'day','smoker','time')

#4. sunburst chart on feature ('sex','day','smoker','time')


st.subheader('draw histogram for total bill')

fig = px.histogram(data_frame=data,x='total_bill')

st.plotly_chart(fig)


#2.

st.markdown('---')
st.subheader('draw histogram for total bill and color by sex')

fig = px.histogram(data_frame = data,x='total_bill',color='sex')

st.plotly_chart(fig)

#3.

st.markdown('---')

st.subheader(' draw scatter plot bw total_bill and tips and color by (sex,day,smoker,time)')

select = st.selectbox('Select the category to color',('sex','smoker','day','time'))

fig = px.histogram(data_frame = data,x='total_bill',color=select)

#4.


st.plotly_chart(fig)

st.markdown('---')

st.subheader('scatter chart on feature (sex,day,smoker,time)')

color_option = st.selectbox('Select the category to color' , ('sex','smoker','day','time'),key="sunburst")

a = px.scatter(data_frame = data , x = 'total_bill',y='tip',color= color_option)

st.plotly_chart(a)


#4.

st.markdown('---')

st.subheader('sunburst chart on feature (sex,day,smoker,time)')

path = st.multiselect('Select the categorical features path', ('sex','smoker','day','time'))

fig = px.sunburst(data_frame=data,path=path)

st.plotly_chart(fig)