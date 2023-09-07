# Hand_Gesture_Recognition
Hand Gesture ecognition OpenCV (Open Source Computer Vision Library) and MediaPipe to perform real-time hand gesture recognition from a webcam feed. It can recognize six different hand gestures: Fist, Open Hand, Thumb Up, Thumb Down, Peace Sign, and Rock and Roll.

<p align="center"><img src="https://how2electronics.com/wp-content/uploads/2020/01/Gesture-Recognition-and-Its-Application-in-Machine-Learning-1000x528.jpg"></p>

  <h1>Code Explanation</h1>

  <h2>1. Import Libraries:</h2>
    <p>
        The code starts by importing the necessary libraries, including <code>concurrent.futures</code>, <code>cv2</code>
        (OpenCV), and <code>mediapipe</code>.
    </p>

  <h2>2. Initialize MediaPipe Hands Model:</h2>
    <p>
        It initializes the MediaPipe Hands model for hand landmark detection with some configuration settings. It specifies
        that it should work in static image mode and detect a maximum of one hand.
    </p>

  <h2>3. Define Gesture Names:</h2>
    <p>
        A dictionary <code>gesture_names</code> is defined to map gesture codes to their names.
    </p>

  <h2>4. Gesture Recognition Function:</h2>
    <p>
        The <code>recognize_gesture</code> function takes hand landmarks as input and uses the positions of specific
        landmarks to recognize gestures. It returns the name of the recognized gesture.
    </p>

  <h2>5. Open Camera Stream:</h2>
    <p>
        It opens the camera stream using OpenCV (<code>cv2.VideoCapture</code>).
    </p>

  <h2>6. Main Loop:</h2>
    <p>
        The code enters a main loop that continuously captures frames from the camera.
    </p>

  <h2>7. Process Frames:</h2>
    <p>
        Each frame is processed within the loop:
        <ul>
            <li>It converts the frame from BGR to RGB color space.</li>
            <li>It processes the frame using the MediaPipe Hands model to detect hand landmarks.</li>
        </ul>
    </p>

  <h2>8. Multi-Hand Landmarks Handling:</h2>
    <p>
        If multiple hand landmarks are detected in the frame, it uses a ThreadPoolExecutor to parallelize the gesture
        recognition process for each detected hand.
    </p>

  <h2>9. Drawing Landmarks and Displaying Gestures:</h2>
    <p>
        For each detected hand, it draws landmarks and hand connections on the frame using
        <code>mp_drawing.draw_landmarks</code>. It also puts text on the frame to display the recognized gesture.
    </p>

  <h2>10. Display the Frame:</h2>
    <p>
        The processed frame is displayed in a window titled "Hand Gesture Recognition" using
        <code>cv2.imshow</code>.
    </p>

  <h2>11. Quit on 'q' Key Press:</h2>
    <p>
        The program checks for a 'q' key press, and if it detects it, the loop breaks.
    </p>

  <h2>12. Release Resources:</h2>
    <p>
        After the loop exits, it releases the camera resource (<code>cap.release()</code>) and closes all OpenCV windows
        (<code>cv2.destroyAllWindows()</code>).
    </p>
