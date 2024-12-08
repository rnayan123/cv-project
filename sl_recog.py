import cv2
import streamlit as st
import requests
import cv2
import google.generativeai as genai

st.title("GestureChatBot")

# Initialize session state for controlling video capture
if 'started' not in st.session_state:
    st.session_state.started = False
if 'stop' not in st.session_state:
    st.session_state.stop = False

# Function to capture and display video frames
def capture_video():
    cap = cv2.VideoCapture(0)
    frame_placeholder = st.empty()

    while not st.session_state.stop:
        ret, frame = cap.read()
        if not ret:
            st.error("Failed to capture image")
            break

        # Convert the frame to RGB (OpenCV uses BGR by default)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in Streamlit
        frame_placeholder.image(frame_rgb, channels="RGB")

        # Check if stop button is pressed
        if st.session_state.stop:
            break

    cap.release()
    cv2.destroyAllWindows()

st.header("Video Controls")

if not st.session_state.started:
    if st.button("Start Video"):
        st.session_state.started = True
        st.session_state.stop = False
else:
    if st.button("Stop Video"):
        st.session_state.stop = True
        st.session_state.started = False

# Start video capture if started
if st.session_state.started and not st.session_state.stop:
    capture_video()
