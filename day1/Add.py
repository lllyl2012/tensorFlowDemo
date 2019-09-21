import tensorflow as tf

a = tf.constant([1,2,3,4])
b = tf.constant([2,3,4,5])

result = tf.add(a,b)

with tf.Session() as sess:
    print(sess.run(result))

