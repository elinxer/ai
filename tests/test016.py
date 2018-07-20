import tensorflow as tf

# 浮点型简写 1.  2.  2.
# matrix1 = tf.constant([[3., 3.]], name='matrix1')  # 1 row by 2 column
# matrix2 = tf.constant([[2.], [2.]], name='matrix2')  # 2 row by 1 column

# 矩阵相乘
# product = tf.matmul(matrix1, matrix2, name='product')

var1 = tf.constant([1, 2, 3, 4, 5, 6], name="var1", shape=[2, 3])

var2 = tf.constant([7, 8, 9, 10, 11, 12], name="var2", shape=[3, 2])

pred = tf.matmul(var1, var2, name="pred") + 1

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(pred))
    pass
