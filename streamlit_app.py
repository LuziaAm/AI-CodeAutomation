import streamlit as st
from langchain.llms import OpenAI
# from langchain_community.llms import OpenAI
import pandas as pd
import numpy as np
import time

st.title("🦜Code For Test Automation")

openai_api_key = st.sidebar.text_input('To type API Key and Press ENTER for send Key')

if not openai_api_key.startswith('sk-'):
  st.sidebar.warning('Please enter your OpenAI API key!', icon='⚠')

if openai_api_key.startswith('sk-'):
  api_key = openai_api_key
  print(openai_api_key)
  st.sidebar.write("Key saved")

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  textllm = llm(input_text)
  st.write(textllm)
  return textllm


# Custom CSS to modify the textarea width and height
custom_css = '''
<style>
    textarea.stTextArea {
        width: 800px !important;
        height: 400px !important;
    }
</style>
'''

st.write(custom_css, unsafe_allow_html=True)

# st.title("Input your Test Case Text")
user_input = st.text_area("Type your text here:")
submitted = st.button('Submit')

if submitted is True:
    code = generate_response(user_input)
    st.download_button("Download Python File", code, file_name='code.py')