"""
FILE_NAME: Image_utils.py
AUTHOR: RCB
CREATED: 2024-04-28-16:04
DESC: 图片文件工具，用于读取和保存图片文件
"""
import os

import numpy as np

os.environ['OPENCV_IO_ENABLE_OPENEXR'] = '1'
import numpy
import matplotlib.image as mping
import matplotlib.pyplot as plt
import cv2


def img_util_show_img(imgs: [numpy.ndarray]):
    i = 0
    for img in imgs:
        plt.figure(i)
        plt.imshow(img)
        i += 1
    plt.show()

def img_util_read_img(file_path: str) -> numpy.ndarray:
    print("OpenImageAt: " + file_path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        if file_path.endswith('.hdr') or file_path.endswith('.exr'):
            img = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
            _, _, cn = img.shape
            img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
            return img
        else:
            img = mping.imread(file_path)
            if len(img.shape) == 2:
                img = numpy.stack((img,img,img,img), axis=2)
                
            return img

    else:
        raise Exception("图片文件路径错误" + file_path)


def img_util_save_img(file_path: str, img: numpy.ndarray):
    if file_path.endswith('.hdr'):
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
        cv2.imwrite(file_path, img)
    elif file_path.endswith('.exr'):
        img = img_util_to_float32(img)
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA)
        cv2.imwrite(file_path, img)
    else:
        img = img_util_to_uint8(img)
        mping.imsave(file_path, img)


def img_util_to_float32(data):
    dt = data.dtype
    if dt == 'float32':
        return data
    if dt == 'uint8':
        data = numpy.asarray(data, 'float32')
        data /= 255.0
        return data
    raise Exception("to_float32 cannot handle type" + str(dt))


def img_util_to_uint8(data):
    dt = data.dtype
    if dt == 'uint8':
        return data
    if dt == 'float32':
        data *= 255.0
        data = data.clip(min=0, max=255)
        data = numpy.asarray(data, 'uint8')
        return data
    raise Exception("to_uint8 cannot handle type" + str(dt))
