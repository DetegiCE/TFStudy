import tensorflow as tf

a = tf.constant([[1,2],[3,4]])
b = tf.constant([[1,2],[3,4]])

y1 = tf.multiply(a,b)
y2 = tf.matmul(a,b)

sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

y1_out = sess.run(y1)
y2_out = sess.run(y2)

print(y1_out)
print(y2_out)
