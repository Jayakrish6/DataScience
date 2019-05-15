# -*- coding: utf-8 -*-
import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)

sess = tf.Session()

#print(sess.run([node1, node2]))

#sess.close()

with tf.Session() as sess:
    output = sess.run([node1, node2])
    print(output)
    
a = tf.constant(5.0)
b = tf.constant(6.0)

c = a*b

sess = tf.Session()

print(sess.run(c))

sess.close()

