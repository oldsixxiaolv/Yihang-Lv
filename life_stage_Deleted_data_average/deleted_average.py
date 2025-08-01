# -- coding:utf-8 --
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from read_shuju import read_shuju
from read_shuju_xiaoyu_067 import read_shuju_xiaoyu


def feature_normalize(dt):
    average = np.nanmean(dt[np.isfinite(dt)])
    sigma = np.nanstd(dt[np.isfinite(dt)])
    return (dt - average) / sigma


def converge(data, data_add):
    data_mid = []
    for i, j in zip(data, data_add):
        data_mid.append(np.concatenate((i, j)))
    return data_mid


def for_(data, stage):
    mid = []
    for i in data:
        mid.append(i[stage])
    return mid


def duqu_excel_julei(path):
    import pandas as pd
    file_path = path
    df = pd.read_excel(file_path, usecols=[1], names=None)
    dali = df.values.tolist()
    result = []
    for i in dali:
        result.append(i[0])
    return result


plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 12
data_last = read_shuju_xiaoyu()
# stage = duqu_excel_julei(r"C:\Users\lvyih\Desktop\stage.xlsx")
# data_last = for_(data_last, stage)
# stage_2 = duqu_excel_julei(r"C:\Users\lvyih\Desktop\stage_2.xlsx")
# data_last = for_(data_last, stage)
# data_last = for_(data_last, stage_2)
# data_add = read_shuju_ADD()
# data_last = converge(data, data_add)
# r, maxht20, maxht30, maxht40, npixels_20, npixels_30, npixels_40, flash_20, flash_30, flash_40, minir, flashrate
r = data_last[0]
maxht20 = data_last[1]
maxht30 = data_last[2]
maxht40 = data_last[3]
npixels_20 = data_last[4]
npixels_30 = data_last[5]
npixels_40 = data_last[6]
flash_20 = data_last[7]
flash_30 = data_last[8]
flash_40 = data_last[9]
minir = data_last[10]
flashrate = data_last[11]
maxht20_minux_maxht40 = data_last[12]
ellip_20 = data_last[13]
ellip_30 = data_last[14]
ellip_40 = data_last[15]
maxdbz = data_last[16]
maxht = data_last[17]
npx40_divide_npx20 = data_last[18]
npx40_divide_npx30 = data_last[19]
np.set_printoptions(threshold=np.inf)
print(len(ellip_30))
# print(ellip_30)
print(np.mean(ellip_20))
print(np.mean(ellip_30))
print(np.mean(ellip_40))
print(np.mean(maxht40/maxht20))
print(np.mean(npx40_divide_npx20))
print(np.mean(maxht20))
print(np.mean(maxht30))
print(np.mean(maxht40))
print(np.mean(npixels_20))
print(np.mean(npixels_30))
print(np.mean(npixels_40))
print(np.mean(r))
# print(np.mean(maxht30))
# print(np.mean(maxht20))
# print(np.mean(npixels_20))
# print(np.mean(npixels_30))
