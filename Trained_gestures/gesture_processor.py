import cv2
import time
import mediapipe as mp

class GestureApp:
    def __init__(self, gesture_model):
        self.model = gesture_model
        self.cap = cv2.VideoCapture(0)
        self.frame_counter = 0
        self.prev_time = time.time()  # ← For FPS calculation

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            timestamp_ms = self.frame_counter * 33
            self.frame_counter += 1

            result = self.model.predict(mp_image, timestamp_ms)

            if result.gestures:
                top_gesture = result.gestures[0][0].category_name
                print(f"Gesture: {top_gesture}")
                cv2.putText(frame, f"Gesture: {top_gesture}", (30, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # === FPS Calculation ===
            curr_time = time.time()
            fps = 1 / (curr_time - self.prev_time)
            self.prev_time = curr_time
            cv2.putText(frame, f"FPS: {int(fps)}", (30, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

            cv2.imshow("Gesture Recognition", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
