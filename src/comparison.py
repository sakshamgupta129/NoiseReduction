import cv2
import matplotlib.pyplot as plt


def create_comparison(original, noisy, results, output_path):

    images = [original, noisy]
    titles = ["Original Image", "Noisy Image"]

    for name, image in results.items():
        images.append(image)
        titles.append(name)

    plt.figure(figsize=(15, 8))

    for i in range(len(images)):
        plt.subplot(2, 3, i + 1)

        image = images[i]

        if len(image.shape) == 3:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        plt.imshow(image)
        plt.title(titles[i])
        plt.axis("off")

    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    print("Comparison image saved successfully.")