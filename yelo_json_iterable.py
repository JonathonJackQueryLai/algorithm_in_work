#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/25 20:10
# @Author  : Jonathon
# @File    : json_iterable.py
# @Software: PyCharm
# @ Motto : 客又至，当如何
import numpy as np
'''
当json数据结构不明确的时候,使用递归去遍历整个json（dict）的嵌套结构
'''

def nan2none(data):
    if isinstance(data, list):
        for i, v in enumerate(data):
            if isinstance(v, dict) or isinstance(v, list):
                nan2none(v)
            elif v == 'nan' or v == 'NaN' or v is np.nan:
                data[i] = None
    elif isinstance(data, dict):
        for k, v in data.items():
            if isinstance(v, dict) or isinstance(v, list):
                nan2none(v)
            elif v == 'nan' or v == 'NaN' or v is np.nan:
                data[k] = None


if __name__ == '__main__':
    json_data = {
        'a': {'b': [np.nan, None, 'NaN']},
        'c': [np.nan, None, 'NaN', 1],
        'd': 'value'
    }
    nan2none(json_data)
    print(json_data)
