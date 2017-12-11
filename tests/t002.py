# 测试

__author__ = 'Elinx'

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# 训练过程中使用到的变量都需要初始化
init_op = tf.global_variables_initializer()

# 启动
sess = tf.Session()

# 训练项
hello = tf.constant('Hello, TensorFlow!')

# 训练
sess.run(hello)

# 关闭，训练完成
sess.close()

