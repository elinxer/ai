

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# a = tf.constant(2)
# b = tf.constant(3)
#
# with tf.Session() as sess:
#     print(sess.run(a)+sess.run(b))

# state = tf.Variable(0,name='counter')
# one = tf.constant(1)
# new_value = tf.add(state,one)
# update = tf.assign(state,new_value)
# init = tf.global_variables_initializer()
# with tf.Session() as sess:
#     sess.run(init)
#     for _ in range(3):
#         sess.run(update)
#         print(sess.run(state))

# input1 = tf.placeholder(tf.float32)
# input2 = tf.placeholder(tf.float32)
#
# output = tf.multiply(input1,input2)
#
# with tf.Session() as sess:
#     print(sess.run(output,feed_dict={input1:[7.],input2:[2.]}

x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3

Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data + biases

loss = tf.reduce_mean(tf.square(y - y_data))

optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x_data, y_data)
    plt.ion()
    plt.show()
    for step in range(201):
        sess.run(train)
        prediction = sess.run(Weights) * x_data + sess.run(biases)
        lines = ax.plot(x_data, prediction, 'r-', lw=3)
        plt.pause(0.1)

        try:
            ax.lines.remove(lines[0])
        except Exception as err:
            print('error:', err)
            pass

        if step % 20 == 0:
            print(step, sess.run(Weights), sess.run(biases))
