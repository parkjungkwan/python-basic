import tensorflow as tf

node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.Variable(node1+node2, name='node3')
init = tf.global_variables_initializer()

sess = tf.Session()
writer = tf.summary.FileWriter("./logs", sess.graph)
sess.run(init)

print(sess.run(node3))


# a = tf.placeholder(tf.float32)
# b = tf.placeholder(tf.float32)
# adder_node = a + b
# sess = tf.Session()
# print(sess.run(adder_node, feed_dict={a:3, b: 4.5}))
# print(sess.run(adder_node, feed_dict={a:[1,3], b:[2,4]}))

# writer = tf.train.SummaryWrtier("./logs", sess.graph)










