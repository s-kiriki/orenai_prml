# coding: UTF-8
#Widrow-Hoffの学習規則の学習ロジック

import numpy as np

#重み係数の学習
def train(wvec, xvecs, tvec):
    low = 0.2#学習係数
    for key, w in zip(range(wvec.size), wvec):
        sum = 0
        for xvec, b in zip(xvecs, tvec):
            wx = np.dot(wvec,xvec)
            sum += (wx - b)*xvec[key]
        wvec[key] = wvec[key] - low*sum
    return wvec

#重み係数を求める
def get_wvec(xvecs, wvec, tvec):
    loop = 100
    for j in range(loop):
        wvec = train(wvec, xvecs, tvec)
    return wvec
