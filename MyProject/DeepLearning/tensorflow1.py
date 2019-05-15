# -*- coding: utf-8 -*-
import tensorflow as tf

a = tf.constant(5.0)
b = tf.constant(6.0)

c = a*b

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)

adder_node = a + b
sess = tf.Session()

#File_writer = tf.summary.FileWriter('C:\\Users\\Mohapjay\\MyProject\\TensorFlow\\graph', sess.graph)
print(sess.run(adder_node, {a:[1, 3], b:[2,4]}))

sess.close()
