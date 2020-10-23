import numpy as np
voltage = [2,5,7,10] #Volts
resistance = 1024.42 #ohms
capacitance =  .39*(10**-6)
capacitance2 =  .23*(10**-6)
RC = resistance*capacitance
RC2 = resistance*capacitance2
print(np.log(1))

y_t = 5
y_inf = 7
y_0 = 0

M1 = (y_t - y_inf)/(y_0 - y_inf)
M2 = RC*(-1*np.log(M1))
dyn_error = 1 - M1
print(M1)
print(M2)
print(dyn_error)

y_t = 5
y_inf = y_t + 1.5
y_0 = y_t - 1.5

M = (y_t - y_inf)/(y_0 - y_inf)
dyn_error = 1 - M



i = 0
t = np.linspace(0,.04,4000)
step2 = [0] * 4000
while i < 4000:

    tau = 0.0003995238
    step1 = 1- (np.exp(-t[i]/tau))
    step2[i] = step1 *(y_0 - y_inf) + y_inf

    i+=1



    voltage = [2, 5, 7, 10]  # Volts
    resistance = 1024.42  # ohms
    capacitance = .39 * (10 ** -6)
    capacitance2 = .23 * (10 ** -6)
    tau = resistance * capacitance
    RC2 = resistance * capacitance2
    A = 5
    t = np.linspace(0,.0004,4000)
    i = 0
    y = np.empty(4000)
'''
    while i < len(t):
        y[i] = A + ((0)-A)*np.exp(-t[i]/tau)
'''