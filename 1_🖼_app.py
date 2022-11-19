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
    token = st.text_input(label='Token')
    link='Can be found [here](https://deepai.org/machine-learning-model/text-generator), for example: quickstart-QUdJIGlzIGNvbWluZy4uLi4K'
    st.markdown(link)
    prompt = st.text_area(label='Prompt')
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
