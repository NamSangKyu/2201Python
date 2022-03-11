import matplotlib.pyplot as plt
figure = plt.figure()
# 1행 2열 - 1번째 차트
axes1 = figure.add_subplot(1,2,1)
# 1행 2열 - 2번째 차트
axes2 = figure.add_subplot(1,2,2)
# 2행 2열 - 1번째 차트
axes3 = figure.add_subplot(2,2,1)
# 2행 2열 - 2번째 차트
axes4 = figure.add_subplot(2,2,2)
plt.show()
