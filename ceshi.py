# -- coding:utf-8 --
import os
import sys
import math
x = int(input())
y = input().split()
# 请在此输入您的代码


def m_out(m):
    n_out = (-1 + math.sqrt(1 + 8 * m)) / 2
    n_out = n_out // 1
    return int(n_out)


def add(x):
    mid = 0
    for hh in range(0, x+1):
        mid += hh
    return mid


def pingfang(n, m):
    out_former = n * (n + 1) / 2
    out_latter = out_former + n + 1
    out_latter_list = []
    for q in range(1, n+1):
        out_latter_list.append(int(out_latter - add(q)))
    out_latter_list.append(out_latter)
    out_latter_list.append(out_former)
    print(out_latter_list)
    if m not in out_latter_list:
        output = 1
    else:
        output = 0
    return output


delete = 0
for i in y:
    if int(i) % 2 != 0:
        pass
    elif int(i) == 2:
        delete += 1
    else:
        mmm = pingfang(m_out(int(i)), int(i))
        delete += mmm
print(delete)
# def A_n(x):
#     acumulus_add = 0
#     for j in range(1, x+1):
#         acumulus_add += j
#     return acumulus_add
# def B_n(y):
#     acumulus_multiply = 1
#     for w in range(1, y+1):
#         acumulus_multiply *= w
#     return acumulus_multiply
#
#
# acumulus_all = 0
# for i in range(1, 2024041331404203):
#     A = A_n(i)
#     B = B_n(i)
#     C = A - B
#     left = C % 100
#     if left == 0 and C != 0:
#         acumulus_all += 1
# print(acumulus_all)
