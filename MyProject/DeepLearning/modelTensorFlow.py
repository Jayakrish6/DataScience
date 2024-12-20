# -*- coding: utf-8 -*-
import tensorflow as tf


W = tf.Variable([.3], tf.float32)
b = tf.Variable([-.3], tf.float32)

x = tf.placeholder(tf.float32)

linear_model = W * x + b
 
y = tf.placeholder(tf.float32)
 
#Loss function
square_delta = tf.square(linear_model - y)
loss = tf.reduce_sum(square_delta)
 
#Optimize 
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

init = tf.global_variables_initializer()
 
sess = tf.Session()
 
sess.run(init)

for i in range(1000):
    sess.run(train, {x:[1,2,3,4], y:[0, -1,-2,-3]})
    
print(sess.run([W, b]))
#print(sess.run(loss, {x:[1,2,3,4], y:[0, -1,-2,-3]}))
