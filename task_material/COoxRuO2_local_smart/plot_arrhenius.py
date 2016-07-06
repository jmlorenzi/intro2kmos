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

nrel = 1e7; nsample = 1e7  # numerical parameters
Ts = range(450,650,20)     # 20 values between 450 and 650 K
TOFs = []                  # empty list for output
# Loop over the temperature
for T in Ts:
    model.parameters.T = T   # Set the temperature
    model.do_steps(nrel)     # Relax the system
    # Sample the reactivity
    output = model.get_std_sampled_data(1, nsample, output='dict')
    # Collect output
    TOFs.append(output['CO_oxidation'])

# Transform the variables
invTs = [1/float(T) for T in Ts]
logTOFs = [math.log(TOF,10.) for TOF in TOFs]

# and plot
import matplotlib.pyplot as plt
plt.plot(invTs, logTOFs, '-o')
plt.xlabel('1/T [1/K]')
plt.ylabel('log(TOF) / events (sites s)^-1')
plt.savefig('arrhenius.pdf') # Optionally, save plot
plt.show()
