import mediapipe as mp
import cv2

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5
)


def draw_keypoints(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    if not results.multi_hand_world_landmarks:
        return frame

    annotated_image = frame.copy()
    for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            annotated_image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style()
        )

    return annotated_image

def get_keypoints(frame):
    results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    return results.multi_hand_landmarks
