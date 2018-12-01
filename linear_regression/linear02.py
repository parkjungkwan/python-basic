import tensorflow as tf
tf.set_random_seed(777)
x_train = [1,2,3]
y_train = [1,2,3]
# trainable 한 variable 이다.


W = tf.Variable(tf.random_normal([1]),name = 'weight') # 가중치
b = tf.Variable(tf.random_normal([1]),name='bias')
# 랭크가 1인 배열
# 텐서가 사용하는 variable 이다
hypothesis = x_train * W + b
# hypothesis 는 x_train 에 따라서 결정 될 것이다.
# hypothesis 은 하나이고 x_train 은 다수의 데이터를 뜻하고
# 위 식에서 x_train 은 독립된 별개의 데이터(독립변수)이고
# hypothesis 는 x_train에 의해 결정되는 종속변수이다.
cost = tf.reduce_mean(tf.square(hypothesis - y_train))

# 비용함수의 최소화 minimize
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)
# train 은 노드가 되고 이것을 실행해야 한다.
sess = tf.Session()
sess.run(tf.global_variables_initializer())
# variable 은 반드시 초기화 해야 한다
# 학습시킨다 -> training
for step in range(2001):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(cost), sess.run(W), sess.run(b))
# 최적화를 학습한다 learn best fit W:[1], b:[0]

# 트레이닝을 실행하면 코스트, 하이퍼시스의 W와  b 값을 추출할 수 있다
# W = 1 이 되고, b = 0 이 되면 학습이 잘 된 것이다.라고 정의

