import cv2

img = cv2.imread('lena.jpg')

dst = cv2.Canny(img,100,100)

cv2.imshow('img',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()