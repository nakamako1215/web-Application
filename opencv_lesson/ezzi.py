import cv2
import numpy as np
img = cv2.imread('lena.jpg')
dst = cv2.Canny(img,100,100)
dst = cv2.cvtColor(dst,cv2.IMREAD_COLOR)

print(img.shape)
print(dst.shape)

gousei = img.copy()

def onMouse(event, x, y, flags, params):
    if event == cv2.EVENT_MOUSEMOVE:
        # 合成用のマスクを作成（imgと同じサイズ）
        mask = np.zeros_like(img)
        mask[:, :x] = dst[:, :x]  # xピクセルまでエッジをコピー
        
        # エッジ部分だけ0.5合成
        gousei = cv2.addWeighted(img, 1.0, mask, 1.0, 0.0)
        
        cv2.imshow('img', gousei)

        
    

cv2.imshow('img',gousei)
cv2.setMouseCallback('img',onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()