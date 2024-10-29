# Object Tracking Robot
This project is a Python-based object detection and tracking system designed for autonomous robotics. Using OpenCV and color-based tracking, the system can recognize and follow a specific object shown to the camera, making it ideal for projects that require simple yet effective tracking capabilities.

# Table of Contents
1. Project Overview
2. Features
3. Requirements
4. Installation
5. Usage
6. Project Structure
7. Configuration
8. License

1.Project Overview:-
This project uses a webcam feed to detect an object of a specific color range in HSV format, initialize tracking, and follow the object in real-time. By adjusting the color range in HSV, the tracker can recognize and lock onto any object matching that color range, updating its position as it moves.

2.Features
   * Object Detection: Identifies objects within a specified color range in HSV.
   * Object Tracking: Follows the detected object in real-time using OpenCV’s tracking algorithms.
   * Easy Configuration: Adjustable HSV color values allow the system to recognize various objects.
   * Efficient Real-Time Performance: Optimized for fast, responsive tracking on a range of systems.

3.Requirements
   * Python 3.x
   * OpenCV
   * NumPy

4.Installation
   * Clone the Repository
   * Set Up a Virtual Environment (Optional)
   * Install Dependencies
   
5.Usage
   * Configure the Color Range:
      Run hsv_detection.py to find the HSV color range for the object you want to track.
      Update color_lower and color_upper in main.py with the detected values.
      Run the Object Tracking System:
      # code to run
      python src/main.py
   * Control:
      The application will detect and start tracking the object.
      Press q to quit the application

6.Project Structure
   1. src folder:
      * main.py                # Main program to run object tracking
      * detector.py            # Function for object detection
      * tracker.py             # Function for object tracking
   2. hsv_detection.py         # Helper script to get HSV values for objects
   3. requirements.txt         # Project dependencies
   4. README.md

7.Configuration
   To customize the object detection for your own object:
   Run hsv_detection.py: Adjust the trackbars until the object appears correctly in the result view.

8.License 
   This project is licensed under MIT license
