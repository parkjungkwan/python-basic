'''
    K-평균 알고리즘
    군집화(Cluster) 문제를 풀기위한 비지도학습 알고리즘.
    ※  지도학습 : 데이터 라벨링하는 작업. 특정 데이터를 입출력하는 것을 반복해서 학습시키는 방식
    주어진 데이터를 지정된 군집 개수(K) 로 그룹화하여 한 그룹내의 동일한 성질을 가지고 다른 그룹과
    차별화 시키는 것.
    알고리즘의 결과는 중심(centroid) 라고 부르는 K 개의 점(dot) 으로, 이들은 각기 다른 그룹의 중심점을
    나타낸다.
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

num_points = 2000
vectors_set = []
for i in range(num_points):
    if np.random.random() > 0.5:
        vectors_set.append([np.random.normal(0.0, 0.9),
                                    np.random.normal(0.0,0.9)])
    else:
        vectors_set.append([np.random.normal(3.0, 0.5),
                                    np.random.normal(1.0,0.5)])
df = pd.DataFrame({
            "x" : [v[0] for v in vectors_set],
            "y" : [v[1] for v in vectors_set]
    })
sns.lmplot("x", "y", data = df, fit_reg = False, size = 6)
plt.show()











