import matplotlib.pyplot as plt

plt.style.use('ggplot')
mbr = ['kim','lee','park','kwon','shim']
mbr_idx = range(len(mbr))
score = [100, 80, 60, 50,30]
fig = plt.figure()
ax1 =  fig.add_subplot(1,1,1)
ax1.bar(mbr_idx, score, align = 'center', color = 'blue')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xticks(mbr_idx, mbr, rotation = 0, fontsize = 'small')
# rotation = 0 은 눈금레이블을 수평으로 지정
plt.xlabel('name')
plt.ylabel('score')
plt.title('grade')
plt.savefig('score.png', dpi=400, bbox_inches = 'tight')
# dpi 는 해상도, bbox_inches = 'tight' 는 그림의 여백을 제거
plt.show()










