
# 模拟投掷色子

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

with tf.Graph().as_default(), tf.Session() as sess:

    dice1 = tf.Variable(tf.random_uniform([10, 1],
                                          minval=1, maxval=7,
                                          dtype=tf.int32))

    dice2 = tf.Variable(tf.random_uniform([10, 1],
                                          minval=1, maxval=7,
                                          dtype=tf.int32))
    dice_sum = tf.add(dice1, dice2)

    # We've got three separate 10x1 matrices. To produce a single
    # 10x3 matrix, we'll concatenate them along dimension 1.
    resulting_matrix = tf.concat(
        values=[dice1, dice2, dice_sum], axis=1)

    # The variables haven't been initialized within the graph yet,
    # so let's remedy that.
    sess.run(tf.global_variables_initializer())

    print(resulting_matrix.eval())
