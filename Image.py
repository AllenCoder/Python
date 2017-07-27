from PIL import Image
im = Image.open("./images/TIM截图20170725165159.png")

# 旋转45度
im.rotate(45).show()

# 灰度显示图像
im2 = Image.open("./images/TIM截图20170725165231.png").convert('L')

# 旋转45度
im2.show()

# RGB显示图像
im2 = Image.open("./images/TIM截图20170725165231.png").convert('RGB')

# 旋转45度
im2.show()