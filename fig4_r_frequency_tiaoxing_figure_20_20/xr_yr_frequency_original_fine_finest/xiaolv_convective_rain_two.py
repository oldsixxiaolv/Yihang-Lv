import matplotlib.pyplot as plt
from all_the_shuju_two import allshuju_two
from read_shuju import read_shuju
from x_labels import x_labels
import numpy as np
from read_shuju_add import read_shuju_ADD


def round2(x):
    """由于之后要用到map函数，在此创建一个函数"""
    ok = round(x, 1)
    return ok


def researching(x, y, fre, begin=0):
    """用来找到0.9和0.8的阙值x"""
    jiu = 0
    for w in fre:
        print(w)
        if (w > x) and (w < y):
            jiu = round(w, 2)
            break
        begin += 0.01
    return round(begin, 2), jiu


def for_(data, stage):
    return data[stage]


def duqu_excel_julei(path):
    import pandas as pd
    file_path = path
    df = pd.read_excel(file_path, usecols=[1], names=None)
    dali = df.values.tolist()
    result = []
    for i in dali:
        result.append(i[0])
    return result


"""读取数据部分"""
all_list = read_shuju()
# stage = duqu_excel_julei(r"C:\Users\lvyih\Desktop\stage.xlsx")
# all_list = for_(all_list, stage)
# all_list2 = read_shuju_ADD()
r = all_list
# r2 = all_list2
# r = np.concatenate((r, r2))
# print(len(r))
# r中有一个空缺值，通过allshuju_two处理后就会消去。
# 这里的frequency最终得到的是0-1的每隔0.01的个数作为元素的列表
frequency = []
allshuju_two(r, frequency)
hh = 0
for i in frequency:
    hh += i
print(hh)
print(len(r))
# 这里的cumsum进行一个累加操作
frequence = np.cumsum(frequency)
# 这里进行求比例处理
frequence = np.divide(frequence, len(r))
# 做到0.96的界限
# begin2, jiu2 = researching(0.959, 0.961, frequence)
# 做到0.95界限
# begin2, jiu2 = researching(0.948, 0.952, frequence)
# 做到0.9的界限
begin2, jiu2 = researching(0.896, 0.900, frequence)
label = x_labels()
labels = []
label = list(map(str, label))
for n in range(0, 101):
    mid = n / 100
    labels.append(float(f"{mid:.2f}"))
label[-1] = "0"
"""绘制图形部分"""
# 我们要注意的是如果我们要对x轴进行自定义然后又要在画图了之后进行设置，一定要用fig，ax=plt.subplots()这个函数才行
fig, ax2 = plt.subplots(1, 1, figsize=(40, 16.75))
# 设置全局的字体样式（即更改默认值）[只对最外层的有作用]
# plt.rcParams["font.family"] = "Times New Roman"
# plt.rcParams["font.size"] = 28
# set_xticks和set_xticklabels一般要一起出现，xticklabels对xticks的进行修正。
# (xticks只输入列表或者数组等，后不加参数，参数在xticklabels那里设置)
# bar函数可以让x轴是数字或者就是字符串
# 我们总结一点就是如果我们画的图的x轴就是数字，那么一定要先用set_xticks先来操作再用set_xticklabels
# 如果我们画的图的x轴就是字符串的，那么set_xticklabels就可以直接用
"""先绘制第一层图形"""
# 这里的plot加上一个"r"的意思是指明线是红色的
plt.rc('axes', linewidth=3)
ax2.plot(labels, frequence)
ax2.fill_between(labels, frequence, hatch="|", color="#D7F4C1")
ax2.set_yticks(np.array(list(map(round2, list(np.arange(0, 1.1, 0.2))))))
ax2.set_ylabel("percent (%)", font={"family": "Times New Roman", "size": 75})
ax2.set_yticklabels(np.array(list(map(round2, list(np.arange(0, 110, 20))))),
                    font={"family": "Times New Roman", "size": 55})
ax2.set_xticks(labels)
ax2.set_xlabel("Ratio", font={"family": "Times New Roman", "size": 75})
ax2.set_xticklabels(label, font={"family": "Times New Roman", "size": 55})
# ax2.axis(labels.extend(list(map(round2, list(np.arange(0, 1.1, 0.2))))), fontsize=16)
# ax2.vlines(begin1, 0, jiu1, linestyles="dashed", color="red", label=f"r={round(1-begin1, 2)} ,  95%", linewidth=4)
# ax2.hlines(jiu1, begin1, 1, linestyles="dashed", colors="red", linewidth=4)
ax2.vlines(begin2, 0, jiu2, linestyles="dashed", color="blue",
           label=f"Ratio = {round(1-begin2, 2)} ,  90%", linewidth=4)
ax2.hlines(jiu2, begin2, 1, linestyles="dashed", color="blue", linewidth=4)
# 指明x和y的范围
ax2.set_ylim(-0.01, None)
# 让r的坐标从最左边的哪里开始出现标签
ax2.set_xlim(-0.012, 1.005)
# 指明图的标签所在的位置
# ax2.legend(loc="lower right", prop={"family": "Times New Roman", "size": 63})
# ax2.set_title("TRMM tropical convective dataset\n"
#               "The distribution of different values of convective precipitation proportions",
#               font={"family": "Times New Roman", "size": 65})
ax2.get_yaxis().set_visible(False)
ax2.tick_params(axis="x", which="major", length=7.5, width=3, pad=10)
# 手动调整一下x轴的刻度值的长度
xticks = ax2.xaxis.get_major_ticks()
for i in range(0, 101, 5):
    xticks[i].tick1line.set_markersize(15)
# ax2.tick_params(axis="x", which="minor", length=8, width=2)
# ax2.yaxis.tick_right()
"""从这里绘制第二层图形"""
ax = ax2.twinx()
ax.set_ylabel("Frequence (#)", font={"family": "Times New Roman", "size": 75})
ax.set_yticks(np.array(list(map(int, list(np.arange(0, 5500, 1000))))))
ax.set_yticklabels(np.array(list(map(int, list(np.arange(0, 5500, 1000)))))
                   , font={"family": "Times New Roman", "size": 55})
ax.bar(labels, frequency, width=0.006)
ax.set_ylim(-40, 5500)  # (-40, None)
ax.yaxis.set_label_position("left")
ax.tick_params(axis="y", which="major", length=15, width=3, pad=10)
# ax.tick_params(axis="y", direction='in', which="minor", length=12, width=2)
# ax.yaxis.tick_right()
# 设置让y轴不显示
# ax.get_yaxis().set_visible(False)
"""第三层画图"""
ax1 = ax.twinx()
ax1.plot(labels, frequence, color="red", linewidth=5)
ax1.set_yticks(np.array(list(map(round2, list(np.arange(0, 1.1, 0.2))))))
ax1.set_yticklabels(np.array(list(map(round2, list(np.arange(0, 110, 20))))),
                    font={"family": "Times New Roman", "size": 55})
ax1.set_ylabel("CDF (%)", font={"family": "Times New Roman", "size": 75}, color="red")
ax1.set_ylim(-0.01, None)
# y轴的刻度的长度和宽度进行设置
ax1.tick_params(axis="y", which="major", length=15, width=3, pad=10, colors="red")
ax1.vlines(begin2, 0, jiu2, linestyles="dashed", color="blue",
           label=f"Ratio = {round(1-begin2, 2)} ,  90%", linewidth=4)
ax1.hlines(jiu2, begin2, 1, linestyles="dashed", color="blue", linewidth=4)
# ax1.tick_params(axis="y", direction='in', which="minor", length=12, width=2)
# 储存绘制的图形
# 把ax2再画蓝线
ax2.legend(loc="lower right", prop={"family": "Times New Roman", "size": 63})
plt.savefig(r"C:\Users\lvyih\Desktop\r_percent_latterhh.jpeg", dpi=400)


