#from ultralytics import solutions

#solutions.ParkingPtsSelection()

import cv2

from ultralytics import solutions

# Video capture
cap = cv2.VideoCapture(r"C:/Users/LENOVO/Parking_Management_System_Using_YOLOv11/carPark.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Video writer
video_writer = cv2.VideoWriter("parking management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize parking management object
parking_manager = solutions.ParkingManagement(
    model=r"C:\Users\LENOVO\Parking_Management_System_Using_YOLOv11\yolov11n_- visdrone.pt",  # path to model file
    json_file=r"C:\Users\LENOVO\Parking_Management_System_Using_YOLOv11\bounding_boxes.json",  # path to parking annotations file
)

while cap.isOpened():
    ret, im0 = cap.read()
    if not ret:
        break
    im0 = parking_manager.process_data(im0)
    video_writer.write(im0)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
