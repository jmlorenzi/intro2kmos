model_name = 'LGD_lateral'
simulation_size = (50, 20)
random_seed = 1


def setup_model(model):
    """Write initialization steps here.
       e.g. ::
    model.put([0,0,0,model.lattice.default_a], model.proclist.species_a)
    """
    x, y = model.size

    for i in xrange(y):
        model._put([x-1, i, 0, 1], model.proclist.drain)
        model._put([0, i, 0, 1], model.proclist.source)
    model._adjust_database()

# Default history length in graph
hist_length = 30

parameters = {
    "E0":{"value":"0.5", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "T":{"value":"300", "adjustable":False, "min":"0.0", "max":"0.0","scale":"linear"},
    "e_int":{"value":"0.002", "adjustable":True, "min":"0.0", "max":"0.01","scale":"linear"},
    "eps_f":{"value":"0.0", "adjustable":True, "min":"-0.05", "max":"0.05","scale":"linear"},
    "thetaD":{"value":"0.0", "adjustable":True, "min":"0.0", "max":"1.0","scale":"linear"},
    "thetaS":{"value":"1.0", "adjustable":True, "min":"0.0", "max":"1.0","scale":"linear"},
    }

rate_constants = {
    "diffusion_bottom_0":("1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)", True),
    "diffusion_bottom_0_source":("1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)", True),
    "diffusion_bottom_1":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_bottom_1_source":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_bottom_2":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_bottom_3":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_bottom_4":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_bottom_4_source":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_bottom_5":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_bottom_5_source":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_bottom_6":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_bottom_7":("1/(beta*h)*exp(-beta*((E0)-3*e_int)*eV)", True),
    "diffusion_left_0":("1/(beta*h)*exp(-beta*((E0+eps_f)-0*e_int)*eV)", True),
    "diffusion_left_1":("1/(beta*h)*exp(-beta*((E0+eps_f)-1*e_int)*eV)", True),
    "diffusion_left_2":("1/(beta*h)*exp(-beta*((E0+eps_f)-1*e_int)*eV)", True),
    "diffusion_left_3":("1/(beta*h)*exp(-beta*((E0+eps_f)-2*e_int)*eV)", True),
    "diffusion_left_4":("1/(beta*h)*exp(-beta*((E0+eps_f)-1*e_int)*eV)", True),
    "diffusion_left_5":("1/(beta*h)*exp(-beta*((E0+eps_f)-2*e_int)*eV)", True),
    "diffusion_left_6":("1/(beta*h)*exp(-beta*((E0+eps_f)-2*e_int)*eV)", True),
    "diffusion_left_7":("1/(beta*h)*exp(-beta*((E0+eps_f)-3*e_int)*eV)", True),
    "diffusion_right_0":("1/(beta*h)*exp(-beta*((E0-eps_f)-0*e_int)*eV)", True),
    "diffusion_right_0_source":("1/(beta*h)*exp(-beta*((E0-eps_f)-0*e_int)*eV)", True),
    "diffusion_right_1":("1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)", True),
    "diffusion_right_1_source":("1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)", True),
    "diffusion_right_2":("1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)", True),
    "diffusion_right_3":("1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)", True),
    "diffusion_right_4":("1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)", True),
    "diffusion_right_4_source":("1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)", True),
    "diffusion_right_5":("1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)", True),
    "diffusion_right_5_source":("1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)", True),
    "diffusion_right_6":("1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)", True),
    "diffusion_right_7":("1/(beta*h)*exp(-beta*((E0-eps_f)-3*e_int)*eV)", True),
    "diffusion_top_0":("1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)", True),
    "diffusion_top_0_source":("1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)", True),
    "diffusion_top_1":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_top_1_source":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_top_2":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_top_2_source":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_top_3":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_top_3_source":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_top_4":("1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)", True),
    "diffusion_top_5":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_top_6":("1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)", True),
    "diffusion_top_7":("1/(beta*h)*exp(-beta*((E0)-3*e_int)*eV)", True),
    "drain_entry":("thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)", True),
    "drain_exit":("(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)", True),
    "source_entry":("thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)", True),
    "source_exit":("(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)", True),
    }

site_names = ['simple_cubic_hollow']
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
<kmc version="(0, 3)">
    <meta author="Michael Seibt" debug="0" email="michael.seibt@tum.de" model_dimension="2" model_name="LGD_lateral"/>
    <species_list default_species="empty">
        <species color="#ff0000" name="drain" representation="Atoms('Ag')" tags=""/>
        <species color="#d3d3d3" name="empty" representation="" tags=""/>
        <species color="#0000ff" name="ion" representation="Atoms('Si')" tags=""/>
        <species color="#00ff00" name="source" representation="Atoms('Au')" tags=""/>
    </species_list>
    <parameter_list>
        <parameter adjustable="False" max="0.0" min="0.0" name="E0" scale="linear" value="0.5"/>
        <parameter adjustable="False" max="0.0" min="0.0" name="T" scale="linear" value="300"/>
        <parameter adjustable="True" max="0.01" min="0.0" name="e_int" scale="linear" value="0.002"/>
        <parameter adjustable="True" max="0.05" min="-0.05" name="eps_f" scale="linear" value="0.0"/>
        <parameter adjustable="True" max="1.0" min="0.0" name="thetaD" scale="linear" value="0.0"/>
        <parameter adjustable="True" max="1.0" min="0.0" name="thetaS" scale="linear" value="1.0"/>
    </parameter_list>
    <lattice cell_size="1.0 0.0 0.0 0.0 1.0 0.0 0.0 0.0 1.0" default_layer="simple_cubic" representation="" substrate_layer="simple_cubic">
        <layer color="#ffffff" name="simple_cubic">
            <site default_species="default_species" pos="0.5 0.5 0.5" tags="" type="hollow"/>
        </layer>
    </lattice>
    <process_list>
        <process enabled="True" name="diffusion_bottom_0" rate_constant="1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_0_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_1" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_1_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_2" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_3" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_4" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_4_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_5" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_5_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_6" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_bottom_7" rate_constant="1/(beta*h)*exp(-beta*((E0)-3*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_0" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_1" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_2" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_3" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_4" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_5" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_6" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_left_7" rate_constant="1/(beta*h)*exp(-beta*((E0+eps_f)-3*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_0" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_0_source" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_1" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_1_source" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_2" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_3" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_4" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_4_source" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_5" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_5_source" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_6" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_right_7" rate_constant="1/(beta*h)*exp(-beta*((E0-eps_f)-3*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_0" rate_constant="1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_0_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-0*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_1" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_1_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_2" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_2_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_3" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_3_source" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_4" rate_constant="1/(beta*h)*exp(-beta*((E0)-1*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_5" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_6" rate_constant="1/(beta*h)*exp(-beta*((E0)-2*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="diffusion_top_7" rate_constant="1/(beta*h)*exp(-beta*((E0)-3*e_int)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 -1 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 1 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
        </process>
        <process enabled="True" name="drain_entry" rate_constant="thetaD*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)" tof_count="{'current': -1}">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="drain"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="drain"/>
        </process>
        <process enabled="True" name="drain_exit" rate_constant="(1-thetaD)*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)" tof_count="{'current': 1}">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="drain"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="1 0 0" species="drain"/>
        </process>
        <process enabled="True" name="source_entry" rate_constant="thetaS*1/(beta*h)*exp(-beta*(E0-eps_f)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
        </process>
        <process enabled="True" name="source_exit" rate_constant="(1-thetaS)*1/(beta*h)*exp(-beta*(E0+eps_f)*eV)">
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="ion"/>
            <condition coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="0 0 0" species="empty"/>
            <action coord_layer="simple_cubic" coord_name="hollow" coord_offset="-1 0 0" species="source"/>
        </process>
    </process_list>
    <output_list/>
</kmc>
"""
