import cv2
import os


def save_result(image, filename):
    output_folder = "output"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    path = os.path.join(output_folder, filename)

    cv2.imwrite(path, image)

    print("Saved:", path)