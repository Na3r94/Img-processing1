import cv2

image = cv2.imread('Joker.jpeg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

image = cv2.resize(image, (1000, 1000))
rows = image.shape[0]
cols = image.shape[1]
print(image.shape)
for i in range(10):
    for j in range(5):
        if i % 2 == 0:
            image[0+100*i:100+100*i, 0 + 200*j :100 + 200*j] = 255
            image[0+100*i:100+100*i, 100 + 200*j :200 + 200*j] = 0
        elif i % 2 == 1:
            image[0+100*i:100+100*i, 0 + 200*j :100 + 200*j] = 0
            image[0+100*i:100+100*i, 100 + 200*j :200 + 200*j] = 255

cv2.imshow('Joker', image)
cv2.waitKey()