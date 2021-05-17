# First, install below packages
# pip install scipy
#
# pip install shutil
#
# pip install os
#
# pip install nibabel
#
# pip install numpy


import os
import numpy as np
from nibabel.testing import data_path
import nibabel as nib
import matplotlib.pylab as plt
import time


def nii2png(nii_directory):
    example_filename = os.path.join(data_path, nii_directory)
    img = nib.load(example_filename)
    data = np.array(img.get_fdata())
    data = np.moveaxis(data, -1, 0)
    print("shape:", data.shape)
    return data


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
    plt.close()


dir = input("Enter the .nii file path: e.g. C:/Users/Name/nii2png/file.nii \n")
out_dir = input("Enter the output path: e.g. C:/Users/Name/nii2png/output.png \n")
start_time = time.time()
data = nii2png(dir)
draw(data, out_dir)
print(f'Conversion is done in {time.time() - start_time} secs.')
