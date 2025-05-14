import cv2

img = cv2.imread('lena.jpg')
dst = cv2.Canny(img,100,100)
dst = cv2.cvtColor(dst,cv2.IMREAD_COLOR)
print(img.shape)
print(dst.shape)
gousei = cv2.addWeighted(img,0.6, dst, 0.4,0.0)
gousei = cv2.cvtColor(img,cv2.IMREAD_COLOR)
def onMouse(event,x,y,flags,params):
    global img
    if event == cv2.EVENT_MOUSEMOVE :
        
        
        print(x)
        cv2.imshow('img',dst)
        
    

cv2.imshow('img',gousei)
cv2.setMouseCallback('img',onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()