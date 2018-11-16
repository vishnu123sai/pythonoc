import cv2
window_name="Live Recording"
video=cv2.VideoCapture(0)
if video.isOpened():
    ret,frame=video.read()
else:
    ret=False

while ret :
    ret,frame=video.read()

    cv2.imshow(window_name,frame)
    key=cv2.waitKey(1)
    if key == 27:
        ret=False
        cv2.destroyWindow(window_name)

print("video recording closed")
