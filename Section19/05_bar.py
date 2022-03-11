import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

#폰트 설정
font_name = font_manager.FontProperties(fname='C:/Windows/Fonts/gulim.ttc').get_name()
matplotlib.rc('font',family=font_name)

figure = plt.figure()

axes = figure.add_subplot(111)
x = ['월','화','수','목','금','토','일']
y = [2,5,1,5,7,8,9]

axes.bar(x,y)
axes.plot(x,y,marker='o',color='r')
plt.show()




