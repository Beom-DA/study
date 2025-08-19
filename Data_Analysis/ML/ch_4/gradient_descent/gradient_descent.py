import numpy as np
import matplotlib.pyplot as plt
x= np.arange(-10,10,1)
f_x = x ** 2

plt.plot(x, f_x)
plt.show()


x_new = 10
derivative = []
y = []
learng_rate= 0.1
for i in range(100):
    old_value = x_new
    derivative.append(old_value - learng_rate * 2 * old_value)
    x_new = old_value - learng_rate *2* old_value
    y.append(x_new ** 2)
plt.plot(x, f_x)
plt.scatter(derivative, y)
plt.show()


def sin_function(x):
    return x * np.sin(x ** 2) + 1

def derivitive_f(x):
    return np.sin(x**2) + 2 * (x **2) * np.cos(x ** 2)
x= np.arange(-3,3,0.001)
f_x = sin_function(x)
plt.plot(x, f_x)
plt.show()


x_new = 1
derivative = []
y = []
learng_rate= 0.01
for i in range(10000):
    old_value = x_new
    x_new = old_value - learng_rate * derivitive_f(old_value)
    derivative.append(x_new)
    y.append(sin_function(x_new))

plt.plot(x, f_x)
plt.scatter(derivative, y)
plt.show()
