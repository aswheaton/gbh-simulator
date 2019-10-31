import matplotlib.pyplot as plt

from Particle import Particle

class GBH_Simulation(object):
    """docstring for GBH_Simulation."""
    def __init__(self):

    # Updates the list of densities to reflect current particle positions.
    def update_densities(self):

    # Gets density at position of a particle due to neighboring particles.
    def get_density(self, position, kernel):
        return(density)

    # Updates the list of force to reflect current particle positions.
    def update_forces(self):
        return()

    # Gets the net force on a particle at a position due to neighboring particles.
    def get_force(self, position):
        return(force)
