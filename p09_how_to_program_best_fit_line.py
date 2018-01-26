import matplotlib.pyplot as plt
import numpy as np
from statistics import mean
from matplotlib import style
style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6],dtype = np.float64)
ys = np.array([5,4,6,5,6,7],dtype = np.float64)

def best_fit_slope(xs,ys):
    m = (mean(xs)*mean(ys) - mean(xs*ys))/ (mean(xs)**2 - mean(xs**2))
    b = mean(ys) - m*mean(xs)
    return m,b


m,b = best_fit_slope(xs,ys)

# print(m,b)

regression_line = [(m*x+b) for x in xs]

predict_x = 8
predict_y = (m*predict_x)+b



plt.scatter(xs,ys)
plt.plot(xs,regression_line)
plt.show()

