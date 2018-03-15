import tensorflow as tf
x = tf.placeholder(shape = (None,n+1),name = 'x')
y = tf.placeholder(shape = (None,1),name = 'y')
batch_size = 100
