import os
import pickle
import streamlit as st
import requests

os.environ["REPLICATE_API_TOKEN"] = 'asdas'

# st.set_page_config(layout="wide")

st.title('Stable diffusion test')

with st.form(key='form'):

    prompt = st.text_area(label='Enter prompt')
    
    st.form_submit_button()

    
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': prompt,
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)

image_url = r.json()['output_url']

if prompt:
    st.image(image_url)
else:
    st.warning('Enter prompt.')
