import cv2
import numpy as np
import random


class ImageProc:
    @staticmethod
    def salt_paper(img, lower, upper):
        row, col, _ = img.shape
        number_of_pixels = random.randint(lower, upper)

        for i in range(number_of_pixels):
            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to white
            img[y_coord][x_coord] = 255

        number_of_pixels = random.randint(lower, upper)
        for i in range(number_of_pixels):
            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to black
            img[y_coord][x_coord] = 0

        return img
