#convert rgb to gray
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray

def load_data(dir = 'source'):
    img2 = []
    for filename in os.listdir(dir):
        if os.path.isfile(dir + '/' + filename):
            img = mpimg.imread(dir + '/' + filename)
            img = rgb2gray(img)
            img2.append(img)
    return img2

def show_img(imgs, format=None, gray=False):
    plt.figure(figsize=(20, 40))
    for i, img in enumerate(imgs):
        if img.shape[0] == 3:
            img = img.transpose(1, 2, 0)
        plt_idx = i + 1
        plt.subplot(2, 2, plt_idx)
        plt.imshow(img, format)
    plt.show()