# 矩阵 - 张量

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 设置按需使用GPU
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
# sess = tf.InteractiveSession(config=config)


with tf.Graph().as_default():
    primes = tf.constant([2, 3, 5, 67, 11, 13], dtype=tf.int32)

    ones = tf.ones([6], dtype=tf.int32)

    just_beyond_primes = tf.multiply(primes, ones)

    with tf.Session() as sess:
        print(just_beyond_primes.eval())
        print(sess.run(ones))
