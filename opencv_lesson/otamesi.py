import cv2

img = cv2.imread('lena.jpg')
img1 = img[100:200,300:400] 
cv2.imshow('img',img)
cv2.imshow('img1',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()