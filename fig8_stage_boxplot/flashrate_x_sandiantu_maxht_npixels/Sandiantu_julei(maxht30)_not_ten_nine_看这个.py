# -- coding:utf-8 --
from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt
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
    maxht30 = data.select("maxht30")[:]
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
    npixels_40_K = np.multiply(npixels_40, 4)
    npixels_40_K = np.divide(npixels_40_K, math.pi)
    npixels_40_R = np.sqrt(npixels_40_K)
    npixels_30 = data.select("npixels_30")[:]
    npixels_30 = npixels_30[index]
    npixels_30 = npixels_30[indexw]
    npixels_30 = npixels_size(npixels_30, boost)
    npixels_30_K = np.multiply(npixels_30, 4)
    npixels_30_K = np.divide(npixels_30_K, math.pi)
    npixels_30_R = np.sqrt(npixels_30_K)
    npixels_20 = data.select("npixels_20")[:]
    npixels_20 = npixels_20[index]
    npixels_20 = npixels_20[indexw]
    npixels_20 = npixels_size(npixels_20, boost)
    npixels_20_K = np.multiply(npixels_20, 4)
    npixels_20_K = np.divide(npixels_20_K, math.pi)
    npixels_20_R = np.sqrt(npixels_20_K)
    maxnsrain = data.select("maxnsrain")[:]
    maxnsrain = maxnsrain[index]
    maxnsrain = maxnsrain[indexw]
    flashcount = flashcount.astype(float)
    flashrate = np.divide(flashcount, viewtime)
    flashrate = np.multiply(flashrate, 60)
    fls30 = np.divide(flashrate, npixels_30)
    fls30 = np.multiply(fls30, 100)
    fls40 = np.divide(flashrate, npixels_40)
    fls40 = np.multiply(fls40, 100)
    inde = list(np.where(r > 0.67))
    index_add1 = list(np.where(minir > 0))
    inded = list(set(inde[0]) & set(index_add1[0]))
    inded = sorted(inded)
    flashrate = flashrate[inded]
    maxht40 = maxht40[inded]
    maxht20 = maxht20[inded]
    maxht30 = maxht30[inded]
    npixels_20 = npixels_20[inded]
    npixels_30 = npixels_30[inded]
    npixels_40 = npixels_40[inded]
    fls30 = fls30[inded]
    fls40 = fls40[inded]
    r = r[inded]
    return maxht20, maxht30, maxht40, flashrate, npixels_20, npixels_30, npixels_40, fls40, r


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


def ten_nine(x, former, latter):
    to_sort_data = sorted(x)
    index1 = list(np.where(x >= to_sort_data[round(len(to_sort_data) * former)]))
    index2 = list(np.where(x <= to_sort_data[round(len(to_sort_data) * latter)]))
    index = list(set(index1[0]) & set(index2[0]))
    return index


"""程序开始"""
# 程序发起点
plt.rc('axes', linewidth=3)
plt.tick_params(width=3)
name = ["Maxht20 (km)", "Maxht30 (km)", "Maxht40 (km)", r'FlRate (fl' + r'$\cdot$' + r'min$\mathregular{^{-1}}$)',
        r"Area20 (km$\mathregular{^{2}}$)",
        r"Area30 (km$\mathregular{^{2}}$)", r"Area40 (km$\mathregular{^{2}}$)",
        r'Fl40 (fl' + r'$\cdot$' + r'(100km)$\mathregular{^{-2}}$' +
                r'$\cdot$' + r'min$\mathregular{^{-1}}$)']
data = read_shuju()
# data_add = read_shuju_ADD()
# data_mid = []
# for i, j in zip(data, data_add):
#     data_mid.append(np.concatenate((i, j)))
# data = data_mid
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
# stage4 = duqu_excel_julei(r"C:\Users\lvyih\Desktop\stage4.xlsx")
# stage5 = duqu_excel_julei(r"C:\Users\lvyih\Desktop\stage5.xlsx")
data1 = for_(data, stage1)
data2 = for_(data, stage2)
data3 = for_(data, stage3)
# data4 = for_(data, stage4)
# data5 = for_(data, stage5)
# print(np.mean(data1[2] / (np.sqrt(data1[6] / math.pi) * 2)))
# print(np.mean(data2[2] / (np.sqrt(data2[6] / math.pi) * 2)))
# print(np.mean(data3[2] / (np.sqrt(data3[6] / math.pi) * 2)))
print(np.mean(data1[8]))
print(np.mean(data2[8]))
print(np.mean(data3[8]))
# print(np.mean(data4[7]))
# print(np.mean(data5[7]))
# print(len(data3[0]))
# print(len(data2[0]))
# print(len(data2[0]))
stage = ["All", "Pre-MT", "MT", "Post-MT"]
coefficient = 0
fig = plt.figure(coefficient, figsize=(38, 18))
plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["font.size"] = 35
mid = 1
abcdef = ["(a)", "(b)", "(c)", "(d)", "(e)", "(f)", "(g)", "(h)"]
for j in range(0, 8):
    ALL_STAGE = data[j]
    ALL_STAGE = ALL_STAGE[ten_nine(ALL_STAGE, 0.01, 0.99)]
    # Development = data1[j]
    Pre_Maturity = data1[j]
    Pre_Maturity = Pre_Maturity[ten_nine(Pre_Maturity, 0.01, 0.99)]
    Maturity = data2[j]
    Maturity = Maturity[ten_nine(Maturity, 0.01, 0.99)]
    # Post_Maturity = data4[j]
    Dissipation = data3[j]
    Dissipation = Dissipation[ten_nine(Dissipation, 0.01, 0.99)]
    ax = fig.add_subplot(2, 4, mid)
    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)
    if j == 0:
        ax.set_ylim(-0.7, 20.5)
    elif j == 1:
        ax.set_ylim(-0.7, 20.5)
    elif j == 2:
        ax.set_ylim(-0.5, 15.5)
    elif j == 3:
        ax.set_ylim(-1, 33)
    elif j == 4:
        ax.set_ylim(-120, 4010)
    elif j == 5:
        ax.set_ylim(-60, 2200)
    elif j == 6:
        ax.set_ylim(-30, 1030)
    elif j == 7:
        # for fls30
        # ax.set_ylim(-0.1, 3.3)
        # for fls40
        ax.set_ylim(-0.2, 8.7)
    ax.tick_params(direction='in', which="major", length=10, width=2,
                   top=False, right=False)
    # 用于设置y轴的刻度的大小即yticks的大小
    ax.tick_params(axis="y", labelsize=38)
    ax.minorticks_on()
    ax.tick_params(direction="in", which="minor", length=6, width=1.5,
                   top=False, right=False, bottom=False)
    ax.boxplot([ALL_STAGE, Pre_Maturity, Maturity, Dissipation], widths=0.4,
               showmeans=True, labels=stage, showfliers=False, whis=1, medianprops={"c": "black"},
               whiskerprops={"linestyle": "--", "linewidth": 2, "c": "black"})
    # ax.set_xlabel(fontsize=40)
    # ax.set_yticks(fontsize=30)
    # ax.set_xticks(fontsize=30)
    ax.set_title(f"{name[j]}", fontsize=40)
    ax.text(0.04, 0.9, abcdef[j], transform=ax.transAxes, fontsize=50)
    mid += 1
# plt.tight_layout(h_pad=0.5)
# plt.title("Different Stages of boxplot", fontsize=40)
# plt.yticks(fontsize=30)
# plt.xticks(fontsize=30)
plt.savefig(f"C:\\Users\\lvyih\\Desktop\\stage_boxplot.jpeg", bbox_inches="tight", dpi=400)
"""ax.text(
        0.2, 0.1, 'some text',
        horizontalalignment='center',  # 水平居中
        verticalalignment='center',  # 垂直居中
        transform=ax.transAxes  # 使用相对坐标
    )"""
