"""
Simple lattice gas particle diffusion model
"""
from kmos.types import *

pt = Project()
# Meta information
pt.set_meta(author='Juan M. Lorenzi',
            email='jmlorenzi@gmail.com',
            model_name='ion_diffusion_model',
            model_dimension=2)

# Species
pt.add_species(name='empty', color='#d3d3d3')
pt.add_species(name='ion', color = '#0000ff',
               representation="Atoms('Si')")
pt.species_list.default_species = 'empty'

# Layers
layer = Layer(name='default')
layer.sites.append(Site(name='a', pos='0.5 0.5 0.5',
                        default_species='empty'))
pt.add_layer(layer)
pt.lattice.cell = np.diag([3, 3, 3])

# Parameters
pt.add_parameter(name= 'E0', value = 0.5)
pt.add_parameter(name='T', value = 300)

# Coords
center = pt.lattice.generate_coord('a.(0,0,0).default')

up = pt.lattice.generate_coord('a.(0,1,0).default')
down = pt.lattice.generate_coord('a.(0,-1,0).default')

left = pt.lattice.generate_coord('a.(-1,0,0).default')
right = pt.lattice.generate_coord('a.(1,0,0).default')

# Processes
pt.add_process(name='diffusion_up',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=up)],
               actions=[Action(species='ion', coord=up),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

pt.add_process(name='diffusion_down',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=down)],
               actions=[Action(species='ion', coord=down),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

pt.add_process(name='diffusion_left',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=left)],
               actions=[Action(species='ion', coord=left),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

pt.add_process(name='diffusion_right',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=right)],
               actions=[Action(species='ion', coord=right),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*E0*eV)')

# Export
pt.export_xml_file('LGD.xml')
