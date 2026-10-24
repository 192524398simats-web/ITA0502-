
import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("C:/Users/jdhar/OneDrive/Attachments/Desktop/images.jpg", 0)

if img is None:
    print("Image not found!")
else:
    # Apply histogram equalization
    equalized = cv2.equalizeHist(img)

    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    # Display equalized image
    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Equalized Image")
    plt.axis("off")

    plt.show()
