#!/usr/bin/env python

from kmos.run import KMC_Model
import pylab
import numpy as np
import random
from ase.all import view

#load model
model = KMC_Model(print_rates=False, banner=False)

#set pressures and temperature
model.parameters.T = 600
model.parameters.p_COgas = 1
model.parameters.p_O2gas = 1

#prepare random initial state of O-poisoned lattice (known steady-state solution)
#this ensures faster relaxation.

#get coverage labels, disregarding the empty species
Nsite_types = model.lattice.spuck
cov_labels = model.get_occupation_header().split(' ')[:-Nsite_types]

#define guess coverages
guess_coverages = [0.05, 0.05, 0.95, 0.95] #CO_br, CO_cus, O_br, O_cus

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
#model.print_coverages()
#atoms=model.get_atoms()
#view(atoms)

#get DRC for CO adsorption on cus site
process = "CO_adsorption_cus"

#in finite-difference derivative, change rate constant by plus/minus 2%
delta = 0.02

#relax_steps
relax_steps = 1e6

#sample_steps
sample_steps = 1e7

#relax model
model.do_steps(relax_steps)
atoms = model.get_atoms(geometry=False)

#get rate constant
k = float(model.rate_constants(process).split('=')[1][1:-8])

#get initial TOF
k_ini = k*(1-delta)
model.rate_constants.set("CO_adsorption_cus", k_ini)
data = model.get_std_sampled_data(samples=1,sample_size=sample_steps,tof_method="integ")
tof_ini = float(data.split(' ')[3])

#get final TOF
k_fin = k*(1+delta)
model.rate_constants.set("CO_adsorption_cus", k_fin)
data = model.get_std_sampled_data(samples=1,sample_size=sample_steps,tof_method="integ")
tof_fin = float(data.split(' ')[3])

delta_TOF = tof_fin - tof_ini
delta_k = k_fin - k_ini
DRC = (k_ini / tof_ini) * (delta_TOF / delta_k)

print 'delta: ',delta
print 'sample_steps: ',sample_steps
print 'DRC: ',DRC


