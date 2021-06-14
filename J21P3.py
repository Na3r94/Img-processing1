import cv2

img = cv2.imread('3.Jpg')
img2 = cv2.imread('3.Jpg')

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
img = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

rows = img.shape[0]
cols = img.shape[1]

for i in range(rows):
    for j in range(cols):
        img2[i, j] = img[rows-i-1, cols-j-1]


cv2.imshow('Output', img2)
cv2.waitKey()