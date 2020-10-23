import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
voltage = [2, 5, 7, 10]  # Volts
resistance = 1024.42  # ohms
capacitance = .39 * (10 ** -6)
capacitance2 = .23 * (10 ** -6)
tau = resistance * capacitance
RC2 = resistance * capacitance2
A = 5
t = np.linspace(0, .04, 4000)
i = 0
y = np.empty(4000)
while i < len(t):
    y[i] = A + ((0) - A) * np.exp(-t[i] / tau)
    i+=1
plt.plot(t,y)
plt.show()