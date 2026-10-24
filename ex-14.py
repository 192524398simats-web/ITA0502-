import cv2
import numpy as np

img = cv2.imread("C:/Users/jdhar/Downloads/Vibrant Pink Gerbera Amidst Greenery.png")

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape[:2]

    points1 = np.float32([
        [0, 0],
        [cols - 1, 0],
        [0, rows - 1],
        [cols - 1, rows - 1]
    ])

    points2 = np.float32([
        [50, 50],
        [cols - 50, 0],
        [0, rows - 50],
        [cols - 1, rows - 1]
    ])

    matrix = cv2.getPerspectiveTransform(points1, points2)

    transformed = cv2.warpPerspective(img, matrix, (cols, rows))

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
