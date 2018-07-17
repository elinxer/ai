
"""
tf基础知识



"""

import tensorflow as tf

W = tf.constant([[1, 2, 3], [3, 2, 1]])


print("W: ", W)


"""

result:

W:  Tensor("Const:0", shape=(2, 3), dtype=int32)

由图可以看见，关于Tensor的解释主要由三个属性组成：名字(name)、维度(shape)、类型(type)。
其中第一个属性名字给出了这个张量是怎么来的，
"Const:0"表示的是这个张量由计算节点Const（关于节点的解释下面介绍Flow的时候给出）输出的第一个结果得来；
第二个属性shape给出了这个张量的维度信息，shape=(2,3)说明了张量是个二维数组，也可理解为一个2 x 3的矩阵；
第三个属性说明了张量的数据类型，TensorFlow支持14种不同的类型：
浮点型float(tf.float32, tf.float64)， 整数型int(tf.int8, tf.int16, tf.int32, tf.int64, tf.int128)， 
布尔型(tf.bool)，复数(tf.complex64, tf.complex128)，
值得注意的一点时，当两个张量进行运算时，数据类型要相同，不然TensorFlow会报错。由此可见我们定义的W并非简单的数组。

"""




