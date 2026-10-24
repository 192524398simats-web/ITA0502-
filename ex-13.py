import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    rows, cols = img.shape[:2]

    points1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    points2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    matrix = cv2.getAffineTransform(points1, points2)

    transformed = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformation", transformed)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
