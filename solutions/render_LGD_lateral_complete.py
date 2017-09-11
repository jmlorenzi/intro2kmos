from itertools import product

from kmos.cli import main as cli_main
from kmos.types import Action, Condition, Layer, Project, Site, Species


# Project
pt = Project()
pt.set_meta(
    author='Michael Seibt',
    email='michael.seibt@tum.de',
    model_name='LGD_lateral',
    model_dimension=2
)

# Species
pt.add_species(
    Species(name='empty', color='#d3d3d3'),
    Species(name='ion', color='#0000ff', representation="Atoms('Si')"),
    Species(name='source', color='#00ff00', representation="Atoms('Au')"),
    Species(name='drain', color='#ff0000', representation="Atoms('Ag')")
)
pt.species_list.default_species = 'empty'

# Layer and Coordinates
layer = Layer(name='simple_cubic')
layer.add_site(Site(name='hollow', pos='0.5 0.5 0.5'))
pt.add_layer(layer)

center = pt.lattice.generate_coord('hollow')
bottom = pt.lattice.generate_coord('hollow.(0,-1,0)')
top = pt.lattice.generate_coord('hollow.(0,+1,0)')
left = pt.lattice.generate_coord('hollow.(-1,0,0)')
right = pt.lattice.generate_coord('hollow.(+1,0,0)')

# Parameters
pt.add_parameter(name='E0', value=0.5)
pt.add_parameter(name='T', value=300)
pt.add_parameter(name='eps_f', value=0.0, adjustable=True, min=-0.05, max=0.05)
pt.add_parameter(name='e_int', value=0.002, adjustable=True, min=0.00, max=0.01)
pt.add_parameter(name='thetaS', value=1.0, adjustable=True, min=0.0, max=1.0)
pt.add_parameter(name='thetaD', value=0.0, adjustable=True, min=0.0, max=1.0)

# Processes
names = ['top', 'left', 'bottom', 'right']
delta_Es = ['E0', 'E0+eps_f', 'E0', 'E0-eps_f']
coordinates = [top, left, bottom, right]
for coordinate_name, delta_E, coordinate in zip(names, delta_Es, coordinates):
    for i, conf in enumerate(product(['empty', 'ion'], repeat=3)):
        diffusion_condition = [
            Condition(species='ion', coord=center),
            Condition(species='empty', coord=coordinate)
        ]
        diffusion_action = [
            Condition(species='ion', coord=coordinate),
            Condition(species='empty', coord=center)
        ]
        temp_coords = coordinates[:]
        temp_coords.remove(coordinate)
        for conf_species, temp_coord in zip(conf, temp_coords):
            diffusion_condition.append(Condition(species=conf_species, coord=temp_coord))

        nns = conf.count('ion')
        pt.add_process(
            name='diffusion_%s_%s' % (coordinate_name, i),
            conditions=diffusion_condition,
            actions=diffusion_action,
            rate_constant='1/(beta*h)*exp(-beta*((%s)-%s*e_int)*eV)' % (delta_E, nns)
        )

        # if left == empty, make another process where condition is left == source
        # important for first step after emission -> otherwise deadlock
        if left in temp_coords:
            left_index = temp_coords.index(left)
            if conf[left_index] == 'empty':
                diffusion_condition = [
                    Condition(species='ion', coord=center),
                    Condition(species='empty', coord=coordinate)
                ]
                for conf_species, temp_coord in zip(conf, temp_coords):
                    if temp_coord == left:
                        conf_species = 'source'
                    diffusion_condition.append(Condition(species=conf_species, coord=temp_coord))

                pt.add_process(
                    name='diffusion_%s_%s_source' % (coordinate_name, i),
                    conditions=diffusion_condition,
                    actions=diffusion_action,
                    rate_constant='1/(beta*h)*exp(-beta*((%s)-%s*e_int)*eV)' % (delta_E, nns)
                )

source_entry_conditions = [
    Condition(species='empty', coord=center),
    Condition(species='source', coord=left)
]
source_exit_conditions = [
    Condition(species='ion', coord=center),
    Condition(species='source', coord=left)
]
pt.add_process(
    name='source_entry',
    conditions=source_entry_conditions,
    actions=source_exit_conditions,
    rate_constant='thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)'
)
pt.add_process(
    name='source_exit',
    conditions=source_exit_conditions,
    actions=source_entry_conditions,
    rate_constant='(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)'
)

drain_entry_conditions = [
    Condition(species='ion', coord=center),
    Condition(species='drain', coord=right)
]
drain_exit_conditions = [
    Action(species='empty', coord=center),
    Action(species='drain', coord=right)
]
pt.add_process(
    name='drain_exit',
    conditions=drain_entry_conditions,
    actions=drain_exit_conditions,
    rate_constant='(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)',
    tof_count={'current': 1}
)

pt.add_process(
    name='drain_entry',
    conditions=drain_exit_conditions,
    actions=drain_entry_conditions,
    rate_constant='thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)',
    tof_count={'current': -1}
)

# Build model
file_name = pt.meta.model_name + '.xml'
pt.save(file_name)
if False:  # build the exported .xml directly
    cli_main('export %s' % file_name)
pt.print_statistics()
