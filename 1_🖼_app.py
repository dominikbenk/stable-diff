import os
import streamlit as st
import requests

st.set_page_config(
    page_title="Text-to-image app",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.title('Text-to-image generator')

with st.form(key='form'):
    token = st.text_input()
    prompt = st.text_area(label='Enter prompt')
    st.form_submit_button()

if prompt and token:
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': prompt,
        },
        headers={'api-key': token}
    )
    image_url = r.json()['output_url']
    st.image(image_url)
    
else:
    st.warning('Enter prompt and token.')
