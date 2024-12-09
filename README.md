# Sign Language Chatbot 🤲💬

## Project Overview

This innovative multimodal chatbot enables communication through American Sign Language (ASL) hand gesture recognition. The application bridges communication gaps by allowing users to generate chat prompts using hand gestures, making interaction more accessible and inclusive.

## Features

- *Hand Gesture Recognition*: Detect and interpret ASL characters from A to Z
- *Real-time Gesture Tracking*: Uses MediaPipe for accurate hand landmark detection
- *Machine Learning Classification*: Random Forest Classifier for gesture interpretation
- *Streamlit Frontend*: Intuitive and user-friendly web interface
- *Multimodal Input*: Convert hand gestures into text prompts for chatbot interaction

## Technology Stack

- *Computer Vision*: OpenCV
- *Hand Tracking*: MediaPipe
- *Machine Learning*: Random Forest Classifier
- *Frontend*: Streamlit
- *Programming Language*: Python

## Prerequisites

- Python 3.8+
- OpenCV
- MediaPipe
- Streamlit
- scikit-learn
- NumPy

## Installation

1. Clone the repository:
   bash
   git clone https://github.com/rnayan123/cv-project
   cd sign-language-chatbot
   

2. Create a virtual environment:
   bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   

3. Install required dependencies:
   bash
   pip install -r requirements.txt
   

## Usage

Run the Streamlit application:
bash
streamlit run app.py


### How to Use

1. Launch the application
2. Position your hand in front of the camera
3. Make ASL gestures for characters A-Z
4. The system will recognize and convert your gestures into text
5. Send the generated prompt to the chatbot

## Model Training

The Random Forest Classifier is trained on a comprehensive dataset of hand gesture landmarks. Key steps include:

- Data Collection: Gather hand gesture images/videos
- Preprocessing: Extract hand landmarks using MediaPipe
- Feature Engineering: Convert landmarks to feature vectors
- Model Training: Train Random Forest Classifier
- Evaluation: Assess model accuracy and performance

## Performance Metrics

- Gesture Recognition Accuracy: 40%
- Real-time Processing Speed: ~30 FPS
- Supported Characters: A-Z

## Limitations

- Requires good lighting conditions
- Works best with clear, distinct hand gestures
- May have reduced accuracy with complex or fast movements
- More images for training is required

## Future Improvements

- Expand character recognition (numbers, special characters)
- Improve model accuracy through advanced machine learning techniques
- Add support for continuous gesture recognition
- Implement more sophisticated chatbot interactions


## Contact

Username - koushik.das@mca.christuniversity.in and nayan.raj@mca.christuniversity.in

Project Link: [https://github.com/rnayan123/cv-project](https://github.com/yourusername/sign-language-chatbot)

---
Screenshots
![WhatsApp Image 2024-12-09 at 10 41 19](https://github.com/user-attachments/assets/418f024f-cece-41aa-a363-9c631df3fb7b)

![WhatsApp Image 2024-12-09 at 10 41 21](https://github.com/user-attachments/assets/3e828b6d-fff8-4f14-8136-68b3af5781bf)


![WhatsApp Image 2024-12-09 at 10 41 24](https://github.com/user-attachments/assets/85e13e8d-14cf-46f9-9dd6-48c64f01f04f)
