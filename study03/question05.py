# coding: UTF-8
import numpy as np
import matplotlib.pyplot as plt

def train(wvec, xvec, is_c1):
    low = 0.5#学習係数
    if (np.dot(wvec,xvec) > 0) != is_c1:
        if is_c1:
            wvec_new = wvec + low*xvec
        else:
            wvec_new = wvec - low*xvec
        return wvec_new
    else:
        return wvec

if __name__ == '__main__':
    
    data = np.array([[1.0, 1],[0.5, 1],[-0.2, 2],[-1.3, 2]])#データ群
    
    features = data[:,0].reshape(data[:,0].size,1)#特徴ベクトル
    labels = data[:,1]#クラス（今回はc1=1,c2=2）
    wvec = np.array([0.2, 0.3])#初期の重みベクトル
    is_c1s = (labels == 1)#c1かどうか booleanの配列
    
    xvecs = np.c_[np.ones(features.size), features]#xvec[0] = 1
    
    loop = 100
    for j in range(loop):
        for xvec, is_c1 in zip(xvecs, is_c1s):
            wvec = train(wvec, xvec, is_c1)
    
    print wvec
    print -(wvec[0]/wvec[1])
    
    plt.axhline(y=0, c='gray')
    plt.scatter(features[is_c1s], np.zeros(features[is_c1s].size), c='red', marker="o")
    plt.scatter(features[~is_c1s], np.zeros(features[~is_c1s].size), c='yellow', marker="o")
    #分離境界線
    plt.axvline(x=-(wvec[0]/wvec[1]), c='green')    
    plt.show()

