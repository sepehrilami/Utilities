import numpy as np
import matplotlib.pyplot as plt
import os, glob
import pydicom
import pylibjpeg
import pylab as pl
import sys
import matplotlib.path as mplPath


def draw(images, name, columns=4):
    rows = int(np.ceil(images.shape[0] / columns))
    max_size = 20

    width = min(columns * 5, max_size)
    height = width * rows // columns

    plt.figure(figsize=(width, height))
    plt.gray()
    plt.subplots_adjust(0, 0, 1, 1, 0.01, 0.01)
    for i in range(images.shape[0]):
        plt.subplot(rows, columns, i + 1), plt.imshow(images[i]), plt.axis('off')
    plt.savefig(name)
    print("file saved at", name)



from pathlib import Path
data = Path("E:/WindowsBackup/Desktop/ct/abnormal/")

import os
subdirs = [x[0] for x in os.walk(data)]
print(len(subdirs))
print("Done")

for directory in subdirs:
    plots = []
    empty = True
    print(directory)
    for f in glob.glob(directory + "/*.dcm"):
        empty = False
        f = str(f)
        filename = f.split("/")[-1]
        ds = pydicom.dcmread(filename)
        try:
            pix = ds.pixel_array
            pix = pix*1+(-1024)
            plots.append(pix)
        except:
            empty = True
            continue
    if not empty:
        draw(np.array(plots), str(directory))





