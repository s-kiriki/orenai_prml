# coding: UTF-8
# # 1次元のWidrow-Hoffの学習規則の実装例
import numpy as np
import matplotlib.pyplot as plt
from widrow_hoff import get_wvec

import sys

if __name__ == '__main__':
    
    #homework02
    #data = np.array([[1.0, 1],[0.5, 1],[-0.2, 2],[-1.3, 2]])#データ群
    #homework03
    data = np.array([[1.0, 1],[0.5, 1],[-0.2, 2],[-0.4, 1],[-1.3, 2],[-2.0, 2]])#データ群
    
    features = data[:,0].reshape(data[:,0].size,1)#特徴ベクトル
    labels = data[:,1]#クラス（今回はc1=1,c2=2）
    wvec = np.array([0.2, 0.3])#初期の重みベクトル
    xvecs = np.c_[np.ones(features.size), features]#xvec[0] = 1
    
    #クラス1について
    tvec1 = labels.copy()#クラス1の教師ベクトル
    tvec1[labels == 1] = 1
    tvec1[labels == 2] = 0
    
    wvec1 = get_wvec(xvecs, wvec, tvec1)
    print "wvec1 = %s" % wvec1
    print "g1(x) = %f x + %f" % (wvec1[1], wvec1[0])
    
    for xvec,label in zip(xvecs,labels):
        print "g1(%s) = %s (クラス:%s)" % (xvec[1],np.dot(wvec1, xvec), label)    
    
    #クラス2について
    tvec2 = labels.copy()#クラス2の教師ベクトル
    tvec2[labels == 1] = 0
    tvec2[labels == 2] = 1
    
    wvec2 = get_wvec(xvecs, wvec, tvec2)
    print "wvec2 = %s" % wvec2
    print "g2(x) = %f x + %f" % (wvec2[1], wvec2[0])
    
    for xvec,label in zip(xvecs,labels):
        print "g2(%s) = %s (クラス:%s)" % (xvec[1],np.dot(wvec, xvec), label)     
