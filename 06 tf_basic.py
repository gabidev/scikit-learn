import tensorflow as tf 

hello = tf.constant('Hello Tensorflow!')
print(hello)

sess = tf.Session()
print(sess.run(hello))

a = tf.constant(10)
b = tf.constant(40)
c = tf.add(a, b)
print(c)
print(sess.run(c))
print(sess.run([a, b, c]))

sess.close()
