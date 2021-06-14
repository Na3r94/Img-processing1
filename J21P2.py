import cv2

img = cv2.imread('2.Jpg')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

rows = img.shape[0]
cols = img.shape[1]

for i in range(rows):
    for j in range(cols):
        img[i, j] = 255 - img[i, j]

cv2.imshow('Output', img)
cv2.waitKey()