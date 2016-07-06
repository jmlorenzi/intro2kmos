#!/usr/bin/env python

from kmos.run import KMC_Model
import pylab
import numpy as np
import random
from ase.all import view

#load model
model = KMC_Model(print_rates=False, banner=False)

#set pressures and temperature
model.parameters.T = 450
model.parameters.p_COgas = 1
model.parameters.p_O2gas = 1

#prepare random initial state of system based on initial guess of species coverages.
#the initial guess could be the coverages obtained in a mean-field (rate equations) model.

#get coverage labels, disregarding the empty species
Nsite_types = model.lattice.spuck
cov_labels = model.get_occupation_header().split(' ')[:-Nsite_types]

#define guess coverages
guess_coverages = [0.25, 0.15, 0.35, 0.55] #CO_br, CO_cus, O_br, O_cus

#dictionaries for converting to kmos variables
kmos_species = {'CO':model.proclist.co, 'O':model.proclist.o}
kmos_sites = {'bridge':model.lattice.ruo2_bridge, 'cus':model.lattice.ruo2_cus}

#available sites
sites_list = []
for i in range(model.size[0]):
    for j in range(model.size[1]):
        sites_list.append([i,j])

#convert coverages to occupations
nsites = model.size[0]*model.size[1]
occupations = {'bridge':[],'cus':[]}
for cov,label in zip(guess_coverages,cov_labels):
    ads = label.split('_')[0]
    site = label.split('_')[2]
    if float(cov) < 1./nsites:
        pass
    else:
        Nsites = int(np.floor(float(cov)*nsites))
        occupations[site].append((ads,Nsites))

#populate the lattice
for key, value in occupations.iteritems():
    available_sites = sites_list[:]
    for ads,Nsites in value:
        site = kmos_sites[key]
        species = kmos_species[ads]
        chosen_sites = random.sample(available_sites, Nsites)
        for elem in chosen_sites:
            model._put(site=[elem[0],elem[1],0,site], new_species=species)
            available_sites.remove(elem)
model._adjust_database()

#check that lattice occupation is as expected
model.print_coverages()
atoms=model.get_atoms()
view(atoms)

#run and plot model as before...

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
pylab.savefig('relaxation_random_initialization.pdf', dpi=300)

