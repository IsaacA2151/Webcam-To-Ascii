import cv2, time
import image_to_ascii

cap = cv2.VideoCapture(0)
count = 0

cap.set(3, 320)     # width
cap.set(4, 180)     # height

start = time.time()
time_passed = 0.2

while True:
    fname = "webcam_feed/capture{}.jpg".format(count)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF


    height, width, channels = frame.shape
    asc = image_to_ascii.ToAscii(height=height,width=width,frame=frame)
    print(asc.main())