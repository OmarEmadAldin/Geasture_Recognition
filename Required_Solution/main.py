import cv2
import numpy as np
import mediapipe as mp

from video_capture import VideoCaptureService
from hand_detector import HandDetector
from motion_analyzer import MotionAnalyzer
from gesture_recognizer import GestureRecognizer
from display_service import DisplayService

def main():
    video_service = VideoCaptureService()
    hand_detector = HandDetector()
    motion_analyzer = MotionAnalyzer()
    gesture_recognizer = GestureRecognizer(hand_detector.mp_hands)
    display_service = DisplayService()

    while True:
        frame = video_service.get_frame()
        if frame is None:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hand_detector.detect(frame_rgb)

        h, w, _ = frame.shape
        motion_text = ""
        gesture_text = ""

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            lm = hand_landmarks.landmark

            # Wrist motion
            wrist = lm[hand_detector.mp_hands.HandLandmark.WRIST]
            wrist_pos = np.array([wrist.x * w, wrist.y * h])
            motion_text = motion_analyzer.update_and_get_motion(wrist_pos)

            # Gesture recognition
            gesture_text = gesture_recognizer.recognize(lm)

            # Draw landmarks
            display_service.draw_landmarks(frame, hand_landmarks, hand_detector.mp_hands)

        display_service.draw_text(frame, motion_text, (10, 30), (0, 255, 0))
        display_service.draw_text(frame, gesture_text, (10, 70), (255, 0, 0))

        cv2.imshow("Hand Motion and Gestures", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_service.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
