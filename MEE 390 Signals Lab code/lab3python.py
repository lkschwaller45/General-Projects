import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

resistance = 1024.42 #ohms
capacitance =  .39*(10**-6)
capacitance2 =  .23*(10**-6)
uncert_r = .005
uncert_c = (.005)*(10**-6)

uncert = np.sqrt(((resistance*uncert_c)**2)+((capacitance2*uncert_r)**2))
print(uncert)
