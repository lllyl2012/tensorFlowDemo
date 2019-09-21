import tensorflow as tf

config = tf.ConfigProto(allow_soft_placement=True,log_device_placement=True)
#用cpu
# with tf.device('/cpu:0'):
#     rand_t = tf.random_uniform([50,50],0,10,dtype=tf.float32,seed=0)
#     a = tf.Variable(rand_t)
#     b = tf.Variable(rand_t)
#     c = tf.matmul(a,b)
#     init = tf.global_variables_initializer()
# sess = tf.Session(config=config)
# sess.run(init)
# print(sess.run(c))


#用gpu
with tf.device('/gpu:0'):
    rand_t = tf.random_uniform([50,50],0,10,dtype=tf.float32,seed=0)
    a = tf.Variable(rand_t)
    b = tf.Variable(rand_t)
    c = tf.matmul(a,b)
    init = tf.global_variables_initializer()
sess = tf.Session(config=config)
sess.run(init)
print(sess.run(c))

# for d in ['/gpu:0','/gpu:1']:
#     with tf.device(d):
#         rand_t = tf.random_uniform([50,50],0,10,dtype=tf.float32,seed=0)
#         a = tf.Variable(rand_t)
#         b = tf.Variable(rand_t)
#         c = tf.matmul(a,b)
#         init = tf.global_variables_initializer()

