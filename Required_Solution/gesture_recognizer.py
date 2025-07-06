class GestureRecognizer:
    def __init__(self, mp_hands):
        self.mp_hands = mp_hands

    def recognize(self, landmarks):
        finger_tips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP
        ]
        finger_pips = [
            self.mp_hands.HandLandmark.INDEX_FINGER_PIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
            self.mp_hands.HandLandmark.RING_FINGER_PIP,
            self.mp_hands.HandLandmark.PINKY_PIP
        ]

        fingers_extended = []
        for tip, pip in zip(finger_tips, finger_pips):
            if landmarks[tip].y < landmarks[pip].y:
                fingers_extended.append(True)
            else:
                fingers_extended.append(False)

        if all(fingers_extended):
            return "STOP"
        elif all(not f for f in fingers_extended):
            return "MOVE BACKWARD"
        elif fingers_extended[0] and fingers_extended[1] and not fingers_extended[2] and not fingers_extended[3]:
            return "MOVE FORWARD"
        else:
            return ""
