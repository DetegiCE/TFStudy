import tensorflow as tf

data = [1,2,3,4]

a = tf.placeholder(dtype=tf.float32)

y1 = tf.arg_max(a,0)
y2 = tf.arg_min(a,0)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

y1_out = sess.run(y1, feed_dict={a:data})
y2_out = sess.run(y2, feed_dict={a:data})

print(y1_out)
print(y2_out)
