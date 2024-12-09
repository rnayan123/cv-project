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

## Future Improvements

- Expand character recognition (numbers, special characters)
- Improve model accuracy through advanced machine learning techniques
- Add support for continuous gesture recognition
- Implement more sophisticated chatbot interactions

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## License

Distributed under the MIT License. See LICENSE for more information.

## Contact

Your Name - koushik.das@mca.christuniversity.in

Project Link: [https://github.com/rnayan123/cv-project](https://github.com/yourusername/sign-language-chatbot)

---

*Disclaimer*: This project is a prototype and aims to demonstrate the potential of assistive communication technologies.
