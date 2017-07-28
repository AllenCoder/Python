# 直方图

import numpy as np
from PIL import Image

import matplotlib.pyplot as plt

#  转换图像，图像的矩阵
def histeq(im, nbr_bins=256):
    imhist, bins = np.histogram(im.flatten(), nbr_bins, density=True)  # 对每个元素求概率密度
    cdf = imhist.cumsum()  # 对概率密度数组求累计和
    cdf = 255 * cdf / cdf[-1]  #累积和变换到0-255区间
    im2 = np.interp(im.flatten(), bins[:-1], cdf) #线性插值
    return im2.reshape(im.shape), cdf  #还原图像维度

#    L = R * 299/1000 + G * 587/1000 + B * 114/1000
im = np.array(Image.open('./images/TIM截图20170725165159.png').convert('L')) # 得到灰度图像
im2, cdf = histeq(im)

plt.gray()

plt.subplot(221) #2行2列，第1个图
plt.imshow(im)
plt.subplot(222) #2行2列，第2个图
plt.hist([x for x in im.flatten() if x < 250], 256)
plt.subplot(223)
plt.imshow(im2)
plt.subplot(224)
plt.hist([x for x in im2.flatten() if x < 250], 256)
plt.show()
