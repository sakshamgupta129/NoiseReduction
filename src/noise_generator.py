import cv2
import numpy as np


def add_gaussian_noise(image):
    noise = np.random.normal(0, 25, image.shape)
    noisy_image = image.astype(np.float32) + noise

    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = noisy_image.astype(np.uint8)

    return noisy_image


def add_salt_pepper_noise(image):
    noisy_image = image.copy()

    probability = 0.02

    random_values = np.random.random(image.shape[:2])

    noisy_image[random_values < probability / 2] = 0
    noisy_image[random_values > 1 - probability / 2] = 255

    return noisy_image


def save_noisy_image(image, path):
    cv2.imwrite(path, image)
    print("Noisy image saved successfully.")