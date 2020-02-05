import os
from os import path
import PIL.ImageOps
import imageio
import tensorflow
from PIL import Image


def mkdir_anyway(path: str) -> None:
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


# Create a nice folder structure for saving all images
mkdir_anyway("train")
for number in range(10):
    mkdir_anyway(path.join("train", str(number)))
mkdir_anyway("test")
for number in range(10):
    mkdir_anyway(path.join("test", str(number)))

# load the handwriting data
handwriting = tensorflow.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = handwriting.load_data()


def save_images(destination: str, imagedata: list, classifications: list):
    count_per_image = [0] * 10
    for i in range(len(imagedata)):
        image = imagedata[i]
        number = classifications[i]
        # Invert the image, so it's more natural black on white
        image = Image.fromarray(image)
        image = PIL.ImageOps.invert(image)
        # Save the PNG
        count_per_image[number] += 1
        filename = path.join(destination, str(number), str(count_per_image[number])) + ".png"
        imageio.imwrite(filename, image)


save_images("train", x_train, y_train)
save_images("test", x_test, y_test)
