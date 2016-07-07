model_name = 'ion_diffusion_model'
simulation_size = (50, 20)
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    lx = model.size[0]
    ly = model.size[1]

    for iy in xrange(ly):
        model._put([0,iy,0,1], model.proclist.source)
        model._put([lx-1,iy,0,1], model.proclist.drain)
    model._adjust_database()

# Default history length in graph
hist_length = 30

parameters = {
    "E0":{"value":"0.5", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"300", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "eps_f":{"value":"0.0", "adjustable":True, "min":"-0.05", "max":"0.05","scale":"linear"},
    "eps_int":{"value":"0.0", "adjustable":True, "min":"0.0", "max":"0.2","scale":"linear"},
    "thetaD":{"value":"0.0", "adjustable":True, "min":"0.0", "max":"1.0","scale":"linear"},
    "thetaS":{"value":"1.0", "adjustable":True, "min":"0.0", "max":"1.0","scale":"linear"},
    }

rate_constants = {
    "diffusion_down":("1/(beta*h)*exp(-beta*E0*eV)", True),
    "diffusion_left":("1/(beta*h)*exp(-beta*(E0+eps_f)*eV)", True),
    "diffusion_right":("1/(beta*h)*exp(-beta*(E0-eps_f)*eV)", True),
    "diffusion_up":("1/(beta*h)*exp(-beta*E0*eV)", True),
    "drain_entry":("thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)", True),
    "drain_exit":("(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)", True),
    "source_entry":("thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)", True),
    "source_exit":("(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)", True),
    }

site_names = ['default_a']
representations = {
    "drain":"""Atoms('Ag')""",
    "empty":"""""",
    "ion":"""Atoms('Si')""",
    "source":"""Atoms('Au')""",
    }

lattice_representation = """"""

species_tags = {
    "drain":"""""",
    "empty":"""""",
    "ion":"""""",
    "source":"""""",
    }

tof_count = {
    "drain_entry":{'current': -1},
    "drain_exit":{'current': 1},
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 2)">
    <meta author="Juan M. Lorenzi" debug="0" email="jmlorenzi@gmail.com" model_dimension="2" model_name="ion_diffusion_model"/>
    <species_list default_species="empty">
        <species color="#ff0000" name="drain" representation="Atoms('Ag')" tags=""/>
        <species color="#d3d3d3" name="empty" representation="" tags=""/>
        <species color="#0000ff" name="ion" representation="Atoms('Si')" tags=""/>
        <species color="#00ff00" name="source" representation="Atoms('Au')" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="E0" scale="linear" value="0.5"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="T" scale="linear" value="300"/>
        <parameter adjustable="True" max="0.05" min="-0.05" name="eps_f" scale="linear" value="0.0"/>
        <parameter adjustable="True" max="0.2" min="0.0" name="eps_int" scale="linear" value="0.0"/>
        <parameter adjustable="True" max="1.0" min="0.0" name="thetaD" scale="linear" value="0.0"/>
        <parameter adjustable="True" max="1.0" min="0.0" name="thetaS" scale="linear" value="1.0"/>
    </parameter_list>
    <lattice cell_size="3.0 0.0 0.0 0.0 3.0 0.0 0.0 0.0 3.0" default_layer="default" representation="" substrate_layer="default">
        <layer color="#ffffff" name="default">
            <site default_species="empty" pos="0.5 0.5 0.5" tags="" type="a"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="diffusion_down" rate_constant="1/(beta*h)*exp(-beta*E0*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left" rate_constant="1/(beta*h)*exp(-beta*(E0+eps_f)*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right" rate_constant="1/(beta*h)*exp(-beta*(E0-eps_f)*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_up" rate_constant="1/(beta*h)*exp(-beta*E0*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="0 1 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="drain_entry" rate_constant="thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)" tof_count="{'current': -1}">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="a" coord_offset="1 0 0" species="drain"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="1 0 0" species="drain"/>
        </process>
        <process enabled="True" name="drain_exit" rate_constant="(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)" tof_count="{'current': 1}">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="1 0 0" species="drain"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="1 0 0" species="drain"/>
        </process>
        <process enabled="True" name="source_entry" rate_constant="thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="source"/>
        </process>
        <process enabled="True" name="source_exit" rate_constant="(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="source"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
