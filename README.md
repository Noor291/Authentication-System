# FaceAuth

## Introduction
This FaceAuth application is a Python-based program that uses the face_recognition library to perform face detection and authentication. It allows users to check the authenticity of individuals and register new users for future recognition. The application utilizes a webcam to capture images for processing and stores facial embeddings for recognition.

## Features
- **Check Authenticity**: This feature allows users to capture a live image using their webcam and determine the authenticity of the person in the image. If the person is recognized, their name is displayed; otherwise, it alerts that the person is unknown.

- **Register New User**: Users can register new individuals by capturing their images and associating them with a name. These images are stored for future recognition.

## Structure
- **faceauth.py**: The main script that initiates the application.
- **util.py**: A utility script containing helper functions for capturing images, displaying messages, and handling user registration.
- **/db**: A directory where the facial embeddings of registered users are stored.

## Dependencies
- tkinter: GUI library for creating the application's graphical interface.
- OpenCV (opencv-python): Used for capturing images from the webcam.
- Pillow: Python Imaging Library for image processing.
- face_recognition: A library for face detection and recognition.
- ttkbootstrap: A library for creating themed GUIs.

## Screenshot of the interface
![image](https://github.com/Noor291/FaceAuth/assets/78134535/1e6a3f46-9994-4457-8c59-55c08a7e2112)
![image](https://github.com/Noor291/FaceAuth/assets/78134535/2ca8f895-8c96-4120-88ca-117cf6132a13)
![image](https://github.com/Noor291/FaceAuth/assets/78134535/7a8ed6e8-c8df-40e3-9fe9-5b2942dc5d08)
![image](https://github.com/Noor291/FaceAuth/assets/78134535/4faf1ef4-42a7-45ed-9a4f-1abd571b716d)

