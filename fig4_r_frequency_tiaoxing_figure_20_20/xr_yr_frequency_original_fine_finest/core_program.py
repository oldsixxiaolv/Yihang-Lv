import numpy as np


def core_program(average_y, zuizhongy, rx):
    """�������������ݴ���������򣬵õ�����ͼ��Ҫ������"""
    begin = 0
    for i in average_y:
        if begin != 1:
            if i == []:
                zuizhongy.append(np.NAN)
                rx.append(f"{begin:.2f}")
                begin += 0.01
            else:
                for j in i:
                    zuizhongy.append(j)
                    rx.append(f"{begin:.2f}")
                begin += 0.01
        else:
            if i == []:
                zuizhongy.append(np.NAN)
                rx.append(f"{begin:.2f}")
            else:
                for j in i:
                    zuizhongy.append(j)
                    rx.append(f"{begin:.2f}")
        begin = float(f"{begin:.2f}")
    return rx, zuizhongy