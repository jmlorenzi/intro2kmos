model_name = 'ion_diffusion_model'
simulation_size = 20
random_seed = 1

def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    #from setup_model import setup_model
    #setup_model(model)
    pass

# Default history length in graph
hist_length = 30

parameters = {
    "E0":{"value":"0.5", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"300", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    }

rate_constants = {
    "diffusion_down":("1/(beta*h)*exp(-beta*E0*eV)", True),
    "diffusion_left":("1/(beta*h)*exp(-beta*E0*eV)", True),
    "diffusion_right":("1/(beta*h)*exp(-beta*E0*eV)", True),
    "diffusion_up":("1/(beta*h)*exp(-beta*E0*eV)", True),
    }

site_names = ['default_a']
representations = {
    "empty":"""""",
    "ion":"""Atoms('Si')""",
    }

lattice_representation = """"""

species_tags = {
    "empty":"""""",
    "ion":"""""",
    }

tof_count = {
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 3)">
    <meta author="Juan M. Lorenzi" debug="0" email="jmlorenzi@gmail.com" model_dimension="2" model_name="ion_diffusion_model"/>
    <species_list default_species="empty">
        <species color="#d3d3d3" name="empty" representation="" tags=""/>
        <species color="#0000ff" name="ion" representation="Atoms('Si')" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="E0" scale="linear" value="0.5"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="T" scale="linear" value="300"/>
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
        <process enabled="True" name="diffusion_left" rate_constant="1/(beta*h)*exp(-beta*E0*eV)">
            <condition coord_layer="default" coord_name="a" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="empty"/>
            <action coord_layer="default" coord_name="a" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="default" coord_name="a" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right" rate_constant="1/(beta*h)*exp(-beta*E0*eV)">
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
    </process_list>
    <output_list/>
</kmc>
"""
