 # # from utils.video_utils import read_video, save_video, detect_vehicles
# # # from object_tracker.tracker3 import Tracker
# # #
# # # def main():
# # #
# # #     frames = read_video("C:\\Users\\SAI MAHITHA\\PycharmProjects\\pythonProject\\2103099-uhd_2560_1440_30fps.mp4")
# # #
# # #     #object tracking
# # #     obj_tracker = Tracker()
# # #     result = obj_tracker.detect_objects(frames)
# # #     output_frames = obj_tracker.draw_annotations(frames, result)
# #
# #
# # #     save_video(output_frames, "output/123.avi")
# #
# # ###### Main function for 1 image
# #
# # # def main():
# #
# # #     frames = read_video("data/image.jpg")
# #
# # #     #object tracking
# # #     obj_tracker = Tracker()
# # #     result = obj_tracker.detect_frame(frames)
# # #     print(result)
# #
# #     # output_frames = obj_tracker.draw_annotations(frames, result)
# #     #
# #     #
# #     # save_video(output_frames, "output/output.avi")
# #
# # if __name__ == '__main__':
# #     main()
# #
#
# # from ultralytics import YOLO
# # import cv2
# #
# # import utils
# # from sort import *
# # import numpy as np
# # # from sort_tracker import *
# # from utils.util import get_car, read_license_plate, write_csv
# #
# #
# # results = {}
# #
# # mot_tracker = Sort()
# #
# # # load models
# # coco_model = YOLO('yolov8x.pt')
# # license_plate_detector = YOLO("C:\\Users\\SAI MAHITHA\\PycharmProjects\\pythonProject\\venv\\new_best_2nd_dec.pt")
# #
# # # load video
# # cap = cv2.VideoCapture("C:\\Users\\SAI MAHITHA\\PycharmProjects\\pythonProject\\2103099-uhd_2560_1440_30fps.mp4")
# #
# # vehicles = [2, 3, 5, 7]
# #
# # # read frames
# # frame_nmr = -1
# # ret = True
# # while ret:
# #     print(frame_nmr)
# #     frame_nmr += 1
# #     ret, frame = cap.read()
# #     if ret:
# #         results[frame_nmr] = {}
# #         # detect vehicles
# #         detections = coco_model(frame)[0]
# #         detections_ = []
# #         for detection in detections.boxes.data.tolist():
# #             x1, y1, x2, y2, score, class_id = detection
# #             if int(class_id) in vehicles:
# #                 detections_.append([x1, y1, x2, y2, score])
# #
# #         # track vehicles
# #         track_ids = mot_tracker.update(np.asarray(detections_))
# #         # print(track_ids)
# #
# #         # detect license plates
# #         license_plates = license_plate_detector(frame)[0]
# #         for license_plate in license_plates.boxes.data.tolist():
# #             x1, y1, x2, y2, score, class_id = license_plate
# #
# #             # assign license plate to car
# #             xcar1, ycar1, xcar2, ycar2, car_id = get_car(license_plate, track_ids)
# #
# #
# #
# #
# #
# #
# #             if car_id != -1:
# #
# #                 # crop license plate
# #                 license_plate_crop = frame[int(y1):int(y2), int(x1): int(x2), :]
# #
# #                 # process license plate
# #                 license_plate_crop_gray = cv2.cvtColor(license_plate_crop, cv2.COLOR_BGR2GRAY)
# #
# #                 # _, license_plate_crop_thresh = cv2.threshold(license_plate_crop_gray, 64, 255, cv2.THRESH_BINARY_INV)
# #
# #                 # sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# #                 # license_plate_crop_thresh = cv2.filter2D(license_plate_crop, -1, sharpen_kernel)
# #
# #                 # _, license_plate_crop_thresh_1 = cv2.threshold(license_plate_crop_thresh, 70, 255, cv2.THRESH_BINARY_INV)
# #                 license_plate_crop_thresh = license_plate_crop_gray
# #                 object_filename = f"data1/original/{x1}_{car_id}.jpg"
# #                 cv2.imwrite(object_filename, license_plate_crop_thresh)
# #
# #                 # read license plate number
# #                 license_plate_text, license_plate_text_score = read_license_plate(license_plate_crop_thresh)
# #
# #                 if license_plate_text is not None:
# #                     results[frame_nmr][car_id] = {'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
# #                                                   'license_plate': {'bbox': [x1, y1, x2, y2],
# #                                                                     'text': license_plate_text,
# #                                                                     'bbox_score': score,
# #                                                                     'text_score': license_plate_text_score}}
# #
# # # write results
# # write_csv(results, './test1.csv')
#
#
# from utils.video_utils import read_video, save_video, detect_vehicles
# from object_tracker.tracker2 import Tracker
# def main():
#     frames = read_video("video_path") #enter your video path
#
#     track = Tracker()
#     result = track.process_video(frames)
#
# if __name__ == '__main__':
#     main()

from utils.video_utils import read_video, save_video, detect_vehicles
# from object_tracker.tracker_2 import Tracker

# def main():
#
#     frames = read_video("data/traffic_video.mp4")
#
#     #object tracking
#     obj_tracker = Tracker()
#     result = obj_tracker.detect_objects(frames)
#     output_frames = obj_tracker.draw_annotations(frames, result)
#
#
#     output_frames = obj_tracker.process_video(frames)
#
#
#     # save_video(output_frames, "output/123.avi")


from object_tracker.tracker3 import Tracker
def main():
    frames = read_video(r'C:\\Users\\SAI MAHITHA\\PycharmProjects\\pythonProject\\2103099-uhd_2560_1440_30fps.mp4')

    track = Tracker()
    result = track.process_video(frames)

if __name__ == '__main__':
    main()
