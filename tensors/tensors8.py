import tensorflow as tf

data = [[1],[2],[3],[4]]

a = tf.placeholder(dtype=tf.float32, shape=[4,1])
b = tf.Variable([0,1,2], dtype=tf.float32)
y = tf.add(a,b)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

y_out = sess.run(y, feed_dict = {a:data})
print(y_out)
