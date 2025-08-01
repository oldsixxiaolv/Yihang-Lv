# -- coding:utf-8 --
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split  # 划分训练集和测试集
from sklearn.neighbors import KNeighborsClassifier  # 导入KNN算法
from sklearn.metrics import accuracy_score  # 导入分类评分标准


data = pd.read_excel(r"C:\Users\lvyih\Desktop\output_julei.xlsx")
y = list(data.columns)[:-1]  # 这里得到的是第一行
X_train, X_test, y_train, y_test = train_test_split(data[y], data["npx40_divide_npx20"], random_state=1)
result = {}
for i in range(20):
    knn = KNeighborsClassifier(n_neighbors=(i + 1))
    knn.fit(X_train, y_train)
    prediction = knn.predict(X_test)
    score = accuracy_score(y_test, prediction)
    result[i+1] = score * 100
for i in result.keys():
    if result[i] == max(result.values()):
        print("最佳近临数：" + str(i))
print("模型评分" + str(max(result.values())))

