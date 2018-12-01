import tensorflow as tf

X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

add = tf.add(X,Y)
mul = tf.multiply(X,Y)
# step 1. node 의 선택
add_hist = tf.summary.scalar("add_scalar", add) # return 이 단일
mul_hist = tf.summary.scalar("mul_scalar", mul) 

# step 2. summary 로 데이터 통합. 
merged = tf.summary.merge_all()  # 두개의 동작을 통합함

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer()) # 변수 초기화

    # step 3. writer 생성
    writer = tf.summary.FileWriter("./logs/add",sess.graph)

    for i in range(100):
        # step 4. 노드 추가
        summary = sess.run(merged, {X : i * 1.0, Y : 2.0})
        print(summary)
        writer.add_summary(summary, i)

# step 5. 콘솔에서 명령 실행 -> 텐서보드 실행





