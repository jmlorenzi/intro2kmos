"""
Use the ModelRunner to generate Arrhenius plot
using kmos

Mie Andersen
TU Munich
July 2017
"""

from kmos.run import ModelRunner, PressureParameter, TemperatureParameter

class ScanKinetics(ModelRunner):
    p_O2gas = PressureParameter(1.e-1)
    T = TemperatureParameter(min=450, max=650, steps=20)
    p_COgas = PressureParameter(2.e-1)
ScanKinetics().run(init_steps=1e7, sample_steps=1e7, cores=4)

