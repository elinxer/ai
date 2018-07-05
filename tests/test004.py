# test

__author__ = 'Elinx'
__tf__ = '1.8'

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Create a graph.
g = tf.Graph()

# Establish the graph as the "default" graph.
# 创建默认图,并加入会话中
with g.as_default():
    # Assemble a graph consisting of the following three operations:
    #   * Two tf.constant operations to create the operands.
    #   * One tf.add operation to add the two operands.
    x = tf.constant(8, name="x_const")
    y = tf.constant(5, name="y_const")
    suma = tf.add(x, y, name="x_y_sum")

    z = tf.constant(10, name="z_const")

    new_sum = tf.add(suma, z, name="x_y_z_sum")

    # Now create a session.
    # The session will run the default graph.
    with tf.Session() as sess:

        # 将图写入模型文件
        writer = tf.summary.FileWriter("logs/", sess.graph)

        # 初始化图变量
        init = tf.global_variables_initializer()

        # 写入模型
        sess.run(init)
