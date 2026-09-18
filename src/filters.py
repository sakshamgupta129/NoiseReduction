import cv2


def mean_filter(image):
    return cv2.blur(image, (5, 5))


def median_filter(image):
    return cv2.medianBlur(image, 5)


def gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


def bilateral_filter(image):
    return cv2.bilateralFilter(image, 9, 75, 75)