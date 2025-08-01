# -- coding:utf-8 --
from sklearn.cluster import KMeans
from sklearn import metrics
from scipy.spatial.distance import cdist
import numpy as np
import matplotlib.pyplot as plt
from read_shuju import read_shuju
from read_shuju_add import read_shuju_ADD


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
data_last = read_shuju()
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
# print(len(viewtime))
# viewtime = viewtime[~np.isnan(npixels40_divide_npixels20)]
# npixels20_R = npixels20_R[~np.isnan(npixels40_divide_npixels20)]
# npixels40_R = npixels40_R[~np.isnan(npixels40_divide_npixels20)]
# npixels40_divide_npixels20 = npixels40_divide_npixels20[~np.isnan(npixels40_divide_npixels20)]
# index1 = list(np.where(viewtime < 190))
# viewtime = viewtime[index1[0]]
# print(len(viewtime))
# npixels20_R = npixels20_R[index1[0]]
# npixels40_R = npixels40_R[index1[0]]
# npixels40_divide_npixels20 = npixels40_divide_npixels20[index1[0]]
r = feature_normalize(r)
maxht40_divide_maxht20 = feature_normalize(maxht40 / maxht20)
maxht20_minus_maxht40_divide_maxht20 = feature_normalize((maxht20-maxht40) / maxht20)
maxht20 = feature_normalize(maxht20)
maxht30 = feature_normalize(maxht30)
maxht40 = feature_normalize(maxht40)
npixels_20 = feature_normalize(npixels_20)
npixels_30 = feature_normalize(npixels_30)
npixels_40 = feature_normalize(npixels_40)
flash_20 = feature_normalize(flash_20)
flash_30 = feature_normalize(flash_30)
flash_40 = feature_normalize(flash_40)
minir = feature_normalize(minir)
flashrate = feature_normalize(flashrate)
maxht20_minux_maxht40 = feature_normalize(maxht20_minux_maxht40)
ellip_20 = feature_normalize(ellip_20)
ellip_30 = feature_normalize(ellip_30)
ellip_40 = feature_normalize(ellip_40)
maxdbz = feature_normalize(maxdbz)
maxht = feature_normalize(maxht)
npx40_divide_npx20 = feature_normalize(npx40_divide_npx20)
npx40_divide_npx30 = feature_normalize(npx40_divide_npx30)
# viewtime = feature_normalize(viewtime)
# print(len(npixels20_R))
# print(len(npixels40_R))
# print(len(npixels40_divide_npixels20))
# print(len(list(zip(npixels20_R, npixels40_R, npixels40_divide_npixels20))))
# print(len(list(zip(npixels20_R, npixels40_R))))
# 就选用flashrate, maxht40, npixels_40, flash_40, flash_20这五个量进行聚类效果是显著的好的
X = np.array(list(zip(ellip_30, maxht40_divide_maxht20, npx40_divide_npx20, maxdbz
                      ))).reshape(len(ellip_30), 4)
# 这里得到的distortion是欧几里得距离
distortions = []
# 这里的inertias是样本到其最近聚类中心的平方距离之和
inertias = []
Silhouette_Coefficient = [np.nan]
CH = [np.nan]
K = range(1, 9)
for k in K:
    kmeanModel = KMeans(n_clusters=k).fit(X)
    distortions.append(sum(np.min(cdist(X, kmeanModel.cluster_centers_, "euclidean"), axis=1)) / X.shape[0])
    inertias.append(kmeanModel.inertia_)
    if k == 1:
        pass
    else:
        # Silhouette_Coefficient.append(round(float(metrics.silhouette_score(X, kmeanModel.labels_,
        #                                                        metric="euclidean")), 2))
        CH.append(round(float(metrics.calinski_harabasz_score(X, kmeanModel.labels_))))
        # print(f"k={k}")
        # print("轮廓系数", metrics.silhouette_score(X, kmeanModel.labels_, metric="euclidean"))
        # print("CH", metrics.calinski_harabasz_score(X, kmeanModel.labels_))
        print("---------------------------------")

fig = plt.figure(1, figsize=(4, 4))
# ax = fig.add_subplot(1, 2, 1)
# ax.set_xlabel("k", fontsize=14)
# ax.set_ylabel("distortions", fontsize=14)
# ax.plot(K, distortions, "bx-")
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_xlabel("k", fontsize=14)
ax1.set_ylabel("inertias", fontsize=14)
ax1.plot(K, inertias, "bx-")
ax2 = ax1.twinx()
print(CH)
ax2.plot(K, CH, "r^-")
ax2.set_ylabel("CH", fontsize=14)
plt.savefig("C:\\Users\\lvyih\\Desktop\\zhoubutu____.jpeg", bbox_inches="tight", dpi=400)

