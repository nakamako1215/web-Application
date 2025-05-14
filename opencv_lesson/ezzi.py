import cv2

img = cv2.imread('lena.jpg')



def onMouse(event,x,y,flags,params):
    global pt1 , img
    if event == cv2.EVENT_MOUSEMOVE :
        dst = cv2.Canny(img,x,y)
        cv2.imshow('img',dst)
        
    

cv2.imshow('img',img)
cv2.setMouseCallback('img',onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()