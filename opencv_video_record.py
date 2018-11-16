import cv2
window_name="Live Recording"
video=cv2.VideoCapture(0)
if video.isOpened():
    ret,frame=video.read()
else:
    ret=False
resolution=(640,480)
framerate=30
filename="video.avi"
codec=cv2.VideoWriter_fourcc('X','V','I','D')
video_rec=cv2.VideoWriter(filename,codec,framerate,resolution)
while ret :
    ret,frame=video.read()

    cv2.imshow(window_name,frame)
    video_rec.write(frame)
    key=cv2.waitKey(1)
    if key == 27:
        ret=False
        cv2.destroyWindow(window_name)
        video_rec.release()

print("video recording closed")
 
