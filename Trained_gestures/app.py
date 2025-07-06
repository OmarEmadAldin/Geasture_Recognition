from gesture_model import GestureModel
from gesture_processor import GestureApp  # Assuming these are in separate files

def main():
    model_path = "F:\Omar 3amora\Gesture Recognition\Mediapipe_solution\gesture_recognizer.task"  
    gesture_model = GestureModel(model_path)
    app = GestureApp(gesture_model)
    app.run()

if __name__ == "__main__":
    main()
