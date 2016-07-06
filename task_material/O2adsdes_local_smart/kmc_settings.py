model_name = 'O2_adsdes'
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
    "kads":{"value":"1.0", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "kdes":{"value":"1.0", "adjustable":True, "min":"0.01", "max":"100.0","scale":"log"},
    }

rate_constants = {
    "O2_ads_0":("0.5*kads", True),
    "O2_ads_1":("0.5*kads", True),
    "O2_des_0":("0.5*kdes", True),
    "O2_des_1":("0.5*kdes", True),
    }

site_names = ['fcc100_hol']
representations = {
    "O":"""Atoms('O', [[0., 0., 0.,]])""",
    "empty":"""""",
    }

lattice_representation = """"""

species_tags = {
    "O":"""""",
    "empty":"""""",
    }

tof_count = {
    }

xml = """<?xml version="1.0" ?>
<kmc version="(0, 3)">
    <meta author="Juan M. Lorenzi" debug="0" email="juan.lorenzi@tum.de" model_dimension="2" model_name="O2_adsdes"/>
    <species_list default_species="empty">
        <species color="#ff0000" name="O" representation="Atoms('O', [[0., 0., 0.,]])" tags=""/>
        <species color="#dddddd" name="empty" representation="" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="kads" scale="linear" value="1.0"/>
        <parameter adjustable="True" max="100.0" min="0.01" name="kdes" scale="log" value="1.0"/>
    </parameter_list>
    <lattice cell_size="1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0" default_layer="fcc100" representation="" substrate_layer="fcc100">
        <layer color="#ffffff" name="fcc100">
            <site default_species="default_species" pos="0.5 0.5 0.0" tags="" type="hol"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="O2_ads_0" rate_constant="0.5*kads">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="O"/>
        </process>
        <process enabled="True" name="O2_ads_1" rate_constant="0.5*kads">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="O"/>
        </process>
        <process enabled="True" name="O2_des_0" rate_constant="0.5*kdes">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="1 0 0" species="empty"/>
        </process>
        <process enabled="True" name="O2_des_1" rate_constant="0.5*kdes">
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="O"/>
            <condition coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="O"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="fcc100" coord_name="hol" coord_offset="0 1 0" species="empty"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
