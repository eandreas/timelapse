# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['openImageCV2', 'plotCV2', 'putText', 'getDateTimePictureTaken']

# Cell
import cv2
from pathlib2 import Path
from matplotlib import pyplot as plt
from exif import Image
from datetime import datetime

# Cell
def openImageCV2(path):
    '''Returns a cv2-image read based on a pathlib2-Path variable'''
    return cv2.imread(path.as_posix())

# Cell
def plotCV2(img):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

# Cell
def putText(img, text, x, y, fontSize, thickness, bgrColor):
    return cv2.putText(
        img,  text, (x,y),
        cv2.FONT_HERSHEY_SIMPLEX, fontSize,
        bgrColor, thickness, cv2.LINE_AA)

# Cell
def getDateTimePictureTaken(path):
    ds = Image(path).get("datetime_original")
    return datetime.strptime(ds, '%Y:%m:%d %H:%M:%S')