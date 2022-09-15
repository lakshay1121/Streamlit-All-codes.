import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

x = [1,2,3,4,5]
y = [6,7,2,4,5]

p = figure(title='Simple Line Chart',
            x_axis_label='x',
            y_axis_label='y'
)

p.line(x=x,y=y,width=2)

p.circle(x,y,size=10)

st.bokeh_chart(p)

#1. scatterplot bw total_bill and tip.

#2. scatter plot bw total_bill and tip colro by options.

#3. (sex, smoker ,day, time)

data = pd.read_csv('tips.csv')

#1.

st.subheader('scatterplot bw total_bill and tip.')

p = figure(title='scatterplot bw total bill vs tips.')


p.circle(x='total_bill',y='tip',source=data,size=10)

st.bokeh_chart(p)

#2.

st.markdown('---')

st.subheader('scatter plot bw total_bill and tip colro by options.')

p = figure(title='Scatter plot coloring by categories')

select = st.selectbox('Select the categories',('sex','day','smoker','day','time'))

color_palette = ['blue','red','green','#CCCCFF','black']

unique_cats = data[select].unique()

index_cmap = factor_cmap(select, color_palette[:len(unique_cats)], factors = sorted(unique_cats) )

p.circle('total_bill','tip',source = data,fill_color = index_cmap,size=12,legend=select)

st.bokeh_chart(p)



