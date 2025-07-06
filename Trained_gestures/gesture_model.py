import mediapipe as mp
from mediapipe.tasks.python.vision import GestureRecognizer, GestureRecognizerOptions, RunningMode

class GestureModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.recognizer = self._load_model()

    def _load_model(self):
        options = GestureRecognizerOptions(
            base_options=mp.tasks.BaseOptions(model_asset_path=self.model_path),
            running_mode=RunningMode.VIDEO,
            num_hands=1
        )
        return GestureRecognizer.create_from_options(options)

    def predict(self, mp_image, timestamp_ms):
        return self.recognizer.recognize_for_video(mp_image, timestamp_ms)
