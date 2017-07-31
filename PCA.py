from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pim = Image.open('./images/2638385516-56385ba771f51.png').crop((110, 360, 460, 675)).resize((256, 230)).convert(
    'L')  # 二维黑白页面
im = np.array(pim)
n, m = im.shape[0:2]  # 从索引第0个开始，取两个
points = []

for i in range(n):
    for j in range(m):
        if im[i, j] < 128:  # 把小于128的灰度值作为黑点取出来
            points.append([float(j), float(n) - float(i)])  # 坐标转换一下
    im_x = np.mat(points).T
print('im_X=', im_x, 'shape=', im_x.shape)


# X
def pca(X, k=1):  # 降为K维
    d, n = X.shape
    mean_x = np.mean(X, axis=1)  # axis 为0表示计算每列的均值，为1表示计算每行的均值
    print('mean_X=', mean_x)
    X = X - mean_x
    C = np.dot(X, X.T)
    e, EV = np.linalg.eig(np.mat(C))  # 求协方差的特征值和特征向量
    print('C=', C)
    print('e=', e)
    print('EV=', EV)
    e_idx = np.argsort(-e)[:k]
    EV_main = EV[:, e_idx]  # 获取特征值 对应的特征向量，作为主成分
    print('e_idx=', e_idx, 'EV_main=', EV_main)
    low_X = np.dot(EV_main.T, X)
    return low_X, EV_main, mean_x


low_X, EV_main, mean_x = pca(im_x)

print('low_X=', low_X)
print('EV_main=', EV_main)
recon_X = np.dot(EV_main, low_X) + mean_x

print('recon_X.shape=', recon_X.shape)

fig = plt.figure()
ax = fig.add_subplot(111) # 第一行第一列第一个
ax.scatter(im_x[0].A[0], im_x[1].A[0], s=1, alpha=0.5)
ax.scatter(recon_X[0].A[0], recon_X[1].A[0], marker='o', s=100, c='blue', edgecolors='white')

# x :数组，样本点在x轴上坐标集
# y :数组，样本点在y轴坐标集
# s :表示画出来的点的缩放大小
# c 表示画出来的点内部颜色
# edgecolors :表示小圆圈边缘颜色
plt.show()
