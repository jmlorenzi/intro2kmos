"""
Generate a kmos model for simple crystal growth using
an adsorption-desorption Solid-on-Solid (SOS) model.

Adsorption rate is constant, and desorption rate follow
an Arrhenius like rate, that considers atractive nearest
neighbor interactions

Juan M. Lorenzi
TU Munich
16.05.2016
"""

from kmos.types import *
import itertools

def main():

    pt = Project()

    # Define project meta
    pt.meta.author = 'Juan M. Lorenzi'
    pt.meta.email = 'jmlorenzi@gmail.com'
    pt.meta.model_name = 'SOS_adsdes'
    pt.meta.model_dimension = 3
    pt.meta.debug = 0

    # Add species
    pt.add_species(name='empty', color='#ffffff')
    pt.add_species(name='Pt', color = '#0000ff', representation = "Atoms('Pt')")

    pt.add_species(name='sub', color='#00ff00', representation = "Atoms('Pd')")

    # Add sites and layer
    layer = Layer(name='default')
    layer.sites.append(Site(name='sc'))
    pt.add_layer(layer)

    # Define the unit cell size for better visualization
    pt.layer_list.cell = 2.7*np.eye(3)

    pt.species_list.default_species = 'empty'

    # Parameters
    pt.add_parameter(name='T', value=200, adjustable=True, min=200., max=500.)
    pt.add_parameter(name='kads', value=3e-3, adjustable=True, min = 1e-5, max=1e0, scale='log')

    pt.add_parameter(name='E_des', value=1.0)
    pt.add_parameter(name='E_int', value=0.5)

    # Auxiliary coordinates
    central = pt.lattice.generate_coord('sc')
    up = pt.lattice.generate_coord('sc.(0,0,1)')
    down = pt.lattice.generate_coord('sc.(0,0,-1)')
    xp = pt.lattice.generate_coord('sc.(1,0,0)')
    xm = pt.lattice.generate_coord('sc.(-1,0,0)')
    yp = pt.lattice.generate_coord('sc.(0,1,0)')
    ym = pt.lattice.generate_coord('sc.(0,-1,0)')

    xpd = pt.lattice.generate_coord('sc.(1,0,-1)')
    xmd = pt.lattice.generate_coord('sc.(-1,0,-1)')
    ypd = pt.lattice.generate_coord('sc.(0,1,-1)')
    ymd = pt.lattice.generate_coord('sc.(0,-1,-1)')


    # Processes

    # Adsorption
    condition_list = [ Condition(coord=central, species='empty'),
                       Condition(coord=down, species='Pt')]
    action_list = [Action(coord=central, species='Pt')]

    pt.add_process(name = 'Ads',
                   rate_constant = 'kads',
                   condition_list = condition_list,
                   action_list = action_list,
                   tof_count = {'Adsorption' : 1,
                                'Growth' : 1}
                   )

    # Auxiliary adsorption into substrate
    condition_list = [ Condition(coord=central, species='empty'),
                       Condition(coord=down, species='sub')]
    action_list = [Action(coord=central, species='Pt')]

    pt.add_process(name = 'Ads_sub',
                   rate_constant = 'kads',
                   condition_list = condition_list,
                   action_list = action_list,
                   )


    # Desorption

    conds_base = [ Condition(coord=central, species='Pt'),
                   Condition(coord=up, species='empty'),]

    action_list = [ Condition(coord=central, species='empty') ]

    # We need to consider all possible configurations of
    # the NNs of the central site
    nns = [xp, yp, xm, ym]

    proc_counter = 0
    for conf in itertools.product(['empty', 'Pt'], repeat=len(nns)):
        nr_nns = conf.count('Pt')
        conds_extra = []
        for i, spec in enumerate(conf):
            conds_extra.append(Condition(coord=nns[i], species=spec))

        rate = '1/(beta*h)*exp(-beta*(E_des+{}*E_int)*eV)'.format(nr_nns)
        proc = Process(name = 'Des_{:03d}'.format(proc_counter),
                       condition_list = conds_base + conds_extra,
                       action_list = action_list,
                       rate_constant = rate,
                       tof_count = {'Desorption' : 1,
                                    'Growth' : -1})
        pt.add_process(proc)
        proc_counter += 1


    pt.save('SOS_adsdes.xml')


if __name__ == '__main__':
    main()
