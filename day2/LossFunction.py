import tensorflow as tf

sess = tf.Session()

X = tf.placeholder(tf.float32, name='X')
Y = tf.placeholder(tf.float32, name='Y')

w0 = tf.Variable(0.0)
w1 = tf.Variable(0.0)

Y_hat = X*w1 + w0

loss = tf.square(Y - Y_hat, name='loss')

sess.close()