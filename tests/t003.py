
# test 003

import os
import tensorflow as tf

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

var1 = tf.constant(3.0, dtype=tf.float32)  # 定义32位浮点数常量
var2 = tf.constant(4.3, dtype=tf.float32)
var3 = tf.constant(5.2, dtype=tf.float32)

print(var1)  # 直接打印变量属性，由于tensorflow需运行才能找到变量内容，直接打印则显示变量属性内容

sess = tf.Session()

node = tf.add(var1, var2)  # 节点相加

var3 = sess.run(node)  # 运行
print(var3)

