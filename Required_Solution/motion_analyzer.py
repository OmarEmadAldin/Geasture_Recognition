import numpy as np
from collections import deque

class MotionAnalyzer:
    def __init__(self, history_length=5, threshold=30):
        self.motion_history = deque(maxlen=history_length)
        self.motion_threshold = threshold

    def update_and_get_motion(self, wrist_pos):
        self.motion_history.append(wrist_pos)
        if len(self.motion_history) < 2:
            return ""
        delta = self.motion_history[-1] - self.motion_history[0]
        dx, dy = delta

        if abs(dx) > abs(dy):
            if dx > self.motion_threshold:
                return "Moving Right"
            elif dx < -self.motion_threshold:
                return "Moving Left"
        else:
            if dy > self.motion_threshold:
                return "Moving Down"
            elif dy < -self.motion_threshold:
                return "Moving Up"
        return ""
