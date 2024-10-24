from ultralytics import YOLO, checks, hub
checks()

hub.login('1657c21a84c25ad93c2d9be83fa598b5e0f4b38b0c')

model = YOLO('https://hub.ultralytics.com/models/ClU3LFlnkwlXVbYka62e')
results = model.train()
