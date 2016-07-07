"""
Generate plots of TOF and coverage as
a function of CO patial pressure
for the CO oxidation on RuO2 1p-kMC model

Juan M. Lorenzi
TU Munich
June 2016
"""
import numpy as np

from kmos.run import KMC_Model
model = KMC_Model(banner = False)

model.parameters.T = 600.
model.parameters.p_O2gas = 1.e-1

nrel = 1e7; nsample = 1e7  # numerical parameters
pCOs = np.logspace(-2, 1, 20) # CO partial pressures
# Initialize a list for each output value
TOFs = []; CObr = []; COcus = []; Obr = []; Ocus = []
# Loop over CO partial pressure values
for pCO in pCOs:
    model.parameters.p_COgas = pCO  # Set pCO
    model.do_steps(nrel)        # Relax the system
    # Perform sampling
    output = model.get_std_sampled_data(1, nsample, output='dict')
    # Collect all data
    TOFs.append(output['CO_oxidation'])
    CObr.append(output['CO_ruo2_bridge'])
    COcus.append(output['CO_ruo2_cus'])
    Obr.append(output['O_ruo2_bridge'])
    Ocus.append(output['O_ruo2_cus'])

# Make the plots
import matplotlib.pyplot as plt
fig = plt.figure(figsize = (6,5))
ax1 = fig.add_subplot(211)    # make two plots in top of eachother
ax2 = fig.add_subplot(212)
# Top plot for the TOF
ax1.plot(pCOs, TOFs, 'k-o')
# Bottom plot for coverages
ax2.plot(pCOs, CObr, 'b-^', label='CO@bridge')
ax2.plot(pCOs, COcus, 'b-s', label='CO@cus')
ax2.plot(pCOs, Obr, 'r-^', label='O@bridge')
ax2.plot(pCOs, Ocus, 'r-s', label='O@cus')

# Set proper scales...
ax1.set_xscale('log'); ax1.set_yscale('log'); ax2.set_xscale('log')
# and labels
ax1.set_ylabel('TOF [1/(s site)]');
ax2.set_xlabel('pCO [bar]'); ax2.set_ylabel('Coverage')

plt.legend(loc='best') # render the legend
plt.tight_layout()     # and adjust figure layout
fig.savefig('vs_pCO.pdf') # Optionally save the plot
# plt.show()
