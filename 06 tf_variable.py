import tensorflow as tf 

a = tf.constant(100)
b = tf.constant(120)
c = tf.constant(140)

v = tf.Variable(0)
calc_op = a + b + c
assign_app = tf.assign(v, calc_op)

sess = tf.Session()
sess.run(assign_app)

print(sess.run(v))