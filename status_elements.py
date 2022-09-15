import streamlit as st
import time

# progress bar.

st.header('st.progress')
st.caption('it will dispaly a progress bar')

# my_bar = st.progress(50)

# changing dynamically value of progress bar.

def progress_bar():

     for pct_complete in range(1,101):

      time.sleep(0.1)
      
      pct_complete = min(pct_complete , 100)
     my_bar.progress(pct_complete)



#spinner


with st.spinner("Something is Processing"):

    my_bar = st.progress(0)
    progress_bar()

    # info.

    st.subheader('st.info')

    st.info("This is information message!")

    st.subheader('st.success')

    st.success("This is st.success")

    st.subheader('st.warning')

    st.warning('This is st.warning')

    st.subheader("st.error")

    st.error("this is error")

    time.sleep(2)

    st.balloons()