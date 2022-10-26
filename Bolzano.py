import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def bolzano(func, a, b, iteration):
    i = 1
    def f(x):
        f = eval(func)
        return f 
    
    data = [['iterasi', 'x1', 'x2', 'x3', 'f(x1)', 'f(x2)', 'f(x3)']]
    while iteration > 0:
        c = (b+a)/2
        data.append([i,a,b,c,f(a),f(b),f(c)])
        i = i + 1
        if f(a) * f(b) >= 0:
            print("Tidak memenuhi iterasi bolzano")
            quit()

        elif f(c) * f(a) < 0:
            b = c

        elif f(c) * f(b) < 0:
            a = c
        else:
            print("Terjadi eror")
            quit()
        iteration -= 1

    
    print(tabulate(data, headers="firstrow", tablefmt="github"))

    print(f"Batas bawahnya adalah {a} dan batas atasnya adalah {b}")

function = input("Masukkan fungsi : ")
a = input("batas bawah: ")
b = input("batas atas: ")
iteration = input("Banyaknya iterasi: ")

x = np.linspace(-5, 5, num = 1000)
y = eval(function)
plt.axvline(x = 0, c = "black")
plt.axhline(y = 0, c = "black")
plt.plot(x, y)
plt.show()
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

bolzano(function, float(a), float(b), float(iteration))