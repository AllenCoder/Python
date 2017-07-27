# 想把一幅图像转为np.array表示
from PIL import Image
import numpy as np

im = np.array(Image.open('./images/TIM截图20170725165159.png'))
print(im.shape, im.dtype)

# 表示图像数据918行，1556列，颜色通道数4，以uint8类型存储
im_1 = np.array(Image.open('./images/TIM截图20170725165159.png').convert('L'))

print(im_1.shape, im.dtype)  # 灰度图像没有颜色通道信息
