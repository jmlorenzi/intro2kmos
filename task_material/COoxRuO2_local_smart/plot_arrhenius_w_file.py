"""
Generate and Arrhenius plot
using kmos

Juan M. Lorenzi
TU Munich
June 2016
"""
import math

from kmos.run import KMC_Model
model = KMC_Model(banner = False)

model.parameters.p_COgas = 2.e-1
model.parameters.p_O2gas = 1.e-1

nrel = 1e7; nsample = 1e7          # numerical parameters
Ts = range(450,650,20)             # 20 values between 450 and 650 K
fout = open('arrhenius.dat', 'w')  # open an output file
fout.write(model.get_std_header()) # print the header
# Loop over the temperature
for T in Ts:
    model.parameters.T = T   # Set the desired temperature
    model.do_steps(nrel)     # Relax the system
    # Sample the reactivity and print data to file
    output = model.get_std_sampled_data(1, nsample)
    fout.write(output)
fout.close() # Close output file

# We can read the file with numpy...
import numpy as np
data = np.loadtxt('arrhenius.dat')
iT = 0; iTOF = 3 # columns for each variable
# ... and then plot
import matplotlib.pyplot as plt
# numpy arrays can be transformed much more easily
plt.plot(1/data[:,iT], np.log10(data[:,iTOF]), '-o')
plt.xlabel('1/T [1/K]')
plt.ylabel('log(TOF) / events (sites s)^-1')
# plt.savefig('arrhenius.pdf') # Optionally, save plot
plt.show()
