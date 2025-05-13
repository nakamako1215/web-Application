import cv2

img = cv2.imread('lena.jpg')

def mousetriming(event, x, y, flags, param):
        global pt1
        global pt2
        if event == cv2.EVENT_LBUTTONDOWN:
            pt1 = (x,y)
            print(pt1)
        elif event == cv2.EVENT_RBUTTONDOWN:
            pt2 = (x,y)
            print(pt2)
            cv2.line(img,(pt1),(pt2),(255,0,0),2)
        cv2.imshow('img',img)

cv2.imshow('img',img)
cv2.setMouseCallback('img', mousetriming)

cv2.waitKey(0)
cv2.destroyAllWindows()