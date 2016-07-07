from kmos.run import KMC_Model
import random

Ts = [350, 450]
kads = 3e-3
size = (30, 30, 30)
targetML = 4.

nsteps = 100

for i,T in enumerate(Ts):
    random_seed = random.random()*1e12
    model = KMC_Model(banner=False,
                      size = size,
                      random_seed = random_seed)
    model.parameters.T = T
    model.parameters.kads = kads
    tsim = 0.0
    ML = 0.0
    while ML < targetML:
        model.do_steps(nsteps)
        at = model.get_atoms(geometry=False)
        # Convert TOF into ML growth
        ML += at.tof_data[model.tofs.index('Growth')]*at.delta_t*size[2]
    outname = '_'.join(['config', 'T{}'.format(T)] +
                       ['{}'.format(d) for d in model.size])
    model.dump_config(outname)
    print('Finished with T={}K'.format(T))
    print('Deposited {}ML in {} s'.format(
        ML,
        model.base.get_kmc_time()))

    model.deallocate()
