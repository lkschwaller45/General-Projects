
import numpy as np

neighborhood_length = 1 ; 
num_dims = 3 ; 

weights_shape = []
mesh_grid_vectors = []
weights_width = neighborhood_length*2+1
for i in range(0,num_dims):
    weights_shape.append(weights_width)
    mesh_grid_vectors.append(np.arange(0,weights_width))
    
weights_shape = tuple(weights_shape)
mesh_grid = np.meshgrid(*mesh_grid_vectors)
mesh_grid = np.asarray(mesh_grid)
mesh_grid = np.abs(mesh_grid-neighborhood_length)

# gaussian formula is 
# f(x) = 1/(sigma*sqrt(2*pi)) * e^(-1/2 * (x/sigma)^2)

weights_distances = np.zeros(weights_shape)
for i in range(0,mesh_grid.shape[0]):
    weights_distances[:] = weights_distances[:] + np.square(mesh_grid[i,:])

weights_distances = np.sqrt(weights_distances)

sigma = 1.0 ; 
multiplier = 5.0 ; 

weights = multiplier/(sigma*np.sqrt(2*3.141593)) * np.exp(-1/2 * np.square(weights_distances/sigma))

print("done...")
    
