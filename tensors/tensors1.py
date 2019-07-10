import tensorflow as tf
a = tf.constant([[1,2],[2,3]])
b = tf.constant([[1,2],[2,3]])
add = tf.add(a,b)
sub = tf.subtract(a,b)

#define session
sess = tf.Session()
init = tf.global_variables_initializer()
sess.run(init)

#calculation
add_out = sess.run(add)
sub_out = sess.run(sub)
print(add_out)
print(sub_out)
