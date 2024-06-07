import cv2
import numpy as np


class ImageProc:
    @staticmethod
    def salt_paper(img):
        w, h, _ = img.shape
        # noise1 = np.random.randint(0, 10, (w, h), dtype=np.uint8)
        # noise2 = np.random.randint(0, 10, (w, h), dtype=np.uint8)
        # noise3 = np.random.randint(0, 10, (w, h), dtype=np.uint8)
        noises = np.random.normal(0, 0.1, img.shape)
        return img + noises

        # img[:, :, 0] += noise1
        # img[:, :, 1] += noise2
        # img[:, :, 2] += noise3
        return img
