import cv2
url = "http://192.168.100.163:8080" # Your url might be different, check the app
vs = cv2.VideoCapture(url+"/video")

while True:
    ret, frame = vs.read()
    if not ret:
        continue
    # Processing of image and other stuff here
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break