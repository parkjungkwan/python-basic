import numpy as np

a = np.array([1,2,3])
# rank 가 1인 배열 생성
print( type(a)) # <class 'numpy.ndarray'>
print(a.shape) # (3,)
print(a[0], a[1], a[2]) # 1 2 3
a[0] = 5
print(a) # [5 2 3]

b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # (2, 3)
print(b[0,0],b[0,1],b[1,1]) # 1 2 5

print('----------------------------')

c = np.zeros((2,2)) # 모든 값이 0인 배열 생성
print(c) 
#[[0. 0.]
 # [0. 0.]]

d = np.ones((1,2)) # 모든 값이 1인 배열 생성
print(d)  # [[1. 1.]]

e = np.full((2,2), 7) # 모든 값이 7인 배열 생성
print(e) 
# [[7 7]
# [7 7]]

f = np.random.random((2,2)) # 모든 값이 랜덤으로 채워진 배열 생성
print(f)
# [[0.78742485 0.18952318]
# [0.1540344  0.1309769 ]]


