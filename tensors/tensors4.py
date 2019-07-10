import tensorflow as tf

data = [[1],[2],[3],[4]]
print("input data type is ",type(data))
a = tf.placeholder(dtype=tf.float32, shape=[None,1])

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

a_out = sess.run(a,feed_dict={a:data})

print("a type is", type(a_out))
