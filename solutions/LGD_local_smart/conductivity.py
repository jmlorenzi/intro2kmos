"""
Study the conductivity of a simple ion diffusion
model as a function of concentration gradient
and external electric field using kmos

Juan M. Lorenzi
TU Munich
June 2016
"""
from kmos.run import KMC_Model
import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 50
H = 20

NREL = 1e7
NSAMPLE = 5e7

# current vs field
theta = 0.5
currents = []
fields = np.linspace(0.005, 0.04, 10)
for eps_f in fields:
    model = KMC_Model(banner = False, size = [L, H])

    model.parameters.thetaS = theta
    model.parameters.thetaD = theta
    model.parameters.eps_f = eps_f

    model.do_steps(NREL)
    exit0 = (model.base.get_procstat(model.proclist.drain_exit)
            - model.base.get_procstat(model.proclist.drain_entry))
    t0 = model.base.get_kmc_time()

    model.do_steps(NSAMPLE)
    currents.append( ( model.base.get_procstat(model.proclist.drain_exit)
                   - model.base.get_procstat(model.proclist.drain_entry)
                   - exit0) / (model.base.get_kmc_time() - t0) / float(L))
    model.deallocate()

fig = plt.figure(figsize = (8, 5))
plt.plot(fields, currents, '-o')
plt.xlabel('Field contribution [eV]')
plt.ylabel('Current [ ions / (s site) ]')
plt.savefig('current_vs_field.pdf')

# current vs. concentration
eps_f = 0.02
currents = []
thetas = np.linspace(0.1, 0.9, 9)
for theta in thetas:
    model = KMC_Model(banner = False, size = [L, H])

    model.parameters.thetaS = theta
    model.parameters.thetaD = theta
    model.parameters.eps_f = eps_f

    model.do_steps(NREL)
    exit0 = (model.base.get_procstat(model.proclist.drain_exit)
            - model.base.get_procstat(model.proclist.drain_entry))
    t0 = model.base.get_kmc_time()

    model.do_steps(NSAMPLE)
    currents.append( ( model.base.get_procstat(model.proclist.drain_exit)
                   - model.base.get_procstat(model.proclist.drain_entry)
                   - exit0) / (model.base.get_kmc_time() - t0) / float(L))
    model.deallocate()

fig = plt.figure(figsize = (8, 5))
plt.plot(thetas, currents, '-o')
plt.xlabel('Concentration')
plt.ylabel('Current [ ions / (s site) ]')
plt.savefig('current_vs_concentration.pdf')
