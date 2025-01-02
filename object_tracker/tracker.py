from ultralytics import YOLO
import cv2


class Tracker:

    def __init__(self):
        self.model = YOLO("yolov8x.pt")  # Load the YOLOv8 model

    def detect_objects(self, frames):
        detections = []

        for frame in frames:
            detected_objs = self.detect_frame(frame)  # Detect objects in each frame
            detections.append(detected_objs)

        return detections

    def detect_frame(self, frame):
        results = self.model.track(frame, persist=True)[0]  # Run tracking on the frame
        name_dict = results.names  # Get class names dictionary

        detected_objects = {}

        # Loop through each box (detection) in the result
        for box in results.boxes:
            track_id = int(box.id.tolist()[0])  # Get the tracking ID
            result = box.xyxy.tolist()[0]  # Get the bounding box coordinates (xyxy format)
            object_class_id = int(box.cls.tolist()[0])  # Get the class ID
            object_class_name = name_dict[object_class_id]  # Get the class name from the ID

            # Track only the objects you're interested in
            if object_class_name in ["car", "motorcycle", "truck", "bicycle"]:  # Add bike and truck
                detected_objects[track_id] = result  # Store object with its bounding box coordinates

        return detected_objects

    def draw_annotations(self, frames, object_detections):
        output_video_frames = []

        for frame, obj_detected in zip(frames, object_detections):
            for track_id, bbox in obj_detected.items():
                x1, y1, x2, y2 = bbox  # Get the bounding box coordinates

                # Draw rectangle around detected object (red for visualization)
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

                # Optionally, add label for tracking object (like "car", "bike", etc.)
                cv2.putText(frame, f"ID: {track_id}", (int(x1), int(y1) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            output_video_frames.append(frame)

        return output_video_frames
