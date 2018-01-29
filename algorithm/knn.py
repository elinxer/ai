#!/usr/bin/python3

import numpy as np

# 忽略除法错误信息
np.seterr(divide='ignore', invalid='ignore')

'''
k-近邻算法实现

http://blog.csdn.net/dobests/article/details/48580899

k 代表近邻数，表示用相邻的K个属性特征进行对比

k值选择
偏差与方差
统计学习方法中参数选择一般是要在偏差(Bias)与方差(Variance)之间取得一个平衡(Tradeoff)。

偏差：模型输出值与真实值之间的差异。偏差越高，则数据越容易欠拟合(Underfitting)，未能充分利用数据中的有效信息。
方差：对数据微小改变的敏感程度。假如有一组同一类的样本，并且这些样本的特征之间只有微小差异，用训练好的模型进行预测并求得方差。
理想情况下，我们应该得到的方差为0，因为我们预料我们的模型能很好处理这些微小的变化；
但现实中存在很多噪声(即存在不同类别的样本，其特征向量差异很小)，即使是特征差异很小的同一类样本也可能达到不同类别的结果。
而方差实际上就是衡量对噪声的敏感程度。方差越高，越容易过拟合(Overfiiting)，对噪声越敏感。
如何选择
同样，对knn而言，k值的选择也要在偏差与方差之间取得平衡。
若k取很小，例如k=1，则分类结果容易因为噪声点的干扰而出现错误，此时方差较大；
若k取很大，例如k=N(N为训练集的样本数），则对所有测试样本而言，结果都一样，是分类的结果都是样本最多的类别，这样稳定是稳定了，但预测结果与真实值相差太远，是偏差过大。
这样k即不能取太大也不能取太小，怎么办？通常的做法是，利用交叉验证（Cross Validation）评估一系列不同的k值，选取结果最好的k值作为训练参数。

'''


# 读取文本数据
def read_data(filename):
    # 读取文本数据，格式：特征1    特征2 ……  类别

    f = open(filename, 'rt')
    row_list = f.readlines()  # 以每行作为列表
    f.close()
    data_array = []
    labels_vector = []
    while True:
        if not row_list:
            break
        row = row_list.pop(0).strip().split(' ')  # 去除换行号，分割制表符（这里是分割空格）
        # print(row)
        temp_data_row = [float(a) for a in row[:-1]]  # 将字符型转换为浮点型
        data_array.append(temp_data_row)  # 取特征值
        labels_vector.append(row[-1])  # 取最后一个作为类别标签
        # print(row[-1])
        # print(labels_vector)

    return np.array(data_array), np.array(labels_vector)


# 分类
def classify(test_data, dataset, labels, k):
    # '''分类'''
    diff_dis_array = test_data - dataset  # 使用numpy的broadcasting
    dis_array = (np.add.reduce(diff_dis_array ** 2, axis=-1)) ** 0.5  # 求距离
    dis_array_index = np.argsort(dis_array)  # 升序距离的索引
    class_count = {}
    for i in range(k):
        temp_label = labels[dis_array_index[i]]
        class_count[temp_label] = class_count.get(temp_label, 0) + 1  # 获取类别及其次数的字典
    sorted_class_count = sorted(class_count.items(), key=lambda item: item[1], reverse=True)  # 字典的值按降序排列
    return sorted_class_count[0][0]  # 返回元组列表的[0][0]


# 数据标准化
def normalize(dataset):
    # '''数据归一化'''
    return (dataset - dataset.min(0)) / (dataset.max(0) - dataset.min(0))


k = 3  # 近邻数
test_data = [0.4, 0.5, 0.8]  # 待分类的场景的一组属性数据组，对应dataset中的列数
data, labels = read_data('testdata/knntest.txt')
print('数据集：\n', data)
print('标签集：\n', labels)
result = classify(test_data, normalize(data), labels, k)
print('分类结果：', result)
