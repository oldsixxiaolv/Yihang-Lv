# -- coding:utf-8 --
from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
from read_shuju_add import read_shuju_ADD
import math


def duqu_excel():
    import pandas as pd
    file_path = r'E:\\Programing\\school_creation_python311\\' \
                'xiaochuang\\2024_thesis\\Excel_and_data_tropical_newest_no_executable\\' \
                'duqu_last.xlsx'
    df = pd.read_excel(file_path, usecols=[1], names=None)
    dali = df.values.tolist()
    result = []
    for i in dali:
        result.append(i[0])
    return result


def npixels_size(npixels, boost):
    boost_former = 4.3 * 4.3
    boost_latter = 5 * 5
    npixel = list(npixels)
    pixel = []
    boost = list(boost)
    t = zip(boost, npixel)
    # 记住以下我们以后要是碰到需要利用两个列表同时遍历的情况，一定要使用zip
    for i, j in t:
        if i == 1:
            mid = j * boost_latter
            pixel.append(mid)
        else:
            mid = j * boost_former
            pixel.append(mid)
    return np.array(pixel)


"""读取数据"""


def read_shuju():
    filepath = r'E:\\Programing\\school_creation_python311\\' \
               'xiaochuang\\2024_thesis\\Excel_and_data_tropical_newest_no_executable\\' \
               'TRMM_tropical_convection_dataset.hdf'
    data = SD(filepath, SDC.READ)
    longitude = list(data.select("longitude")[:])
    latitude = list(data.select("latitude")[:])
    landocean = list(data.select("landocean")[:])
    longitude = np.array(list(map(int, longitude)))
    latitude = np.array(list(map(int, latitude)))
    landocean = np.array(list(map(int, landocean)))
    flashcount = data.select('flashcount')[:]
    flashcount = np.array(list(map(int, flashcount)))
    maxht20 = data.select("maxht20")[:]
    maxht20 = np.array(list(map(int, maxht20)))
    volrain = data.select('volrain')[:]
    rainconv = data.select('rainconv')[:]
    npixels_20 = data.select("npixels_20")[:]
    npixels_40 = data.select("npixels_40")[:]
    viewtime = data.select("viewtime")[:]
    maxht40 = data.select("maxht40")[:]
    maxht40 = np.array(list(map(int, maxht40)))
    # boost = data.select("boost")[:]
    # npixels_40 = data.select("npixels_40")[:]
    # npixels_40_area = npixels_size(npixels_40, boost)
    r = np.divide(rainconv, volrain)
    # 筛选数据
    index1 = np.where(longitude > -20)
    index2 = list(np.where(latitude > -20))
    index3 = list(np.where(landocean == 1))
    index4 = list(np.where(longitude < 50))
    index5 = list(np.where(latitude < 20))
    # 把没有闪电数据的但是有maxht40的和没有maxht40但有闪电数据的去除
    # index6 = list(np.where(flashcount != 0))
    index6 = list(np.where(npixels_40 != 0))
    index7 = list(np.where(maxht40 != 0))
    index8 = list(np.where(flashcount != 0))
    # index8 = list(np.where(npixels_20 > 0))
    # index9 = list(np.where(r > 0))
    # index10 = list(np.where(r < 1))
    index11 = list(np.where(maxht20 != 0))
    index12 = list(np.where(npixels_20 != 0))
    index13 = list(np.where(~np.isnan(viewtime)))
    # 两个数组取交集
    index = list(set(index1[0]) & set(index2[0]) & set(index3[0]) & set(index4[0]) &
                 set(index5[0]) & set(index6[0]) & set(index7[0]) & set(index8[0]) &
                 set(index11[0]) & set(index12[0]) & set(index13[0]))
    index = sorted(index)
    indexw = duqu_excel()
    r = r[index]
    r = r[indexw]
    # 把hdf文件中的闪电频数数据提取出来
    flashcount = data.select('flashcount')[:]
    flashcount = flashcount[index]
    flashcount = flashcount[indexw]
    # 把hdf文件中总的降水数据提取出来
    volrain = data.select('volrain')[:]
    volrain = volrain[index]
    volrain = volrain[indexw]
    # 把hdf文件中的层云降水数据提取出来
    rainstrat = data.select('rainstrat')[:]
    rainstrat = rainstrat[index]
    rainstrat = rainstrat[indexw]
    # 把hdf文件中的对流降水数据分离出
    rainconv = data.select('rainconv')[:]
    rainconv = rainconv[index]
    rainconv = rainconv[indexw]
    # 把hdf文件中的观测时间数据提取出来
    viewtime = data.select('viewtime')[:]
    viewtime = viewtime[index]
    viewtime = viewtime[indexw]
    # 把hdf文件是否升轨数据提取出来
    boost = data.select("boost")[:]
    boost = boost[index]
    boost = boost[indexw]
    # 把hdf文件的最大顶高数据提取出来（这个数据老师说第一个maxht不用操作）
    maxht = data.select("maxht")[:]
    maxht = maxht[index]
    maxht = maxht[indexw]
    maxht20 = data.select("maxht20")[:]
    maxht20 = maxht20[index]
    maxht20 = maxht20[indexw]
    maxht30 = data .select("maxht30")[:]
    maxht30 = maxht30[index]
    maxht30 = maxht30[indexw]
    maxht40 = data.select("maxht40")[:]
    maxht40 = maxht40[index]
    maxht40 = maxht40[indexw]
    # 这个是云的顶层的亮温，可以通过知晓这个温度的高低来判断云顶的高度，温度越低意味着云越高
    minir = data.select("minir")[:]
    minir = minir[index]
    minir = minir[indexw]
    # 这个先不用
    npixels_40 = data.select("npixels_40")[:]
    npixels_40 = npixels_40[index]
    npixels_40 = npixels_40[indexw]
    npixels_40 = npixels_size(npixels_40, boost)
    npixels_20 = data.select("npixels_20")[:]
    npixels_20 = npixels_20[index]
    npixels_20 = npixels_20[indexw]
    npixels_20 = npixels_size(npixels_20, boost)
    npixels_30 = data.select("npixels_30")[:]
    npixels_30 = npixels_30[index]
    npixels_30 = npixels_30[indexw]
    npixels_30 = npixels_size(npixels_30, boost)
    maxnsrain = data.select("maxnsrain")[:]
    maxnsrain = maxnsrain[index]
    maxnsrain = maxnsrain[indexw]
    flashcount = flashcount.astype(float)
    flashrate = np.divide(flashcount, viewtime)
    flashrate = np.multiply(flashrate, 60)
    n20 = data.select("n20dbz")[:]
    n20 = n20[index]
    n20 = n20[indexw]
    n40 = data.select("n40dbz")[:]
    n40 = n40[index]
    n40 = n40[indexw]
    mdbz = data.select("mdbz")[:]
    mdbz = mdbz[index]
    mdbz = mdbz[indexw]
    r = np.divide(rainconv, volrain)
    inde = list(np.where(r > 0.67))
    index_add1 = list(np.where(minir > 0))
    inded = list(set(inde[0]) & set(index_add1[0]))
    inded = sorted(inded)
    n20 = n20[inded]
    n40 = n40[inded]
    mdbz = mdbz[inded]
    boost = boost[inded]
    r = r[inded]
    return n20, n40, mdbz, r, boost


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


def chuli_mianji(n, boost):
    n_yes = []
    for i, j in zip(n, boost):
        if j == 1:
            n_yes.append(i * 5 * 5)
        else:
            n_yes.append(i * 4.3 * 4.3)
    return n_yes


"""程序开始"""
# 程序发起点
plt.rc('axes', linewidth=3)
plt.tick_params(width=3)
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 40
name = ['FlRate (fl' + r'$\cdot$' + r'min$^{-1}$)',
        "Maxht20 (km)", "Maxht30 (km)", "Maxht40 (km)", "Area20 (km$^{2}$)",
        "Area30 (km$^{2}$)", "Area40 (km$^{2}$)"]
data = read_shuju()
# data_add = read_shuju_ADD()
# data_mid = []
# for i, j in zip(data, data_add):
#     data_mid.append(np.concatenate((i, j)))
# data = data_mid
# stage = duqu_excel_julei(r"C:\Users\lvyih\Desktop\stage.xlsx")
file_stage1_path = r'E:\\Programing\\school_creation_python311\\' \
                          'xiaochuang\\2024_thesis\\Excel_and_data_tropical_newest_no_executable\\' \
                          'stage1.xlsx'
stage1 = duqu_excel_julei(file_stage1_path)
file_stage2_path = r'E:\\Programing\\school_creation_python311\\' \
                          'xiaochuang\\2024_thesis\\Excel_and_data_tropical_newest_no_executable\\' \
                          'stage2.xlsx'
stage2 = duqu_excel_julei(file_stage2_path)
file_stage3_path = r'E:\\Programing\\school_creation_python311\\' \
                          'xiaochuang\\2024_thesis\\Excel_and_data_tropical_newest_no_executable\\' \
                          'stage3.xlsx'
stage3 = duqu_excel_julei(file_stage3_path)
# data_all = for_(data, stage)
data1 = for_(data, stage1)
data2 = for_(data, stage2)
data3 = for_(data, stage3)
name_data = [data, data1, data2, data3]
stage = ["All", "Development", "Maturity", "Dissipation"]
Height = np.arange(0, 20, 1.25)
n40_all = np.mean(chuli_mianji(data[1], data[4]), axis=0)
n40_develop = np.mean(chuli_mianji(data1[1], data1[4]), axis=0)
n40_mature = np.mean(chuli_mianji(data2[1], data2[4]), axis=0)
n40_dissi = np.mean(chuli_mianji(data3[1], data3[4]), axis=0)
# np.set_printoptions(threshold=np.inf)
fig = plt.figure(figsize=(10, 15))
ax = fig.add_subplot(1, 1, 1)
ax.plot(n40_all, Height, "black", marker="*",
        label="All", linewidth=4.33, markersize=12)
ax.plot(n40_develop, Height, "g", marker="^",
        label="Pre-MT", linewidth=4.33, markersize=12)
ax.plot(n40_mature, Height, "r", marker="s",
        label="MT", linewidth=4.33, markersize=12)
ax.plot(n40_dissi, Height, "b", marker="o",
        label="Post-MT", linewidth=4.33, markersize=12)
# ax.set_xlim(10, None)
ax.set_ylim(0, 21)
# 尽管我们更改了整个图形的尺寸，但是可以通过以下set_xticks进行x轴标记的手动设置。
ax.set_xticks(np.arange(0, 600, 100))
ax.set_xlim(0, 445)
ax.text(0.05, 0.9, "(b)", transform=ax.transAxes, fontsize=50)
ax.set_ylabel("Height (km)", fontsize=45)
ax.set_xlabel("Area40 (km$^{2}$)", fontsize=40)
ax.tick_params(axis="both", direction='out', which="major", length=10, width=2,
               top=False, right=False)
ax.minorticks_on()
ax.tick_params(axis="both", direction="out", which="minor", length=6, width=1.5,
               top=False, right=False)
ax.legend(fontsize=35)
# n40_all = data[1]

# n40_develop = data1[1]

# n40_mature = data2[1]

# n40_dissi = data3[1]

# plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["font.size"] = 30
# fig = plt.figure(1, figsize=(30, 15))
# abcdef = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)"]
# plt.tight_layout()
# plt.title("Different Stages of boxplot", fontsize=40)
# plt.yticks(fontsize=30)
# plt.xticks(fontsize=30)
plt.savefig(f"C:\\Users\\lvyih\\Desktop\\Vertical_Profile_n40.jpeg", bbox_inches="tight", dpi=400)
"""ax.text(
        0.2, 0.1, 'some text',
        horizontalalignment='center',  # 水平居中
        verticalalignment='center',  # 垂直居中
        transform=ax.transAxes  # 使用相对坐标
    )"""
