#Main Code
#
# import cv2
# import streamlit as st
# import requests
# import cv2
# import google.generativeai as genai
# from streamlit_js_eval import streamlit_js_eval
#
# st.title("MultiModal ChatBot")
# # Function to call Google Generative Language API
# def call_generative_language_api(message):
#     genai.configure(api_key='AIzaSyCskNIOW63GMxEchQFhLLcjsMjTHLDWuZA')  # Replace with your actual API key
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content(message)
#     return response.text
#
#
# if 'recognized_string' in st.session_state:
#     initial_message = st.session_state['recognized_string']
#     st.write("Recognized String from Sign Language:", initial_message)
#     auto_submit=True
# else:
#     initial_message = ""
#     st.write("No recognized string found. Go to the Sign Language Recognition page and recognize some signs.")
#     auto_submit=False
# with st.form(key='message_form'):
#     message = st.text_area("Enter your message",value=initial_message.lower())
#     submit_button = st.form_submit_button(label="Send")
#
#     if submit_button:
#         bot_response = call_generative_language_api(message)
#         st.text(f"Bot:\n{bot_response}")
# if auto_submit:
#     streamlit_js_eval(js_code="document.querySelector('form').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))")



# Updated code
import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

st.title("MultiModal ChatBot")

# Function to call Google Generative Language API
def call_generative_language_api(message):
    genai.configure(api_key='AIzaSyCskNIOW63GMxEchQFhLLcjsMjTHLDWuZA')  # Replace with your actual API key
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(message)
    return response.text

# Function to read the response aloud using gTTS
def read_aloud(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("afplay response.mp3")  # macOS command to play the mp3 file
    # For Windows use: os.system("start response.mp3")
    # For Linux use: os.system("mpg321 response.mp3")

if 'recognized_string' in st.session_state:
    initial_message = st.session_state['recognized_string']
    st.write("Recognized String from Sign Language:", initial_message)
    auto_submit = True
else:
    initial_message = ""
    st.write("No recognized string found. Go to the Sign Language Recognition page and recognize some signs.")
    auto_submit = False

# Initialize session state for the bot response
if 'bot_response' not in st.session_state:
    st.session_state['bot_response'] = ""

with st.form(key='message_form'):
    message = st.text_area("Enter your message", value=initial_message.lower())
    submit_button = st.form_submit_button(label="Send")

    if submit_button:
        st.session_state['bot_response'] = call_generative_language_api(message)
        st.text(f"Bot:\n{st.session_state['bot_response']}")

# Place the Read Aloud button outside the form
if st.session_state['bot_response']:
    if st.button("Read Aloud"):
        read_aloud(st.session_state['bot_response'])

if auto_submit:
    from streamlit_js_eval import streamlit_js_eval
    streamlit_js_eval(
        js_code="document.querySelector('form').dispatchEvent(new Event('submit', {cancelable: true, bubbles: true}))"
    )