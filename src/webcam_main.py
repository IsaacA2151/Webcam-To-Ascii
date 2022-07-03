import cv2, time
import image_to_ascii
import sys, os

WEB_IMG_STORE = "../imgs/webcam_feed"
manage_imgs = True      # When set to True, images in the "../imgs/webcam_feed" directory will be automatically deleted while running

if sys.platform == "linux":
    cap = cv2.VideoCapture(0)
else:
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
count = 0

cap.set(3, 320)     # width
cap.set(4, 180)     # height

start = time.time()
time_passed = 0.01
max_imgs = 30
ascWidth = 150

def restore_dir():
    os.system("rm -Rfv {}".format(WEB_IMG_STORE))
    os.system("mkdir {}".format(WEB_IMG_STORE))

while True:
    fname = "{}/capture{}.jpg".format(WEB_IMG_STORE,count)
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1) & 0xFF


    if (time.time() - start) > time_passed:
        count += 1

        if count < max_imgs:
            cv2.imwrite(fname, frame)
            asc = image_to_ascii.ToAscii(fileName=fname,asciiWidth=ascWidth,PIL=True)
            text = asc.main()
            text += "\nOG {} x {}\nNEW {} x {}\nIMG COUNT: {}".format(asc.w,asc.h,asc.width,asc.height,count)
            print("\n"*300)
            print(text)
        else:
            if manage_imgs:
                restore_dir()
                count = 0
            else:
                break

        start = time.time()

print("\n\nMAX IMAGES REACHED AT {} ".format(count))
