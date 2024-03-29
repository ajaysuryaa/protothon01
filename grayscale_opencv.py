import cv2 
pic = cv2.imread('C:/Users/hp/Desktop/car1.png')
cv2.imshow('original',pic)
size = pic.shape
for i in range (0,size[0]):
    for j in range (0,size[1]):
        pic[i][j] = pic[i][j][0]*0.34 + pic[i][j][1]*0.51 + pic[i][j][2]*0.15
thresh = 40 
im_bw = cv2.threshold(pic, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('monochrome',im_bw)
cv2.waitKey(0)
cv2.destroyAllWindows()