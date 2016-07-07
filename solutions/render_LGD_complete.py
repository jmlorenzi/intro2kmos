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
pt.add_species(name='source', color = '#00ff00',
               representation="Atoms('Au')")
pt.add_species(name='drain', color = '#ff0000',
               representation="Atoms('Ag')")
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
pt.add_parameter(name= 'eps_f', value = 0.0, adjustable=True, min = -0.05, max=0.05)

pt.add_parameter(name= 'thetaS', value=1.0, adjustable=True, min=0.0, max=1.0)
pt.add_parameter(name= 'thetaD', value=0.0, adjustable=True, min=0.0, max=1.0)

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
               rate_constant='1/(beta*h)*exp(-beta*(E0+eps_f)*eV)')

pt.add_process(name='diffusion_right',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='empty', coord=right)],
               actions=[Action(species='ion', coord=right),
                        Action(species='empty', coord=center)],
               rate_constant='1/(beta*h)*exp(-beta*(E0-eps_f)*eV)')

pt.add_process(name='source_entry',
               conditions=[Condition(species='empty', coord=center),
                           Condition(species='source', coord=left)],
               actions=[Action(species='ion', coord=center),
                        Action(species='source', coord=left)],
               rate_constant='thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)')

pt.add_process(name='source_exit',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='source', coord=left)],
               actions=[Action(species='empty', coord=center),
                        Action(species='source', coord=left)],
               rate_constant='(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)')

pt.add_process(name='drain_exit',
               conditions=[Condition(species='ion', coord=center),
                           Condition(species='drain', coord=right)],
               actions=[Action(species='empty', coord=center),
                        Action(species='drain', coord=right)],
               rate_constant='(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)',
               tof_count = {
                   # 'exit' : 1,
                   'current' : 1
                   },
               )

pt.add_process(name='drain_entry',
               conditions=[Condition(species='empty', coord=center),
                           Condition(species='drain', coord=right)],
               actions=[Action(species='ion', coord=center),
                        Action(species='drain', coord=right)],
               rate_constant='thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)',
               tof_count = {
                   # 'back_entry' : 1,
                   'current' : -1
                   }
                            )

# Export
pt.export_xml_file('LGD.xml')
