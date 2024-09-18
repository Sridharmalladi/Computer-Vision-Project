# Computer-Vision-Project
#Primary Color Detection with Webcam

Summary:
This project uses Python and OpenCV to create a real-time color detection system that can identify primary colors (Red, Green, Blue, Yellow) using a webcam. The program captures the video stream, processes the frames, and highlights the detected primary colors on the screen.

Features:
Real-Time Color Detection: Detects primary colors (Red, Green, Blue) in real-time using a live webcam feed.
Simple GUI: Shows the original video feed alongside the color-detected output.
Customizable Detection: Easy to modify the thresholds for detecting different shades or more colors.
Efficient and Lightweight: Uses OpenCV for fast image processing and real-time performance.
Requirements
Before you run the project, make sure you have the following libraries installed:

How It Works:
Capture Video: The program captures the live video feed from the webcam.
Convert to HSV: Each frame is converted from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value) format to make color detection easier.
Color Masking: The HSV values are then filtered using color ranges to detect Red, Green, and Blue.
Display Output: The original frame and the processed frame (with detected colors) are displayed side-by-side in real-time.
