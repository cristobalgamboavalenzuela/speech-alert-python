# 🎙️ Speech Alert System (Keyword Detection)

This project is a real-time speech recognition system that listens to ambient audio and detects predefined keywords. When a keyword is detected, the system triggers both a voice alert and a visual popup notification.

## 🚀 Features
- Real-time audio listening using microphone
- Keyword detection in Spanish
- Voice alert using text-to-speech
- Visual alert with popup window
- Multithreading for non-blocking alerts

## 🧠 Technologies Used
- Python
- SpeechRecognition
- pyttsx3
- Tkinter
- Threading

## ⚙️ How it works
1. The system listens continuously through the microphone.
2. Audio is converted to text using Google Speech Recognition.
3. If a keyword is detected:
   - A voice alert is triggered
   - A popup window is displayed
