import streamlit as st

st.header("This is the display image using st.image")

st.image('./media/image.jpg' , caption='beautiful city')

st.header('Display video')

video_file = open('./media/waterfalls.mp4' ,'rb')

video_bytes = video_file.read()

st.video(video_bytes)


#displaying audio.

st.header("This is Display Audio")

audio_file = open('./media/audio.mp3','rb')

audio_bytes = audio_file.read()

st.audio(audio_bytes , format = 'audio/ogg')