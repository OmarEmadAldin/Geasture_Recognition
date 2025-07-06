import cv2
import mediapipe as mp

class DisplayService:
    @staticmethod
    def draw_landmarks(frame, hand_landmarks, mp_hands):
        mp.solutions.drawing_utils.draw_landmarks(
            frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    @staticmethod
    def draw_text(frame, text, position, color):
        cv2.putText(frame, text, position,
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
