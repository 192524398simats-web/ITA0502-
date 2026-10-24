
import cv2
import matplotlib.pyplot as plt

def analyze_histogram(filename):
    img = cv2.imread(filename)

    if img is None:
        print("Image not found!")
        return

    colors = ("b", "g", "r")
    names = ("Blue", "Green", "Red")

    for color, name in zip(colors, names):
        hist = cv2.calcHist(
            [img], [colors.index(color)], None, [256], [0, 256]
        )
        plt.plot(hist, color=color, label=name)

    plt.title("Color Histogram")
    plt.xlabel("Pixel Intensity")
    plt.ylabel("Number of Pixels")
    plt.legend()
    plt.show()

analyze_histogram("image.jpg")
