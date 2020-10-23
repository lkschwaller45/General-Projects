
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    print('hi')
    delta_10 = calculate_error(10)
    delta_7 = calculate_error(7)
    delta_5 = calculate_error(5)
    delta_2 = calculate_error(2)
    y_t = np.linspace(0, 5, 1000)
    plt.plot(y_t,delta_10, label='10V',color='black')
    plt.plot(y_t, delta_7, label='7V', color='red')
    plt.plot(y_t, delta_5, label='5V',color='green')
    plt.plot(y_t, delta_2, label='2V',color='blue')
    ax = plt.gca()
    ax.legend()
    plt.xlabel('Voltage at (t)')
    plt.ylabel('Dynamic Error')
    plt.show()

def calculate_error(voltage):
    y_t = np.linspace(0,5,1000)
    y_inf = voltage
    y_zero = 0
    i = 0
    M_t = np.empty(1000)
    delta = np.empty(1000)
    while i < len(y_t):
        M_t[i] = (y_t[i] - y_inf)/(y_zero - y_inf)
        delta[i] = 1 - M_t[i]
        i+=1
    return(delta)
main()
