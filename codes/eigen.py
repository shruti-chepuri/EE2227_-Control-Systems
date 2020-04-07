import numpy as np
m = np.matrix([[0, 1, 0],
               [0, 0, 1],
               [-1, -2, -3]])

eigenvalues = np.linalg.eigvals(m)
print('The eigenvalues are:')
print eigenvalues
print("Roots of the the polynomial:")
print(np.roots([1, 3, 2,1]))
