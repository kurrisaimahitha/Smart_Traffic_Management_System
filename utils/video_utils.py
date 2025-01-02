# import cv2
#
# def read_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     frames = []
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frames.append(frame)
#     cap.release()
#     return frames
#
# import cv2
# import os
#
# def save_video(output_video_frames, output_video_path):
#     if not output_video_frames:
#         raise ValueError("No frames to save.")
#
#     # Ensure the output directory exists
#     output_dir = os.path.dirname(output_video_path)
#     if output_dir and not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#
#     # Use a codec and write the video
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use 'mp4v' for MP4 files
#     frame_height, frame_width = output_video_frames[0].shape[:2]
#     out = cv2.VideoWriter(output_video_path, fourcc, 24.0, (frame_width, frame_height))
#
#     for frame in output_video_frames:
#         out.write(frame)
#
#     out.release()
#     print(f"Video saved successfully at {output_video_path}")
#
#
# def detect_vehicles(frames):
#     # Placeholder for vehicle detection
#     print("Detecting vehicles...")
#     return []  # Replace with actual detection logic

import cv2

def read_video(video_path):

    cap = cv2.VideoCapture(video_path)
    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames


def save_video(output_video_frames, output_video_path):

    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(output_video_path, fourcc, 24.0, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    for frame in output_video_frames:
        out.write(frame)
    out.release()

def detect_vehicles(frames):
    pass
