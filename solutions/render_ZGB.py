"""
Generate the ZGB CO oxidation model

Juan M. Lorenzi
TU Munich
June 2016
"""

# First kmos.types
from kmos.types import *

# Initialize the project
pt = Project()

# Set projects metadata
pt.set_meta( author = 'Juan M. Lorenzi',
             email = 'jmlorenzi@gmail.com',
             model_name = 'O2_adsdes',
             model_dimension = 2)

# Define the lattice
layer = Layer(name = 'fcc100')                 # define a layer
site = Site(name = 'hol', pos = '0.5 0.5 0.5') # define a site
layer.sites.append(site)                       # add site to layer
# Add layer to Project
pt.add_layer(layer)

# Define the surface species
pt.add_species(name = 'empty', color='#dddddd')

pt.add_species(name = 'O', color = '#ff0000',
               representation = "Atoms('O',[[0.,0.,0.]])",
               )

pt.add_species(name = 'CO', color = '#0000ff',
               representation = "Atoms('N',[[0.,0.,0.]])",
               )

# Model parameters
pt.add_parameter(name = 'yCO', value = 0.5,
                 adjustable = True, min = 0.0, max = 1.0)

pt.add_parameter(name = 'kfast', value = 1e10, # "Infinite" reaction rate
                 adjustable = False)

pt.add_parameter(name = 'kslow', value = 1e-10, # "Zero" desorption rate
                 adjustable = False)


# Define Processes
#   Generate auxiliary coordinates
center = pt.lattice.generate_coord('hol')
right = pt.lattice.generate_coord('hol.(1,0,0)')
up = pt.lattice.generate_coord('hol.(0,1,0)')
left = pt.lattice.generate_coord('hol.(-1,0,0)')
down = pt.lattice.generate_coord('hol.(0,-1,0)')


# Define single site processes
pt.add_process(name = 'CO_ads',
               conditions = [Condition(coord=center,species='empty'),],
               actions = [Action(coord=center,species='CO')],
               rate_constant = 'yCO')

pt.add_process(name = 'CO_des',
               conditions = [Condition(coord=center,species='CO'),],
               actions = [Action(coord=center,species='empty')],
               rate_constant = 'kslow')


# Define two-site processes programatically
#    O2 ads/des
for i, coord in enumerate([right, up]):
    ads_conds = [Condition(coord=center, species='empty'),
                 Condition(coord=coord, species='empty')]
    ads_acts  = [Action(coord=center, species='O'),
                 Action(coord=coord, species='O')]
    # O2 adsorption
    pt.add_process(name = 'O2_ads_{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = '0.5*(1-yCO)')
    # O2 desorption
    pt.add_process(name = 'O2_des_{:02d}'.format(i),
                   conditions = ads_acts,
                   actions = ads_conds,
                   rate_constant = 'kslow')

#    CO oxidation
for i, coord in enumerate([right, up, left, down]):
    ads_conds = [Condition(coord=center, species='CO'),
                 Condition(coord=coord, species='O')]
    ads_acts  = [Action(coord=center, species='empty'),
                 Action(coord=coord, species='empty')]

    # O2 adsorption
    pt.add_process(name = 'CO_oxi_{:02d}'.format(i),
                   conditions = ads_conds,
                   actions = ads_acts,
                   rate_constant = 'kfast',
                   tof_count = {'CO_oxidation' : 1})

# Save the model to an xml file
pt.save('ZGB.xml')
