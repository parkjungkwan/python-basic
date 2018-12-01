import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10)
y = x ^ 2
plt.title("그래프 그리기")
plt.xlabel("시간")
plt.ylabel("거리")
plt.plot(x, y, 'r')  # 라인색깔 red
plt.plot(x, y, '>') # 라인타입 - 꺽은선 

plt.show()
