import os

from image_loader import load_image
from noise_generator import add_gaussian_noise, save_noisy_image
from filters import (
    mean_filter,
    median_filter,
    gaussian_filter,
    bilateral_filter
)
from quality_metrics import (
    calculate_mse,
    calculate_psnr,
    calculate_ssim
)
from comparison import create_comparison
from result_saver import save_result


def main():

    input_path = "data/raw/sample.jpg"

    print("\n===== IMAGE NOISE REDUCTION =====\n")

    # Load original image
    original = load_image(input_path)

    if original is None:
        return

    # Add Gaussian noise
    noisy = add_gaussian_noise(original)

    # Save noisy image
    save_noisy_image(noisy, "data/noisy/sample_noisy.jpg")

    # Apply filters
    mean_result = mean_filter(noisy)
    median_result = median_filter(noisy)
    gaussian_result = gaussian_filter(noisy)
    bilateral_result = bilateral_filter(noisy)

    # Store results
    results = {
        "Mean Filter": mean_result,
        "Median Filter": median_result,
        "Gaussian Filter": gaussian_result,
        "Bilateral Filter": bilateral_result
    }

    print("\n===== QUALITY RESULTS =====")

    # Calculate quality metrics
    for name, result in results.items():

        mse = calculate_mse(original, result)
        psnr = calculate_psnr(original, result)
        ssim = calculate_ssim(original, result)

        print("\n" + name)
        print("MSE  :", round(mse, 2))
        print("PSNR :", round(psnr, 2))
        print("SSIM :", round(ssim, 4))

    # Save filtered images
    save_result(mean_result, "mean_filter.jpg")
    save_result(median_result, "median_filter.jpg")
    save_result(gaussian_result, "gaussian_filter.jpg")
    save_result(bilateral_result, "bilateral_filter.jpg")

    # Create comparison image
    create_comparison(
        original,
        noisy,
        results,
        "output/comparison.jpg"
    )

    print("\nProject completed successfully.")
    print("Check the output folder for the results.")


if __name__ == "__main__":
    main()