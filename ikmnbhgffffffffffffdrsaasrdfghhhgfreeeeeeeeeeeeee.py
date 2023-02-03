import cv2

# read the image file
img = cv2.imread('C:\\Users\WinstonBai\OneDrive\Pictures\WIN_20220218_17_58_12_Pro.jpg', 2)

ret, bw_img = cv2.threshold(img, 165, 230, cv2.THRESH_BINARY)

# converting to its binary form
bw = cv2.threshold(img, 170, 240, cv2.THRESH_BINARY)

cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()