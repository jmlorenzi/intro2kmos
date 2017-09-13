"""Visualize the growth of a run of the SOS model"""
import sys, os
from kmos.run import KMC_Model
from ase.visualize import view

config = os.path.splitext(sys.argv[1])[0]

size = (30, 30, 30)
model = KMC_Model(banner = False, size = size)

model.load_config(config)
at = model.get_atoms()

view(at)
