import cv2

img = cv2.imread('4.jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

rows = img.shape[0]
cols = img.shape[1]

for i in range(rows):
    for j in range(cols):
        if img[i,j] < 40:
            img[i,j] = 0
        else:
            img[i,j] = 250


cv2.imshow('Output', img)
cv2.waitKey()