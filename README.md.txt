# Image Noise Reduction Using Different Filters

## 1. Project Description

This project focuses on reducing noise from digital images using different image processing techniques. An original image is taken as input, artificial noise is added to it, and different filters are then applied to reduce the noise.

The project compares Mean, Median, Gaussian, and Bilateral filters. The results are evaluated using MSE, PSNR, and SSIM so that the effect of each filter can be observed.

## 2. Objectives

- To understand image noise and its effect on image quality.
- To add artificial noise to an image.
- To implement different noise reduction filters.
- To compare the output of different filters.
- To evaluate the processed images using image quality metrics.

## 3. Technologies Used

- Python
- OpenCV
- NumPy
- Scikit-Image
- Matplotlib

## 4. Features

- Loads an input image.
- Adds Gaussian noise to the image.
- Applies Mean Filter.
- Applies Median Filter.
- Applies Gaussian Filter.
- Applies Bilateral Filter.
- Calculates MSE, PSNR, and SSIM.
- Saves processed images.
- Creates a comparison image.

## 5. Project Structure

```text
Noise Reduction/
│
├── data/
│   ├── raw/
│   │   └── sample.jpg
│   └── noisy/
│       └── sample_noisy.jpg
│
├── src/
│   ├── main.py
│   ├── image_loader.py
│   ├── noise_generator.py
│   ├── filters.py
│   ├── quality_metrics.py
│   ├── comparison.py
│   └── result_saver.py
│
├── output/
│   ├── mean_filter.jpg
│   ├── median_filter.jpg
│   ├── gaussian_filter.jpg
│   ├── bilateral_filter.jpg
│   └── comparison.jpg
│
├── requirements.txt
├── README.md
├── statement.md
└── .gitignore
6. Requirements

The project requires Python 3 and the following libraries:

NumPy
OpenCV
Scikit-Image
Matplotlib
7. Installation

Open a terminal in the project folder.

Install the required libraries using:

pip install -r requirements.txt
8. How to Run

Place the input image inside:

data/raw/

The input image should be named:

sample.jpg

Run the project using:

python src/main.py

The processed images will be saved in the output folder.

9. Filters Used
Mean Filter

The Mean Filter replaces a pixel with the average value of the pixels in its neighbourhood. It can reduce noise but may also blur image details.

Median Filter

The Median Filter replaces a pixel with the median value of the neighbouring pixels. It is useful for reducing impulse or salt-and-pepper noise.

Gaussian Filter

The Gaussian Filter uses a Gaussian-weighted neighbourhood to smooth the image and reduce noise.

Bilateral Filter

The Bilateral Filter reduces noise while trying to preserve important edges in the image.

10. Evaluation Metrics
MSE

Mean Squared Error measures the average squared difference between the original and processed images.

Lower MSE generally indicates less error.

PSNR

Peak Signal-to-Noise Ratio is used to measure the quality of the processed image.

A higher PSNR generally indicates better image quality.

SSIM

Structural Similarity Index compares structural information between two images.

A value closer to 1 indicates greater structural similarity.

11. Output

After running the program, the following results are generated:

Noisy image
Mean filtered image
Median filtered image
Gaussian filtered image
Bilateral filtered image
Combined comparison image

The comparison image allows the results of the different filters to be viewed together.

12. Conclusion

This project demonstrates how different image filtering techniques can be used to reduce noise from digital images. The project also shows how image quality can be measured using MSE, PSNR, and SSIM.

The comparison of different filters helps in understanding that different filtering methods can produce different results depending on the type and amount of noise present in an image.

13. Future Scope

The project can be extended by:

Supporting more types of image noise.
Adding additional filtering techniques.
Processing multiple images automatically.
Adding a graphical interface.
Comparing results for different noise levels.
Generating detailed result reports.
14. Author

Saksham Gupta
B.Tech CSE (AIML)
VIT Bhopal University