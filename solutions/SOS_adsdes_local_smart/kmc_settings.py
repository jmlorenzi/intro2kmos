model_name = 'SOS_adsdes'
simulation_size = (20, 20, 30)
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    for ix in xrange(model.size[0]):
        for iy in xrange(model.size[1]):
            model._put([ix,iy,0,model.lattice.default_sc], model.proclist.sub)
            model._put([ix,iy,1,model.lattice.default_sc], model.proclist.pt)
    model._adjust_database()

# Default history length in graph
hist_length = 30

parameters = {
    "E_des":{"value":"1.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "E_int":{"value":"0.5", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"200", "adjustable":True, "min":"200.0", "max":"500.0","scale":"linear"},
    "kads":{"value":"0.003", "adjustable":True, "min":"1e-05", "max":"1.0","scale":"log"},
    }

rate_constants = {
    "Ads":("kads", True),
    "Ads_sub":("kads", True),
    "Des_000":("1/(beta*h)*exp(-beta*(E_des+0*E_int)*eV)", True),
    "Des_001":("1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)", True),
    "Des_002":("1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)", True),
    "Des_003":("1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)", True),
    "Des_004":("1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)", True),
    "Des_005":("1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)", True),
    "Des_006":("1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)", True),
    "Des_007":("1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)", True),
    "Des_008":("1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)", True),
    "Des_009":("1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)", True),
    "Des_010":("1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)", True),
    "Des_011":("1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)", True),
    "Des_012":("1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)", True),
    "Des_013":("1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)", True),
    "Des_014":("1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)", True),
    "Des_015":("1/(beta*h)*exp(-beta*(E_des+4*E_int)*eV)", True),
    }

site_names = ['default_sc']
representations = {
    "Pt":"""Atoms('Pt')""",
    "empty":"""""",
    "sub":"""Atoms('Pd')""",
    }

lattice_representation = """"""

species_tags = {
    "Pt":"""""",
    "empty":"""""",
    "sub":"""""",
    }

tof_count = {
    "Ads":{'Growth': 1, 'Adsorption': 1},
    "Des_000":{'Desorption': 1, 'Growth': -1},
    "Des_001":{'Desorption': 1, 'Growth': -1},
    "Des_002":{'Desorption': 1, 'Growth': -1},
    "Des_003":{'Desorption': 1, 'Growth': -1},
    "Des_004":{'Desorption': 1, 'Growth': -1},
    "Des_005":{'Desorption': 1, 'Growth': -1},
    "Des_006":{'Desorption': 1, 'Growth': -1},
    "Des_007":{'Desorption': 1, 'Growth': -1},
    "Des_008":{'Desorption': 1, 'Growth': -1},
    "Des_009":{'Desorption': 1, 'Growth': -1},
    "Des_010":{'Desorption': 1, 'Growth': -1},
    "Des_011":{'Desorption': 1, 'Growth': -1},
    "Des_012":{'Desorption': 1, 'Growth': -1},
    "Des_013":{'Desorption': 1, 'Growth': -1},
    "Des_014":{'Desorption': 1, 'Growth': -1},
    "Des_015":{'Desorption': 1, 'Growth': -1},
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 2)">
    <meta author="Juan M. Lorenzi" debug="0" email="jmlorenzi@gmail.com" model_dimension="3" model_name="SOS_adsdes"/>
    <species_list default_species="empty">
        <species color="#0000ff" name="Pt" representation="Atoms('Pt')" tags=""/>
        <species color="#ffffff" name="empty" representation="" tags=""/>
        <species color="#00ff00" name="sub" representation="Atoms('Pd')" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="E_des" scale="linear" value="1.0"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="E_int" scale="linear" value="0.5"/>
        <parameter adjustable="True" max="500.0" min="200.0" name="T" scale="linear" value="200"/>
        <parameter adjustable="True" max="1.0" min="1e-05" name="kads" scale="log" value="0.003"/>
    </parameter_list>
    <lattice cell_size="2.7 0.0 0.0 0.0 2.7 0.0 0.0 0.0 2.7" default_layer="default" representation="" substrate_layer="default">
        <layer color="#ffffff" name="default">
            <site default_species="default_species" pos="0.0 0.0 0.0" tags="" type="sc"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="Ads" rate_constant="kads" tof_count="{'Growth': 1, 'Adsorption': 1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 -1" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
        </process>
        <process enabled="True" name="Ads_sub" rate_constant="kads">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 -1" species="sub"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
        </process>
        <process enabled="True" name="Des_000" rate_constant="1/(beta*h)*exp(-beta*(E_des+0*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_001" rate_constant="1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_002" rate_constant="1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_003" rate_constant="1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_004" rate_constant="1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_005" rate_constant="1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_006" rate_constant="1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_007" rate_constant="1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_008" rate_constant="1/(beta*h)*exp(-beta*(E_des+1*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_009" rate_constant="1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_010" rate_constant="1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_011" rate_constant="1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_012" rate_constant="1/(beta*h)*exp(-beta*(E_des+2*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_013" rate_constant="1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_014" rate_constant="1/(beta*h)*exp(-beta*(E_des+3*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="Des_015" rate_constant="1/(beta*h)*exp(-beta*(E_des+4*E_int)*eV)" tof_count="{'Desorption': 1, 'Growth': -1}">
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 0 1" species="empty"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 1 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="-1 0 0" species="Pt"/>
            <condition coord_layer="default" coord_name="sc" coord_offset="0 -1 0" species="Pt"/>
            <action coord_layer="default" coord_name="sc" coord_offset="0 0 0" species="empty"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
