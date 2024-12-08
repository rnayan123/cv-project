




# -------------------------------------------------------------------
# # import cv2
# # import streamlit as st
# #
# # st.title("GestureChatBot")
# #
# # # Initialize session state for controlling video capture
# # if 'started' not in st.session_state:
# #     st.session_state.started = False
# # if 'stop' not in st.session_state:
# #     st.session_state.stop = False
# #
# # # Function to capture and display video frames
# # def capture_video():
# #     cap = cv2.VideoCapture(0)
# #     frame_placeholder = st.empty()
# #
# #     while not st.session_state.stop:
# #         ret, frame = cap.read()
# #         if not ret:
# #             st.error("Failed to capture image")
# #             break
# #
# #         # Convert the frame to RGB (OpenCV uses BGR by default)
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #
# #         # Display the frame in Streamlit
# #         frame_placeholder.image(frame_rgb, channels="RGB")
# #
# #         # Check if stop button is pressed
# #         if st.session_state.stop:
# #             break
# #
# #     cap.release()
# #     cv2.destroyAllWindows()
# #
# # # Display the video controls in a card
# # # st.markdown("### Video Controls")
# # if not st.session_state.started:
# #     if st.button("Start Video"):
# #         st.session_state.started = True
# #         st.session_state.stop = False
# #         st.experimental_rerun()
# # else:
# #     if st.button("Stop Video"):
# #         st.session_state.stop = True
# #         st.session_state.started = False
# #         st.experimental_rerun()
# #
# # # Start video capture if started
# # if st.session_state.started and not st.session_state.stop:
# #     capture_video()
# #
# #
# #
# # # Display a separate card with a form containing a text area and a send button
# # st.markdown("### Chat with Bot:")
# # with st.form(key='message_form'):
# #     message = st.text_area("Enter your message")
# #     submit_button = st.form_submit_button(label="Send")
# #
# #     if submit_button:
# #         st.success(f"Message sent: {message}")
#
#
#
# # import cv2
# # import streamlit as st
# #
# # st.title("GestureChatBot")
# #
# # # Initialize session state for controlling video capture
# # if 'started' not in st.session_state:
# #     st.session_state.started = False
# # if 'stop' not in st.session_state:
# #     st.session_state.stop = False
# #
# # # Function to capture and display video frames
# # def capture_video():
# #     cap = cv2.VideoCapture(0)
# #     frame_placeholder = st.empty()
# #
# #     while not st.session_state.stop:
# #         ret, frame = cap.read()
# #         if not ret:
# #             st.error("Failed to capture image")
# #             break
# #
# #         # Convert the frame to RGB (OpenCV uses BGR by default)
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #
# #         # Display the frame in Streamlit
# #         frame_placeholder.image(frame_rgb, channels="RGB")
# #
# #         # Check if stop button is pressed
# #         if st.session_state.stop:
# #             break
# #
# #     cap.release()
# #     cv2.destroyAllWindows()
# #
# # # Display the video controls in a card
# # st.header("Video Controls")
# # if not st.session_state.started:
# #     if st.button("Start Video"):
# #         st.session_state.started = True
# #         st.session_state.stop = False
# #         st.experimental_rerun()
# # else:
# #     if st.button("Stop Video"):
# #         st.session_state.stop = True
# #         st.session_state.started = False
# #         st.experimental_rerun()
# #
# # # Start video capture if started
# # if st.session_state.started and not st.session_state.stop:
# #     capture_video()
# #
# # # Display a separate card with a form containing a text area and a send button
# # st.header("Chat with Bot")
# # with st.form(key='message_form'):
# #     message = st.text_area("Enter your message")
# #     submit_button = st.form_submit_button(label="Send")
# #
# #     if submit_button:
# #         # Simulating bot response for demonstration
# #         bot_response = f"Bot:\n{message}"
# #         st.text(bot_response)
#
#
#
#
# # import cv2
# # import streamlit as st
# # import requests
# #
# # st.title("GestureChatBot")
# #
# # # Initialize session state for controlling video capture
# # if 'started' not in st.session_state:
# #     st.session_state.started = False
# # if 'stop' not in st.session_state:
# #     st.session_state.stop = False
# #
# # # Function to capture and display video frames
# # def capture_video():
# #     cap = cv2.VideoCapture(0)
# #     frame_placeholder = st.empty()
# #
# #     while not st.session_state.stop:
# #         ret, frame = cap.read()
# #         if not ret:
# #             st.error("Failed to capture image")
# #             break
# #
# #         # Convert the frame to RGB (OpenCV uses BGR by default)
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #
# #         # Display the frame in Streamlit
# #         frame_placeholder.image(frame_rgb, channels="RGB")
# #
# #         # Check if stop button is pressed
# #         if st.session_state.stop:
# #             break
# #
# #     cap.release()
# #     cv2.destroyAllWindows()
# #
# # # Define Gemini API endpoint and credentials
# # GEMINI_API_URL = 'https://api.example.com'  # Replace with actual Gemini API URL
# # API_KEY = 'AIzaSyCqHmnjQAEeVhpBDBBJNwoioTQ0isFiz8M'
# # API_SECRET = 'YOUR_API_SECRET'
# #
# # # Function to fetch response from Gemini API
# # def get_gemini_response(message):
# #     headers = {
# #         'Content-Type': 'application/json',
# #         'Authorization': f'Bearer {API_KEY}:{API_SECRET}'
# #     }
# #     data = {
# #         'message': message
# #     }
# #     response = requests.post(GEMINI_API_URL, headers=headers, json=data)
# #     if response.status_code == 200:
# #         return response.json().get('response', 'No response from Gemini')
# #     else:
# #         return f"Error: Failed to fetch response from Gemini API ({response.status_code})"
# #
# # # Display the video controls in a card
# # st.header("Video Controls")
# # if not st.session_state.started:
# #     if st.button("Start Video"):
# #         st.session_state.started = True
# #         st.session_state.stop = False
# #         st.experimental_rerun()
# # else:
# #     if st.button("Stop Video"):
# #         st.session_state.stop = True
# #         st.session_state.started = False
# #         st.experimental_rerun()
# #
# # # Start video capture if started
# # if st.session_state.started and not st.session_state.stop:
# #     capture_video()
# #
# # # Display a separate card with a form containing a text area and a send button
# # st.header("Chat with Bot")
# # with st.form(key='message_form'):
# #     message = st.text_area("Enter your message")
# #     submit_button = st.form_submit_button(label="Send")
# #
# #     if submit_button:
# #         bot_response = get_gemini_response(message)
# #         st.text(f"Bot:\n{bot_response}")
#
#
#
#
#
# import requests
# # import streamlit as st
# # import cv2
# # import google.generativeai as genai
# # import os
# #
# # st.title("GestureChatBot")
# #
# # # Define API Endpoint and API Key
# # API_ENDPOINT = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyCqHmnjQAEeVhpBDBBJNwoioTQ0isFiz8M'
# #
# # # Function to call Google Generative Language API
# # def call_generative_language_api(message):
# #     # headers = {
# #     #     'Content-Type': 'application/json'
# #     # }
# #     # data = {
# #     #     "contents": [
# #     #         {
# #     #             "parts": [
# #     #                 {
# #     #                     "text": message
# #     #                 }
# #     #             ]
# #     #         }
# #     #     ]
# #     # }
# #     genai.configure(api_key='AIzaSyCqHmnjQAEeVhpBDBBJNwoioTQ0isFiz8M')
# #     model = genai.GenerativeModel('gemini-1.5-flash')
# #     response = model.generate_content(message)
# #     # print(response.text)
# #     return response.text
# #     # response = requests.post(API_ENDPOINT, headers=headers, json=data)
# #     # if response.status_code == 200:
# #     #     return response.json().get('contents', [{}])[0].get('parts', [{}])[0].get('text', 'No response from API')
# #     # else:
# #     #     return f"Error: Failed to fetch response from API ({response.status_code})"
# #
# # # Initialize session state for controlling video capture
# # if 'started' not in st.session_state:
# #     st.session_state.started = False
# # if 'stop' not in st.session_state:
# #     st.session_state.stop = False
# #
# # # Function to capture and display video frames
# # def capture_video():
# #     cap = cv2.VideoCapture(0)
# #     frame_placeholder = st.empty()
# #
# #     while not st.session_state.stop:
# #         ret, frame = cap.read()
# #         if not ret:
# #             st.error("Failed to capture image")
# #             break
# #
# #         # Convert the frame to RGB (OpenCV uses BGR by default)
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #
# #         # Display the frame in Streamlit
# #         frame_placeholder.image(frame_rgb, channels="RGB")
# #
# #         # Check if stop button is pressed
# #         if st.session_state.stop:
# #             break
# #
# #     cap.release()
# #     cv2.destroyAllWindows()
# #
# # # Display the video controls in a card
# # # st.header("Video Controls")
# # if not st.session_state.started:
# #     if st.button("Start Video"):
# #         st.session_state.started = True
# #         st.session_state.stop = False
# #         st.experimental_rerun()
# # else:
# #     if st.button("Stop Video"):
# #         st.session_state.stop = True
# #         st.session_state.started = False
# #         st.experimental_rerun()
# #
# # # Start video capture if started
# # if st.session_state.started and not st.session_state.stop:
# #     capture_video()
# #
# # # Display a separate card with a form containing a text area and a send button
# # st.header("Chat with Bot")
# # with st.form(key='message_form'):
# #     message = st.text_area("Enter your message")
# #     submit_button = st.form_submit_button(label="Send")
# #
# #     if submit_button:
# #         if message!="":
# #             bot_response = call_generative_language_api(message)
# #             st.text(f"Bot:\n{bot_response}")
# #         else:
# #             st.text(f"Bot:Enter something,dumbass!")
#
#
#
#
# #
# # import streamlit as st
# # import cv2
# # import google.generativeai as genai
# #
# # st.title("GestureChatBot")
# #
# # # Initialize session state for controlling video capture
# # if 'started' not in st.session_state:
# #     st.session_state.started = False
# # if 'stop' not in st.session_state:
# #     st.session_state.stop = False
# #
# # # Function to capture and display video frames
# # def capture_video():
# #     cap = cv2.VideoCapture(0)
# #     frame_placeholder = st.empty()
# #
# #     while not st.session_state.stop:
# #         ret, frame = cap.read()
# #         if not ret:
# #             st.error("Failed to capture image")
# #             break
# #
# #         # Convert the frame to RGB (OpenCV uses BGR by default)
# #         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #
# #         # Display the frame in Streamlit
# #         frame_placeholder.image(frame_rgb, channels="RGB")
# #
# #         # Check if stop button is pressed
# #         if st.session_state.stop:
# #             break
# #
# #     cap.release()
# #     cv2.destroyAllWindows()
# #
# # # Function to call Google Generative Language API
# # def call_generative_language_api(message):
# #     genai.configure(api_key='AIzaSyCqHmnjQAEeVhpBDBBJNwoioTQ0isFiz8M')  # Replace with your actual API key
# #     model = genai.GenerativeModel('gemini-1.5-flash')
# #     response = model.generate_content(message)
# #     return response.text
# #
# # # Display the video controls in a card
# # st.header("Video Controls")
# # if not st.session_state.started:
# #     if st.button("Start Video"):
# #         st.session_state.started = True
# #         st.session_state.stop = False
# # else:
# #     if st.button("Stop Video"):
# #         st.session_state.stop = True
# #         st.session_state.started = False
# #
# # # Start video capture if started
# # if st.session_state.started and not st.session_state.stop:
# #     capture_video()
# #
# # # Display a separate card with a form containing a text area and a send button
# # st.header("Chat with Bot")
# # with st.form(key='message_form'):
# #     message = st.text_area("Enter your message")
# #     submit_button = st.form_submit_button(label="Send")
# #
# #     if submit_button:
# #         if message.strip() != "":
# #             bot_response = call_generative_language_api(message)
# #             st.text(f"Bot:\n{bot_response}")
# #         else:
# #             st.text(f"Bot: Enter something, dumbass!")  # Example response for empty message
# #
#
#
#
# import cv2
# import streamlit as st
# import requests
# import cv2
# import google.generativeai as genai
#
# st.title("GestureChatBot")
#
# # Initialize session state for controlling video capture
# if 'started' not in st.session_state:
#     st.session_state.started = False
# if 'stop' not in st.session_state:
#     st.session_state.stop = False
#
# # Function to capture and display video frames
# def capture_video():
#     cap = cv2.VideoCapture(0)
#     frame_placeholder = st.empty()
#
#     while not st.session_state.stop:
#         ret, frame = cap.read()
#         if not ret:
#             st.error("Failed to capture image")
#             break
#
#         # Convert the frame to RGB (OpenCV uses BGR by default)
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#
#         # Display the frame in Streamlit
#         frame_placeholder.image(frame_rgb, channels="RGB")
#
#         # Check if stop button is pressed
#         if st.session_state.stop:
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
# # Function to call Google Generative Language API
# def call_generative_language_api(message):
#     genai.configure(api_key='AIzaSyCqHmnjQAEeVhpBDBBJNwoioTQ0isFiz8M')  # Replace with your actual API key
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content(message)
#     return response.text
#
# # Layout for Video Controls
# # st.header("Video Controls")
# # col_video, col_chat = st.columns(2)
#
# # col_chat=st.columns(1)
#
# # with col_video:
# #     if not st.session_state.started:
# #         if st.button("Start Video"):
# #             st.session_state.started = True
# #             st.session_state.stop = False
#
# st.header("Chat with Bot")
# with st.form(key='message_form'):
#     message = st.text_area("Enter your message")
#     submit_button = st.form_submit_button(label="Send")
#
#     if submit_button:
#         bot_response = call_generative_language_api(message)
#         st.text(f"Bot:\n{bot_response}")
#
# # Start video capture if started
# # if st.session_state.started and not st.session_state.stop:
# #     capture_video()
