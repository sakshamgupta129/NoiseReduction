import cv2


def load_image(path):
    image = cv2.imread(path)

    if image is None:
        print("Error: Image could not be loaded.")
        return None

    print("Image loaded successfully.")
    return image