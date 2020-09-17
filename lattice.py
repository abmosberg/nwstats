"""
Defines the Lattice class, used for dealing with lattices of a limited size. Used by the Field class.
"""

import numpy as np
from math import floor
import pickle

class Lattice:

    def __init__(self, Na, Nb, vec_a, vec_b, offset):
        # Number of lattice points in the directions of vec_a and vec_b respectively
        self.Na = Na
        self.Nb = Nb

        # The two primitive lattice vectors, and the third vector pointing to nearest neighbor sites in a hexagonal lattice
        self.vec_a = np.array(vec_a)
        self.vec_b = np.array(vec_b)
        self.vec_c = self.vec_a - self.vec_b

        # Coordinates of the (0, 0) lattice point
        self.offset = offset

    def getParams(self):
        """Return a tuple of all relevant parameters"""
        return self.Na, self.Nb, self.vec_a, self.vec_b, self.offset

    def getMinLatticeDist(self):
        """Return magnitude of shortest lattice vector, including vec_c"""
        return min(np.linalg.norm(self.vec_a), np.linalg.norm(self.vec_b), np.linalg.norm(self.vec_c))

    def getMaxLatticeDist(self):
        """Return magnitude of longest lattice vector, including vec_c"""
        return max(np.linalg.norm(self.vec_a), np.linalg.norm(self.vec_b), np.linalg.norm(self.vec_c))

    def getLatticePoints(self):
        """Return a list of coordinates of all points in the lattice"""
        points = []
        for i in range(0, self.Na):
            for j in range(0, self.Nb):
                points.append([ (i-floor(j/2))*self.vec_a[0] + j*self.vec_b[0] + self.offset[0],
                                (i-floor(j/2))*self.vec_a[1] + j*self.vec_b[1] + self.offset[1] ])

        return points

    def getIndices(self, x, y, roundIndices=True):
        """Return the indices of a lattice point with the given coordinates"""
        displacement = np.array([x, y]) - self.offset
        indices = self.decompose(displacement, self.vec_a, self.vec_b)
        if roundIndices:
            rounded = [round(index) for index in indices]
            indices = rounded

        return indices

    def decompose(self, subject, vec_a, vec_b):
        """Decompose a given vector into a linear combination of two other given vectors

        :param subject: the vector to decompose
        :param vec_a, vec_b: the two vectors forming the basis into which the input vector is decomposed
        :return: array containing a and b in the equation a*vec_a + b*vec_b = subject
        """
        x = np.transpose(np.array([vec_a, vec_b]))
        y = np.array(subject)
        ans = np.linalg.solve(x, y)

        return ans

    def save(self, filename):
        """Save the parameters of the lattice"""
        params = [self.Na, self.Nb, self.vec_a, self.vec_b, self.offset]
        pickle.dump(params, open(filename, 'wb'))

def loadLattice(filename):
    """Return a lattice made from parameters in a file"""
    Na, Nb, vec_a, vec_b, offset = pickle.load(open( filename, 'rb'))
    lattice = Lattice(Na, Nb, vec_a, vec_b, offset)

    return lattice
