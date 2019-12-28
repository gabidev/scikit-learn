import tensorflow as tf 

a = tf.placeholder(tf.int32, [3])
b = tf.constant(2)

x2 = a * b

sess = tf.Session()

r1 = sess.run(x2, feed_dict={a:[1, 2, 3]})
r2 = sess.run(x2, feed_dict={a:[11, 22, 33]})

print(r1)
print(r2)
print("=============================")

aa = tf.placeholder(tf.int32, [None])
bb = tf.constant(10)
x10 = aa * bb

rr1 = sess.run(x10, feed_dict={aa:[1, 2, 3, 4]})
rr2 = sess.run(x10, feed_dict={aa:[1, 2, 3, 4, 5, 6, 7, 8]})
print(rr1)
print(rr2)
