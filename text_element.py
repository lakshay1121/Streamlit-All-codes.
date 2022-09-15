import streamlit as st

#title.

st.title('Using st.title you can display the text in title format')
st.caption('Using caption in a title')
#headers.

st.header('The text inside st.header is an header format')
st.caption('caption for header')

#subheader.

st.subheader('The text inside st.subheader is an subheader format')
st.caption('caption for subheader')

# display the code in page.

st.markdown('---')

st.subheader('Generate Random Numbers')
body = """
  import numpy as np

  def generate_random(size):

    rand = np.random.randn(size=size)
    return rand

  number = generate_random(10)

"""

st.code(body,language='python')

# Latex.

st.subheader('Latex')

formula = """
  
  a + ar + ar^2 + ar^3 +\cdots + a r^ (n-1) = \sum_{k=0}^{n-1} a r^k

"""

st.latex(formula)