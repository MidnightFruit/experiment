import cv2
import numpy as np
import random


class ImageProc:
    @staticmethod
    def salt_paper(img, percent_to_brake):
        row, col, _ = img.shape
        pixels_for_each_color = int(row * col * percent_to_brake / 2)
        number_of_pixels = random.randint(pixels_for_each_color, pixels_for_each_color)

        for i in range(number_of_pixels):
            y_coord = random.randint(0, row - 1)
            x_coord = random.randint(0, col - 1)
            img[y_coord][x_coord] = 255

        number_of_pixels = random.randint(pixels_for_each_color, pixels_for_each_color)
        for i in range(number_of_pixels):
            y_coord = random.randint(0, row - 1)
            x_coord = random.randint(0, col - 1)
            img[y_coord][x_coord] = 0

        return img

    @staticmethod
    def distort_image(img):
        rows, cols, _ = img.shape
        distCoeff = np.zeros((4, 1), np.float64)
        k1 = -5.0e-5
        k2 = 0.0
        p1 = 0.0
        p2 = 0.0
        cam = np.eye(3, dtype=np.float32)
        cam[0, 2] = cols / 2.0
        cam[1, 2] = rows / 2.0
        cam[0, 0] = 10.
        cam[1, 1] = 10.

        distCoeff[0, 0] = k1
        distCoeff[1, 0] = k2
        distCoeff[2, 0] = p1
        distCoeff[3, 0] = p2
        distortion = np.float32([[1, 0, 0],
                                 [0, 1, 0],
                                 [0.0015, 0.0015, 1]])
        # result = cv2.warpPerspective(img, distortion, (rows, cols))
        result = cv2.undistort(img, cam, distCoeff)
        return result

