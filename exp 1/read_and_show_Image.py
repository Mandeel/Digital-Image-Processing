#pre-built OpenCV packages for Python
# https://docs.opencv.org/3.4.7/d1/dfb/intro.html
import cv2

# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56
# https://docs.opencv.org/master/d4/da8/group__imgcodecs.html#ga61d9b0126a3e57d9277ac48327799c80
imgGray = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
imgColor = cv2.imread('image.jpg', cv2.IMREAD_COLOR)

 
#https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#imshow
cv2.imshow('Gray Image',imgGray)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html?highlight=waitkey#waitkey
cv2.waitKey(0)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#destroywindow
cv2.destroyWindow('Gray Image')

cv2.imshow('Color Image',imgColor)
cv2.waitKey(0)

# https://docs.opencv.org/2.4/modules/highgui/doc/user_interface.html#destroyallwindows
cv2.destroyAllWindows()

cropped = imgGray[160:260,160:260]
img_rotate_90_clockwise = cv2.rotate(cropped, 0)
img_rotate_90_counterclockwise = cv2.rotate(cropped, cv2.ROTATE_90_COUNTERCLOCKWISE)

# https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#void%20flip(InputArray%20src,%20OutputArray%20dst,%20int%20flipCode)
flipped = cv2.flip(imgColor,-1)
# 0 means flipping around the x-axis 
# 1 means flipping around the y-axis 
# -1(or any negative value) means flipping around both axes
flipped = cv2.flip(flipped,-1)


cv2.imshow('Cropped Image',cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imshow('rotated Image',img_rotate_90_clockwise)
cv2.waitKey(0)
cv2.destroyAllWindows()

distorted = (img_rotate_90_clockwise + img_rotate_90_counterclockwise)/2

brighted = cropped * 1.5
darkened = cropped * 0.5

cv2.imwrite("cropped.jpg", cropped)
cv2.imwrite("rotated.jpg", img_rotate_90_clockwise)
cv2.imwrite("countered_rotated.jpg", img_rotate_90_counterclockwise)
cv2.imwrite("flipped.png", flipped)
cv2.imwrite("averaged.png", distorted)
cv2.imwrite("brighted.png", brighted)
cv2.imwrite("darkened.png", darkened)

