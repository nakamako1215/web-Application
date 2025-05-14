import cv2

img = cv2.imread('lena.jpg')

dst = cv2.Canny(img,100,100)

def onMouse(event,x,y,flags,params):
    global pt1 , img
    if event == cv2.EVENT_MOUSEMOVE :
        pt1 = x
        print(pt1)
    

cv2.imshow('img',dst)
cv2.setMouseCallback('img',onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()