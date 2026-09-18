import numpy as np
from skimage.metrics import structural_similarity


def calculate_mse(original, processed):
    difference = original.astype(float) - processed.astype(float)
    mse = np.mean(difference ** 2)
    return mse


def calculate_psnr(original, processed):
    mse = calculate_mse(original, processed)

    if mse == 0:
        return float("inf")

    psnr = 10 * np.log10((255 ** 2) / mse)
    return psnr


def calculate_ssim(original, processed):
    original_gray = original
    processed_gray = processed

    if len(original.shape) == 3:
        import cv2
        original_gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        processed_gray = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)

    ssim = structural_similarity(original_gray, processed_gray)
    return ssim