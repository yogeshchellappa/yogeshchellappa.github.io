import cv
import cv2

imageName = (raw_input("Enter the name of the image, with extension: \n")).strip()
image = cv2.imread(imageName)

resizedImage = cv2.resize(image, (1920, 1080))

cv2.imwrite(imageName, resizedImage)

print "Successfully rescaled the image!"
