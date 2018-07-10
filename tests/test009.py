# 拟合平面训练

import tensorflow as tf
import numpy as np
import sys  # 未用到

# 生成数据
x_data = np.float32(np.random.rand(2, 100))  # 随机输入
y_data = np.dot([0.200, 0.300], x_data) + 0.500

# print(x_data)
# print(y_data)

# 构造一个线性模型
b = tf.Variable(tf.zeros([1]))
w = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(w, x_data) + b

# 求解模型
# 设置损失函数
loss = tf.reduce_mean(tf.square(y - y_data))

# 选择梯度下降的方法
optimizer = tf.train.GradientDescentOptimizer(0.5)

# 最小损失函数
train = optimizer.minimize(loss)

# 初始化变量
init = tf.global_variables_initializer()

# 设置tf度gpu按需分配
config = tf.ConfigProto()
config.gpu_options.allow_growth = True

# 启动图
sess = tf.Session(config=config)
sess.run(init)

# 迭代 反复执行上面的最小化损失函数，拟合平面
for step in range(0, 501):
    sess.run(train)
    print(step, sess.run(w), sess.run(b))


