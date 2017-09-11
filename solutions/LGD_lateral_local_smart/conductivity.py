from kmos.run import KMC_Model
import numpy as np
import matplotlib.pyplot as plt

n_relax = 1e7
n_sample = 1e7
eps_f = 0.02
e_int = 0.002
thetas = np.linspace(0.1, 0.9, 9)

# current vs. concentration
currents = []
for theta in thetas:
    model = KMC_Model(banner=False)
    model.parameters.thetaS = theta
    model.parameters.thetaD = theta
    model.parameters.eps_f = eps_f
    model.parameters.e_int = e_int

    model.do_steps(n_relax)
    exit0 = (model.base.get_procstat(model.proclist.drain_exit)
             - model.base.get_procstat(model.proclist.drain_entry))
    t0 = model.base.get_kmc_time()

    model.do_steps(n_sample)
    currents.append((model.base.get_procstat(model.proclist.drain_exit)
                     - model.base.get_procstat(model.proclist.drain_entry)
                     - exit0) / (model.base.get_kmc_time() - t0) / float(model.size[1]))

    model.deallocate()

fig, ax = plt.subplots(1)
ax.plot(thetas, currents, '-o')
ax.set_xlabel('Concentration')
ax.set_ylabel('Current')
ax.grid()
plt.savefig('current_vs_concentration.pdf')
