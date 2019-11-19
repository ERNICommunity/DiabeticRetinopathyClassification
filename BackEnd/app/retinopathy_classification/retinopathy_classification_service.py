# -*- coding: utf-8 -*-
from werkzeug.utils import secure_filename
from os import path

import cv2
import numpy as np


def save_file(file, folder_path):
    filename = secure_filename(file.filename)
    filepath = path.join(
            folder_path,
            'static',
            'images',
            filename)
    file.save(filepath)

    return filepath


def scaleRadius(img, scale):
    x = img[int(img.shape[0]/2), :, :].sum(1)
    r = (x > x.mean() / 10).sum() / 2
    s = scale * 1.0 / r
    return cv2.resize(img, (0, 0), fx=s, fy=s)


def process_image(img_path, scale):
    img = cv2.imread(img_path)

    img = scaleRadius(img, scale)

    img = cv2.addWeighted(
            img, 4, cv2.GaussianBlur(img, (0, 0), scale / 30), -4, 128)

    overlay = np.zeros(img.shape)

    cv2.circle(overlay,
               (int(img.shape[1]/2), int(img.shape[0]/2)), int(scale * 0.9), (1, 1, 1), -1, 8, 0)

    img = img * overlay + 128 * (1 - overlay)

    print("Path: " + path.join(img_path))
    cv2.imwrite(img_path, img)

    return img
