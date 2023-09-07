import concurrent.futures
import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True, max_num_hands=1)
mp_drawing = mp.solutions.drawing_utils

gesture_names = {
    0: "Fist",
    1: "Open Hand",
    2: "Thumb Up",
    3: "Thumb Down",
    4: "Peace Sign",
    5: "Rock and Roll",
}

def recognize_gesture(hand_landmarks):
    if hand_landmarks is not None:
        thumb_tip = hand_landmarks.landmark[4]
        index_tip = hand_landmarks.landmark[8]
        middle_tip = hand_landmarks.landmark[12]
        ring_tip = hand_landmarks.landmark[16]
        pinky_tip = hand_landmarks.landmark[20]

        if thumb_tip.y < index_tip.y < middle_tip.y < ring_tip.y < pinky_tip.y:
            return gesture_names[0]
        elif all(thumb_tip.x < landmark.x for landmark in [index_tip, middle_tip, ring_tip, pinky_tip]):
            return gesture_names[4]
        elif thumb_tip.y > index_tip.y > middle_tip.y > ring_tip.y > pinky_tip.y:
            return gesture_names[1]
        elif thumb_tip.y < index_tip.y > middle_tip.y > ring_tip.y > pinky_tip.y:
            return gesture_names[2]
        elif thumb_tip.y > index_tip.y < middle_tip.y > ring_tip.y > pinky_tip.y:
            return gesture_names[3]
        elif thumb_tip.y > index_tip.y < middle_tip.y < ring_tip.y < pinky_tip.y:
            return gesture_names[5]
    return "No Gesture"


cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            gestures = list(executor.map(recognize_gesture, results.multi_hand_landmarks))

        for hand_landmarks, gesture in zip(results.multi_hand_landmarks, gestures):
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.putText(frame, f"Gesture: {gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Gesture Recognition", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
