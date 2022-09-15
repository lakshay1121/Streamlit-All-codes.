import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('tips.csv')

# st.dataframes to dispaly dataframes.

st.header('st.dataframe')
st.caption('it will dispaly a dataframe as an interactive table')

st.dataframe(data = df , width=1000,  height = 200)

#st.static

st.header('st.table')

st.caption('it will display static table')

st.table(data=df.head())

# data as json. st.json

st.header('st.json')

st.caption('display object or string as a pretty-printed json format.')

json_values = df.head(3).to_dict()

st.json(json_values)