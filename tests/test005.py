
import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.name_scope('graph') as scope:

    # 浮点型简写 1.  2.  2.
    matrix1 = tf.constant([[3., 3.]], name='matrix1')  # 1 row by 2 column
    matrix2 = tf.constant([[2.], [2.]], name='matrix2')  # 2 row by 1 column

    # 矩阵相乘
    product = tf.matmul(matrix1, matrix2, name='product')
    other = tf.constant([1.1, 5.], name="zzzz")

    product = tf.add(product, other)

sess = tf.Session()

# 创建图文件记录
writer = tf.summary.FileWriter("logs/", sess.graph)

# 初始化图
init = tf.global_variables_initializer()

# 在图文件写入模型
sess.run(init)
