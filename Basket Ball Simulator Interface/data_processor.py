


# data processing class for BBall simulation results

import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt


class data_processor:    
    def __init__(self,data_array):
        print("In data_processor constructor...")
        self.data_array_defined = True
        self.hits_array_defined = False
        self.num_hits_defined = False
        self.data_array = data_array ;
        self.data_shape = list(self.data_array.shape)
        
        self.data_max_indices = []
        self.data_min_indices = []
        for i in range(0,len(self.data_shape)):
            self.data_max_indices.append(self.data_shape[i]-1)
            self.data_min_indices.append(0)
        
        print("Data shape is "+str(self.data_shape))
        self.num_dims = len(self.data_shape)
        self.data_size = self.data_array.size
        
        self.changes_array = np.zeros_like(self.data_array)
        
        self.create_hits_array()
        self.find_num_hits()
        
    def find_num_hits(self):
        print("In find_num_hits...")
        if(self.hits_array_defined==False):
            print("hits_array is not defined!")
            return
        self.num_hits = np.sum(self.hits_array)
        self.num_hits_defined = True
        print("Found "+str(self.num_hits)+" total hits...")
        
    def create_hits_array(self):
        print("In create_hits_array...")
        self.hits_array = self.data_array > 0 
        self.hits_array = self.hits_array.astype(int)
        self.hits_array_defined = True
        
        
    def compute_hits_changes(self,num_elements):
        print("In compute_hits_changes...")
        
        temp_hits = np.pad(self.hits_array,num_elements,'edge')
        temp_changes = np.zeros_like(temp_hits)
        
        for i in range(0,self.num_dims):
            pad_forward_placement = []
            pad_backward_placement = []
            for j in range(0,self.num_dims):
                if(i==j):
                    pad_forward_placement.append([0,num_elements])
                    pad_backward_placement.append([0,num_elements])
                else:
                    pad_forward_placement.append([0,0])
                    pad_backward_placement.append([0,0])
                    
            
            #forward_diff = np.absolute(np.pad(np.diff(temp_hits,num_elements,i),pad_forward_placement,'constant'))
            #backward_diff = np.flip(np.absolute(np.pad(np.diff(np.flip(temp_hits,i),num_elements,i),pad_backward_placement,'constant')),i)
            forward_diff = np.pad(np.absolute(np.diff(temp_hits,num_elements,i)),pad_forward_placement,'constant')
            backward_diff = np.flip(np.pad(np.absolute(np.diff(np.flip(temp_hits,i),num_elements,i)),pad_backward_placement,'constant'),i)
            temp_changes = temp_changes + forward_diff + backward_diff
            
            print("waiting")
                
        for i in range(0,self.num_dims):
            for j in range(0,num_elements):
                temp_changes = np.delete(temp_changes,0,i)
            
            for j in range(0,num_elements):
                this = temp_changes.shape[i]-1
                temp_changes = np.delete(temp_changes,this,i)
            
        self.changes_array[:] = temp_changes[:]
        
        
    def compute_hits_volatility(self,neighborhood_length):
        print("In compute_hits_volatility...")
        self.compute_hits_changes(1)
        
        #convolved_changes = ndimage.convolve(np.square(self.changes_array),weights_matrix,mode='nearest')
        convolved_changes = ndimage.convolve(self.changes_array,self.conv_weights_matrix,mode='nearest')
        
        self.convolved_changes = convolved_changes
        print("done with image convolve...")
        
    def compute_sobel_edges(self):
        print("In compute_sobel_edges...")
        self.sobel_edges = ndimage.sobel(self.hits_array,mode='nearest')
        
    def create_convolution_distance_matrix(self,neighborhood_length):
        print("In create_convolution_distance_matrix...")
        weights_shape = []
        mesh_grid_vectors = []
        weights_width = neighborhood_length*2+1
        for i in range(0,self.num_dims):
            weights_shape.append(weights_width)
            mesh_grid_vectors.append(np.arange(0,weights_width))
            
        weights_shape = tuple(weights_shape)
        mesh_grid = np.meshgrid(*mesh_grid_vectors)
        mesh_grid = np.asarray(mesh_grid)
        mesh_grid = np.abs(mesh_grid-neighborhood_length)
        
        weights_distances = np.zeros(weights_shape)
        for i in range(0,mesh_grid.shape[0]):
            weights_distances[:] = weights_distances[:] + np.square(mesh_grid[i,:])
        
        weights_distances = np.sqrt(weights_distances)
        
        return weights_distances
        
        
    def create_gaussian_weights(self,neighborhood_length,sigma,multiplier):
        
        distances = self.create_convolution_distance_matrix(neighborhood_length)
        
        weights = multiplier/(sigma*np.sqrt(2*3.141593)) * np.exp(-1/2 * np.square(distances/sigma))
        
        self.conv_weights_matrix = np.copy(weights)
        
    def create_linear_weights(self,neighborhood_length,maximum,minimum):
        
        distances = self.create_convolution_distance_matrix(neighborhood_length)
        
        slope = (maximum-minimum)/neighborhood_length
        
        weights = maximum - distances*slope
        
        self.conv_weights_matrix = np.copy(weights)
        
    def create_power_weights(self,neighborhood_length,power,maximum,minimum):
        
        distances = self.create_convolution_distance_matrix(neighborhood_length)
        
        weights = np.zeros(1) # placeholder for now
        
        self.conv_weights_matrix = np.copy(weights)
        
        
if __name__=="__main__":
    example_data1 = [[0,0,0,0,0],
                     [0,1,0,1,0],
                     [0,0,1,0,0],
                     [0,1,0,1,0],
                     [0,0,0,0,0]]
    
    example_data1b = [[0,0,0,0,0,0,0,0],
                      [0,1,0,1,0,0,0,0],
                      [0,0,1,0,0,0,0,0],
                      [0,1,0,1,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]
    
    example_data2 = [[0,1,1,0,1,0,0,0,0,0],
                     [0,1,1,0,1,0,0,1,1,0],
                     [0,0,0,0,0,0,0,1,1,0],
                     [0,0,0,0,0,0,0,1,1,0],
                     [1,0,1,1,1,0,1,0,1,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,1,1,1,1],
                     [0,0,0,0,0,0,0,1,1,0]]
    
    
    rand_data = np.random.random((1000,1000)) > 0.99
    #rand_data = np.random.normal(0,1.0,(1000,1000))>2.0
    rand_data = rand_data.astype(int)
    
    example_data1 = np.asarray(example_data1,dtype=int)
    example_data1b = np.asarray(example_data1b,dtype=int)
    example_data2 = np.asarray(example_data2,dtype=int)
    
    plt.imshow(rand_data, cmap='hot', interpolation='nearest')
    plt.show()
    
    dataProcessor1 = data_processor(rand_data)
    
    dataProcessor1.compute_hits_changes(1)
    dataProcessor1.compute_hits_volatility(1)
    plt.imshow(dataProcessor1.changes_array, cmap='hot', interpolation='nearest')
    plt.show()
    
    plt.imshow(dataProcessor1.convolved_changes, cmap='hot', interpolation='nearest')
    plt.show()
    
    print("finished")
        


