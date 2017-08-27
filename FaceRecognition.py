import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# 获取当前路径下所有图像文件
def getFacePath(datapath):
    path = []
    for dir in os.listdir(datapath):
        print(dir)
        try:
            for filename in os.listdir(os.path.join(datapath, dir)):
                path.append(os.path.join(datapath, dir, filename))
        except:
            pass
    return path


imgpaths = getFacePath('./orl_faces')
m, n = np.array(Image.open(imgpaths[0])).shape[0:2]  # 图片分辨率
X = np.mat([np.array(Image.open(impath)).flatten() for impath in imgpaths]).T


def pca(X):
    dim, num_data = X.shape  # dim :维数，num_data:样本数

    mean_X = X.mean(axis=1)
    X = X - mean_X
    M = np.dot(X.T, X)
    e, EV = np.linalg.eigh(M)
    print("e=", e.shape, e)
    print('EV=', EV.shape, EV)
    tmp = np.dot(X, EV).T
    print('tmp=', tmp.shape, tmp)
    V = tmp[::-1]
    print("V =", V.shape, V)

    for i in range(EV.shape[1]):
        V[:, 1] /= np.linalg.norm(EV[:, i])
    return V, EV, mean_X


V, EV, immean = pca(X)

plt.gray()

plt.subplot(2, 4, 1)
plt.imshow(immean.reshape(m, n))

for i in range(7):
    plt.subplot(2, 4, i + 2)
    plt.imshow(V[i].reshape(m, n))
plt.show()


def pca_book(X):
    num_data, dim = X.shape  # 注意：这里的行为样本数，列为维
    mean_X = X.mean(axis=0)  # 注意：axis =0 表示计算每列（维） 均值，结果为行向量
    M = np.dot(X, X.T)
    e, EV = np.linalg.eigh(M)
    tmp = np.dot(X.T, EV).T
    V = tmp[::-1]


# W = EV[:, k]
# projections = []
#
# for xi in X.T:
#     projections.append(np.dot(W.T, xi - mean_X))
#
#
# def euclidean_distance(p, q):
#     p = np.array(p).flatten()
#     q = np.array(q).flatten()
#     return np.sqrt(np.sum(np.power((p-q),2)))
#
# minDist = np.finfo('float').max
# Q = np.dot(W.T,D -mean_X)
# for i in xrange(len(projections)):
#     dist = euclidean_distance(projections[i],Q)



