import cv2
from cv2 import rotate
import imutils
camera_id = '6783f98f889341cc80d238351fa63edd.mov'
# khai bao doi tuong video
video = cv2.VideoCapture(camera_id)
rotate = 0
while True:
    # ret: ket qua tra ve, frame: khung hinh doc duoc tu camera
    ret, frame = video.read()
    if ret:
        if rotate != 0:
            frame = imutils.rotate(frame, rotate)
        cv2.imshow("Anh tu video", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('a'):
        rotate = 90
    elif key == ord('d'):
        rotate = -90
cv2.release() #ngung viec chiem dung tu camera
cv2.destroyAllWindows()