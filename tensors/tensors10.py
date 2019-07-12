import tensorflow as tf

data = [[1,2,3],[2,3,4],[3,4,5],[4,5,6]]

a = tf.placeholder(dtype=tf.float32, shape=[None,3])
b = tf.Variable([0,1,2,4], dtype=tf.float32)
b = tf.reshape(b, [-1,1])
y = tf.add(a,b)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

y_out = sess.run(y, feed_dict = {a:data})
print(y_out)
