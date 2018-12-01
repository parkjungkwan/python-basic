import tensorflow as tf
def test1():
    a = tf.placeholder(tf.int16)
    b = tf.placeholder(tf.int16)

    add = tf.add(a, b)
    mul = tf.multiply(a,b)

    with tf.Session() as sess:
        r1 = sess.run(add, feed_dict = {a : 2, b: 4})
        r2 = sess.run(mul, feed_dict = {a : 2, b: 4})
        # {a : 2, b: 4} 는 딕셔너리 

        print(r1, r2) # 덧셈6  곱셈 8
def test2():
    x = tf.Variable([1.0,2.0])
    y = tf.constant([3.0,3.0])
    sub = tf.subtract(x, y) 
    with tf.Session() as sess:
        x.initializer.run() # 변수 x 를 초기화 하는 문법
        r1 = sess.run(sub)
        print(r1)
if __name__=="__main__":
    test2()
