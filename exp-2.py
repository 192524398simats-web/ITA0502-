
import cv2

# Read the image
img = cv2.imread("image.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (15, 15), 0)

# Display original and blurred images
cv2.imshow("Original Image", img)
cv2.imshow("Gaussian Blur Image", blur)

# Close windows
cv2.waitKey(0)
cv2.destroyAllWindows()
