import cv2

img = cv2.imread('lena.jpg')

def mousetriming(event, x, y, flags, param):
        
        global pt1x
        global pt2x
        global pt1y
        global pt2y
        
        if event == cv2.EVENT_LBUTTONDOWN:
            pt1x = (x,y)
            print(pt1x)
        elif event == cv2.EVENT_LBUTTONUP:
            pt2x = (x,y)
            print(pt2x)
            cv2.line(img,(pt1x),(pt2x),(255,0,0),2)
        elif event == cv2.EVENT_RBUTTONDOWN:
            pt1y = (x,y)
            print(pt1y)
        elif event ==cv2.EVENT_RBUTTONUP:
            pt2y = (x,y)
            print(pt2y)
            cv2.line(img,(pt1y),(pt2y),(255,0,0),2)
            dst = img[min(pt1y[0],pt2y[0]):max(pt1y[0],pt2y[0]),min(pt1x[1],pt2x[1]):max(pt1x[1],pt2x[1])]
            cv2.imwrite('triming/tr.jpg',dst)
        cv2.imshow('img',img)
        
        

cv2.imshow('img',img)
cv2.setMouseCallback('img', mousetriming)
cv2.waitKey(0)
cv2.destroyAllWindows()