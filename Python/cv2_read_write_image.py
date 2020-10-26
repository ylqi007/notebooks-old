#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Time    : 10/24/20 3:28 PM
# Author  : Shark
# Site    : 
# File    : cv2_read_write_image.py
# Software: PyCharm
# ===========================================================
import cv2
import numpy as np


def read_and_write_image():
    img = cv2.imread('images/Lenna.png')    # BGR
    print("Return type of cv2.imread(): ", type(img))   # <class 'numpy.ndarray'>
    print("img shape: ", img.shape)     # (512, 512, 3)
    print("img data type: ", img.dtype) # uint8
    print(np.min(img), np.max(img))     # 3 255
    cv2.imshow("test", img)
    blue = np.copy(img)
    green = np.copy(img)
    red = np.copy(img)

    blue[:, :, [1, 2]] = 0
    cv2.imshow("Only blue channel", blue)

    green[:, :, [0, 2]] = 0
    cv2.imshow("Only green channel", green)

    red[:, :, [0, 1]] = 0
    cv2.imshow("Only red channel", red)

    one_channel = img[:, :, 0]
    print(type(one_channel), one_channel.shape)
    cv2.imshow("Only one channel - blue", one_channel)
    while cv2.waitKey(100) != 27:
        if cv2.getWindowProperty("test", cv2.WND_PROP_VISIBLE) <= 0:
            break
    cv2.destroyAllWindows()

    cv2.imwrite("images/blue_lenna.jpg", blue)
    cv2.imwrite("images/green_lenna.jpg", green)
    cv2.imwrite("images/res_lenna.jpg", red)
    cv2.imwrite("images/one_channel_lenna.jpg", one_channel)
    one_channel = cv2.imread("images/one_channel_lenna.jpg")
    print(type(one_channel), one_channel.shape)

    img_f = img.astype(np.float32)
    print(type(img_f))
    print(img_f.shape)
    print(np.min(img_f), np.max(img_f))



if __name__ == '__main__':
    read_and_write_image()