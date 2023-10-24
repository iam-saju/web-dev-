import cv2

img=cv2.imread('1stimage.png',-1)
print(img)
cv2.imshow('img',img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows() 
else:
    cv2.imwrite('sat.jpeg',img)
    cv2.destroyAllWindows() 