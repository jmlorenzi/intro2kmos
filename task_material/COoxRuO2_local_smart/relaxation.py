#!/usr/bin/env python

from kmos.run import KMC_Model
import pylab
import numpy as np

#load model
model = KMC_Model(print_rates=False, banner=False)

#set pressures and temperature
model.parameters.T = 450
model.parameters.p_COgas = 1
model.parameters.p_O2gas = 1

#prepare initial state of system with all bridge sites covered by O
#for i in range(model.size[0]):
#  for j in range(model.size[1]):
#    model._put([i,j,0,model.lattice.ruo2_bridge], model.proclist.o)
#model._adjust_database()

#get TOF labels
tof_labels = model.get_tof_header().split(' ')

#get coverage labels
cov_labels = model.get_occupation_header().split(' ')

#Number of kmc steps taken in each sample
sample_step = 1e5

#Number of samples
N = 100

#prepare arrays for TOFs, coverages and kmc steps
tofs = np.zeros((N,len(tof_labels)))
covs = np.zeros((N,len(cov_labels)))
steps = np.zeros((N,1))

#run model and save data
for i in range(N):
  atoms = model.get_atoms(geometry=False)
  tof = atoms.tof_integ
  tofs[i,:] = tof
  cov = atoms.occupation
  covs[i,:] = cov.flatten()
  step = atoms.kmc_step
  steps[i] = step
  model.do_steps(sample_step)

#prepare figure and plot colors
fig = pylab.figure()
colors = ["#0065bd","#a2ad00","#e37222","#B452CD","#dad7cb","#000000","r"]

#plot TOFs
ax = fig.add_subplot(2,1,1)
for i in range(len(tof_labels)):
    ax.plot(steps, tofs[:,i], color=colors[i], label='CO2')
ax.set_xlabel('kmc steps')
ax.set_ylabel(ur'TOF (s$^{-1}$site$^{-1}$)')
#pylab.ylim([0,5])
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.legend(bbox_to_anchor=(1, 0.916), bbox_transform=pylab.gcf().transFigure)

#plot covs
ax2 = fig.add_subplot(2,1,2)
for i in range(len(cov_labels)):
    ax2.plot(steps, covs[:,i], color=colors[i], label=cov_labels[i].replace('_ruo2','').replace('bridge','br').replace('empty','*'))
ax2.set_xlabel('kmc steps')
ax2.set_ylabel('Coverage (ML)')
pylab.ylim([-0.05,1.05])
box = ax2.get_position()
ax2.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax2.legend(bbox_to_anchor=(1, 0.48), bbox_transform=pylab.gcf().transFigure)

#save plot
pylab.subplots_adjust(left=0.1, right=0.8, top=0.97)
pylab.savefig('relaxation.pdf', dpi=300)

