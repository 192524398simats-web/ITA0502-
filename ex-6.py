
import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display original and eroded images
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(eroded, cmap="gray")
    plt.title("Eroded Image")
    plt.axis("off")

    plt.show()
