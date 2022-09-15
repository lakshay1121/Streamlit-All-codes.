import streamlit as st
import pandas as pd
import numpy as np

st.write("hello world")

st.title("welcome to streamlit app api's")

#displaying panda dataframe.

df = pd.DataFrame({

    'first-column':[1,2,3,4],
    'second-column':[10,20,30,40]
})

st.write(df)

#displaying numpy array.

st.write(np.array([1,2,3,4]))

#magic  commands.

df1 = pd.DataFrame({
   'col1':[1,2,3,4]
})


#magic is tthe command below.
df1

x = 10 
