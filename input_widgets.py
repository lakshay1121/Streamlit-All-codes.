import streamlit as st
import pandas as pd
import numpy as np
import os


#load the data.

data = pd.read_csv('tips.csv')

def display_display_random(df):

    sample = df.sample(5)

    return sample


# button widget.

st.subheader("Display randome 5 rows")
button = st.button('Display random 5 rows')

if button:

   sample =  display_display_random(data)
   st.dataframe(sample)

#checkbox.

st.markdown('---')

st.subheader('st.checkbox')

agree = st.checkbox('I agree to the terms and conditions') # returns a boolean value.

st.write("status" , agree)

## multiple checkbox.

with st.container():

    st.info('What technologies you know?')

    python = st.checkbox('Python')
    datascience = st.checkbox('Data Science')
    react = st.checkbox('React')
    javascript = st.checkbox('Javascript')


    tech_button = st.button('Submit')

    if tech_button:

        tech_dict = {

            'Python' : python,
            'Data science': datascience,
            'React':react,
            'Javascript':javascript
        }

        st.json(tech_dict)


#radio buttons.

st.markdown('---')

st.subheader("st.radio")

radio_buttons = st.radio('what is your fav color?' , ('white', 'Black' , 'Pink'))


st.write("your fav color is:", radio_buttons)

#select box.

st.markdown('---')

st.subheader('st.selectbox')

select_box = st.selectbox('What skill you want to learn?' , ('java' ,'python','c++','javascript'))

st.write("you selected" , select_box)

#multiselect box.

st.markdown('---')

st.subheader('st.multiselect')

options = st.multiselect('What skill you want to learn?' 
,
['java','python','C++','javascript']

)

st.write("you selected" , options)

#slider.

st.markdown('---')
st.subheader('st.slider')

loan = st.slider(
    'what is the loan amount you are looking for?' , 0 , 100000, 1000 , 1000
)

st.write('loan amount is:' , loan)

# text input.

st.markdown('---')

st.subheader('st.text_input, st.number_input ,st.date_input')

with st.container():

    name = st.text_input('Please enter your name')

    age = st.number_input('what is your age?' , min_value = 5 , max_value = 100, value = 18, step = 1)

    describe = st.text_area('Description',height=150)

    dob = st.date_input("select your DOB")

    submit_button = st.button('get your details')

    if submit_button:

        info = {
            'Name':name,
            'Age':age,
            'Date of Birth':dob,
            'Description':describe
        }

        st.json(info)


# file uploader.


st.markdown('---')

st.subheader('st.file_uploader')

uploaded_file = st.file_uploader('Choose a file')

save_button = st.button('save file')

if save_button:
    if uploaded_file is not None:
        
         with open(os.path.join("./save_folder1",uploaded_file.name) , mode='wb') as f:

            f.write(uploaded_file.getbuffer())

         st.success('File uploaded successfully!')

    else:

        st.warning('Please select a file!')