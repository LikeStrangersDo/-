import pandas as pd


# data demo
# data = [
#     {
#         "time": 1980,
#         "data": [
#             {"name": "台湾", "value": [633.76, 12.28, "台湾"]},
#             {"name": "香港", "value": [432.47, 8.38, "香港"]},
#             {"name": "江苏", "value": [319.8, 6.2, "江苏"]},
#             {"name": "上海", "value": [311.89, 6.05, "上海"]},
#             {"name": "山东", "value": [292.13, 5.66, "山东"]},
#             {"name": "辽宁", "value": [281, 5.45, "辽宁"]},
#             {"name": "广东", "value": [249.65, 4.84, "广东"]},
#             {"name": "四川", "value": [229.31, 4.44, "四川"]},
#             {"name": "河南", "value": [229.16, 4.44, "河南"]},
#             {"name": "黑龙江", "value": [221, 4.28, "黑龙江"]},
#         ]
#     }
# ]

area = {'11': "北京", "12": "天津", "13": "河北", "14": "山西", "15": "内蒙古", "21": "辽宁", "22": "吉林", "23": "黑龙江", "31": "上海",
        "32": "江苏", "33": "浙江", "34": "安徽", "35": "福建", "36": "江西", "37": "山东", "41": "河南", "42": "湖北", "43": "湖南",
        "44": "广东", "45": "广西", "46": "海南", "50": "重庆", "51": "四川", "52": "贵州", "53": "云南", "54": "西藏", "61": "陕西",
        "62": "甘肃", "63": "青海", "64": "宁夏", "65": "新疆", "71": "台湾", "81": "香港", "82": "澳门", "91": "国外"}


def data_convert():
    # 通过用户输入查询月份执行查找花名册
    startMonth = int(input('请输入起始查询月份：'))

    data = []
    for i in range(0, 6):
        # 设置路径
        path = r'./2021年/{}月份花名册.xls'.format(startMonth+i)
        # 读取花名册
        df = pd.read_excel(path)
        # 读取花名册身份证号
        idNub = df['公民身份号码'].tolist()
        # print(idNub)

        # 设置一个空列表，用来储存省份，如['北京','北京','北京,'上海']
        province = []
        for j in range(len(idNub)):
            # 身份证号码的前两位代表省份
            provinceNub = str(idNub[j])[0:2]
            # 从area中匹配名字
            provinceName = area[provinceNub]
            province.append(provinceName)
        # 将列表内容转换成Series，然后使用pandas的value_counts进行统计
        df['province'] = province
        # 统计并转化成字典形式
        province_dict = df['province'].value_counts().to_dict()
        # 省份列表
        keysCount = list(province_dict.keys())
        # 值列表
        valueCount = list(province_dict.values())

        # 数据格式转化，{'name': '北京', 'value': [34, 1, '北京']}
        patternConvert = []
        for k in range(len(province_dict.keys())):
            pattern = {'name': keysCount[k], 'value': [valueCount[k], k+1, keysCount[k]]}
            patternConvert.append(pattern)
        # 根据dataDemo设置内层字典
        dataPatter = {'time': startMonth+i, 'data': patternConvert}
        # 装进data列表
        data.append(dataPatter)
        # 时间列表
        #
        # print(data)
        # print('*'*100)
        # print(time_list)

    return data
