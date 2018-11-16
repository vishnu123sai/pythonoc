import cv2

cap=cv2.VideoCapture(0)

if cap.isOpened():
    ret,frame=cap.read()
    print(ret)
    print(frame)
else:
    ret=False

print("enter ESC key to close the window and s to save and close")
img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("picture",cv2.WINDOW_AUTOSIZE)
cv2.imshow('picture',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyWindow('picture')
elif k==ord('s'):
    cv2.imwrite('picture.jpg',img)
    cv2.destroyWindow('picture')

cap.release()
