# 测试 001

__author__ = 'Elinx <654753115@qq.com>'
import os
import tensorflow as tf
import numpy

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
x_data = numpy.float32(numpy.random.rand(2, 100))
y_data = numpy.dot([0.100, 0.200], x_data) + 0.300

# 构造一个线性模型
b = tf.Variable(tf.zeros([1]))
W = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))
y = tf.matmul(W, x_data) + b

# # 定义损失函数和训练方法
loss = tf.reduce_mean(tf.square(y - y_data))  # 损失函数为 -> 最小方差
optimize = tf.train.GradientDescentOptimizer(0.5)  # 梯度下降法，学习速率为0，5
train = optimize.minimize(loss)  # 训练目标：最小化损失函数

# 初始化变量
init = tf.global_variables_initializer()

# 启动图 graph
sess = tf.Session()
sess.run(init)  # 模型启动

# 拟合平面，画图
for step in range(0, 201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))

sess.close()
