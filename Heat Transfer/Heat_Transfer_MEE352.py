'''

Author: Luke Schwaller
Purpose: Calculate the variables of a heat exchanger to determine the perfect dimensions for transmission of heat
Class: MEE 453 Heat Transfer

'''



import ht
# ht is pythons heat transfer library, it's a chemical library not so much an engineering one, however it has built in functions for much of the heat exchanger process
import pandas as pd
# pandas is a dataframe library for python, allows compilation of data into an easily workable format
import math
# math is a default python library, needed in this case for angles
import matplotlib.pyplot as plt
# matplot lib is pythons most robust plotting mechanism, makes easy to display graphs
import numpy as np
# numpy is one of the libraries in pythons sci-py, a mathamatic and scientific library for python that allows rapid data manipulation

'''
The interpolate function preforms basic linear interpolation, making this a callable function saves time during
calculations later.
'''
def Interpolate(High_1,High_2,Low_1,Low_2,Value_1):
    Step_2 = (1/(((High_1 - Low_1)/(High_1 - Value_1))/(High_2-Low_2)))
    Final = abs(Step_2 - High_2)
    return(Final)
''' 
get_area_cylinder is a function to quickly calculate the cylinders exterior area not including extreme faces, its a one 
line calculation, but shortening it to a function removes chance of errorin calculation
'''
def get_area_cylinder(Diameter,Length):
    Area = 2*3.14*(Diameter/2)*Length
    return(Area)
#Start with declaring known variables of the system, these are from assignment/choices
Cp_H = 4196
Cp_C = 4182
M_H = 20
M_C = 40
Viscocity_H = Interpolate(85,335.4,20,1007.4,52.5)
Therm_k_H = Interpolate(85,672.8,20,602.8,52.5)
T_hi = 80
T_Ci = 20
T_ho = 25
Dia_inner = .025
Dia_outer = .045

#build the data base, it isn't needed till later but slackers never prosper
output = pd.DataFrame(columns=["Dia_inner","Re_inner","h_inner","Dia_outer","Re_outer","h_outer","U","Length","Area_inner","Area_outer","Vol_inner","Vol_outer","Vol_total","Weight_inner","Weight_outer","Weight_total"])

#The big loop, preforms all calculations based on assumptions regarding the system and the set up of the heat exchanger
while Dia_inner<.5:

    q_gen = M_H*Cp_H*(T_hi-T_ho)
    T_co = (q_gen/(M_C*Cp_C))+T_Ci
    T_cEval= (T_Ci+T_co)/2
    Viscoity_C = Interpolate(85,335.4,20,1007.4,T_cEval)
    Therm_K_C = Interpolate(85,672.8,20,602.8,T_cEval)
    Pr_C = Interpolate(85,.9563999,20,0.8458,T_cEval)
    T_lm = ((T_hi-T_cEval)-(T_ho-T_Ci))/(np.log((T_hi-T_cEval)/(T_ho-T_Ci)))
    Re_inner = (4*M_C)/(3.14*(Viscoity_C*10**(-6))*Dia_inner)
    print(Re_inner)
    Nu = .023 * ((Re_inner) ** (4 / 5)) * ((Pr_C) ** (.4))
    h_inner = (Nu * Therm_K_C)/Dia_inner
    Dia_H = Dia_outer - Dia_inner
    Dia_re = (Dia_outer+Dia_inner)
    Re_outer = (4*M_H)/(3.14*Dia_re*(Viscocity_H*10**(-6)))
    print(Re_outer)
    Diameter_ratio = Dia_inner/Dia_outer
    if (Diameter_ratio >.5):
        Nusselt = Interpolate(1,4.86,0.5,4.43,Diameter_ratio)
    else:
        print('ratio doesnt hold')
    h_outer = (Nusselt*Therm_k_H )/Dia_H
    U = (1/((1/h_inner)+(1/h_outer)))
    Length = q_gen/(U*3.14*Dia_inner*T_lm)
    print(Length)
    Density_h = Interpolate(87, 1034, 17, 1000, 52.5)
    Density_c = Interpolate(87, 1034, 17, 1000, T_co)
    Vol_total = (3.14*(Dia_outer/2) *Length)
    Vol_inner = (3.14*(Dia_inner/2) *Length)
    Vol_outer = (3.14*((Dia_outer - Dia_inner)/2) *Length)
    Weight_inner = (Density_c*Vol_inner)
    Weight_outer = (Density_h*Vol_outer)
    Weight = (Weight_inner + Weight_outer)
    Area_inner = get_area_cylinder(Dia_inner,Length)
    Area_outer = get_area_cylinder(Dia_outer,Length)

#adds data for each calculation into the overall dataframe
    output = output.append({"Dia_inner":Dia_inner,"Re_inner":Re_inner,"h_inner":h_inner,"Dia_outer":Dia_outer,"Re_outer":Re_outer,"h_outer":h_outer,"U":U,"Length":Length,"Area_inner":Area_inner,"Area_outer":Area_outer,"Vol_inner":Vol_inner,"Vol_outer":Vol_outer,"Vol_total":Vol_total,"Weight_inner":Weight_inner,"Weight_outer":Weight_outer,"Weight_total":Weight}, ignore_index=True)
# iterates the loop
    Dia_inner += .0005
    Dia_outer += .0005
#display the output so I can double check it isn't insane
print(output)
#Send data to excel for easy use in the report

output.to_excel(r'data.xlsx')

#Plots two variables from the data into a graph, can edit phrases based on the variables in the data
output.plot(x='Dia_inner',y='Weight_total')
plt.show()