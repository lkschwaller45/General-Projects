
# file for creating a class that ties gui2py to the simulation extensions
# the main purpose here is to avoid writing a bunch of code into gui2py, and 
# rather to simply invoke calls to the sim_helper class
#
# for example, if you want to run a parametric study varying 3 parameters at once,
# it makes more sense for the code that creates the parameter space to be interfaced
# with gui2py, rather than directly written in it

from bball2D_pybind import BBall2D
from data_processor import data_processor

import numpy as np
import matplotlib.pyplot as plt
import sys
import operator
import itertools as it
import timeit
import pandas as pd
import os.path
from os import path

class sim_helper :
    
    def __init__(self,sim_mode=None):
        print("Creating sim_helper instance...")
        
        self.sim_mode_defined = False
        
        if sim_mode=="2D":
            self.sim_instance = BBall2D()
            self.sim_mode = "2D"
            self.sim_mode_defined = True
        elif sim_mode=="3D":
            print("No 3D sims implemented yet...")
            self.sim_mode_defined = False
            
        self.timing_every_N_sims = 20 ; 
        
        self.hit_or_miss = []       # hit or miss result for a study or multiple studies 
        self.num_hits = []          # number of total hits in combination of simulations

        self.num_sims = []          # total number of simulations to be ran
        
        self.set_params_constructor_2d = False ; 
        self.set_params_constructor_3d = False ; 
        
    def define_sim_mode(self,sim_mode):
        print("In define_sim_mode...")
        if(not(sim_mode=="2D" or sim_mode=="3D")):
            print("Given sim_mode is not 1D, 2D, or 3D!")
            return
        else:
            self.sim_mode = sim_mode
        
        
    def allocate_result_space(self):
        print("In allocate_result_matrix...")
        self.space_dimensions = 0 
        extent_list = []
        
        num_sims = np.int64(1) ; 
        
        for i in range(0,len(self.param_dict)):
            if(not(self.param_space[i][0]==self.param_space[i][1] or self.param_space[i][2]==0.0) \
                   and not(self.param_space[i][1]-self.param_space[i][0])<self.param_space[i][2]):
                self.space_dimensions = self.space_dimensions+1 
                self.param_numsteps[i] = int((self.param_space[i][1]-self.param_space[i][0])/self.param_space[i][2])
                self.param_extent[i] = self.param_numsteps[i]+1
                extent_list.append(self.param_extent[i])
                num_sims = num_sims*self.param_extent[i]
            else:
                self.param_numsteps[i] = 0
                self.param_extent[i] = 1 
                extent_list.append(self.param_extent[i])
                
                
        extent_tuple = tuple(extent_list)
        
        #results_size = num_sims*sys.getsizeof(bool)/1000000
        self.num_sims = num_sims
        self.timing_every_N_sims = int(self.num_sims/20)
        results_size = num_sims*2/(1000000)
        if(results_size>=500):
            proceed = self.user_proceed_terminal(results_size)
        else:
            proceed = True
            
        if proceed==True :
            self.result_space = np.zeros(extent_tuple,dtype=np.uint16)
            print("result_space created, uses "+str(self.result_space.nbytes/1000000)+" MB")
        else :
            print("result_space not created...")
        
            
        
    def init_param_space(self):
        print("In init_param_space...")
        if self.sim_mode_defined == False : 
            print("Sim mode is not defined!")
            return
        
        if self.sim_mode == "2D" :
            print("sim_mode==2D")
            self.num_params = 5
            self.param_space = np.zeros((self.num_params,3))
            
            self.param_numsteps = np.zeros((self.num_params),dtype=int)
            
            self.param_extent = np.zeros((self.num_params),dtype=int)
            
            self.param_dict = {0:"Launch Omega",
                               1:"Launch X",
                               2:"Launch Y",
                               3:"Launch Angle",
                               4:"Launch Speed"}
            
            self.param_dict_inv = {"Launch Omega":0,
                                   "Launch X":1,
                                   "Launch Y":2,
                                   "Launch Angle":3,
                                   "Launch Speed":4}
            
        elif self.sim_mode == "3D" :
            print("sim_mode==3D, not implemented currently...")
        
    
    def update_param_space(self,param_string,param_start,param_stop=None,param_step=None):
        entry = self.param_dict_inv[param_string]
        self.param_space[entry][0] = param_start
        if(not(param_stop==None) and not(param_step==None)):
            self.param_space[entry][1] = param_stop
            self.param_space[entry][2] = param_step
    
    def user_proceed_terminal(self,results_size):
        print("Expected result space memory use of "+str(results_size)+" MB")
        proceed = input("Would you like to proceed? y/n \n")
        if(proceed=="yes" or proceed=="y" or proceed=="Y"):
            return True
        else:
            return False
        
    def map_param_space(self):
        print("In map_param_space...")
        params_list = []
        for i in range(0,self.num_params):
            if(self.param_extent[i]>1):
                start = self.param_space[i,0]
                stop = self.param_space[i,1]
                ns = self.param_extent[i]
                params_list.append(np.linspace(start,stop,ns))
            else:
                params_list.append(np.asarray([self.param_space[i,0]]))
        
        if(self.sim_mode=="2D"):
            self.sim_params = self.cartesian([params_list[0],params_list[1],params_list[2],params_list[3],params_list[4]])
        elif(self.sim_mode=="3D"):
            print("3D not implemented yet...")
        
        self.param_map = np.copy(self.sim_params)
        
        for i in range(0,self.num_params):
            if(self.param_extent[i]==1):
                self.param_map[:,i] = 0
            elif(self.param_extent[i]>1):
                start = self.param_space[i,0]
                increment = self.param_space[i,2]
                self.param_map[:,i] = (self.param_map[:,i]-start)/increment
                
        self.param_map = self.param_map.astype(int)
            
        
    def print_param_map(self):
        print("In print_param_map...")
        print("sim_params has shape "+str(self.sim_params.shape))
        print("results_space has shape "+str(self.result_space.shape))
        
    def set_timing_every_N_sims(self,N_sims):
        self.timing_every_N_sims = N_sims
        
        
    def run_sims(self):
        print("In run_sims...")
        if(self.sim_mode=="2D"):
            t_start = timeit.default_timer()
            for i in range(0,self.num_sims):
                a = self.param_map[i,0]
                b = self.param_map[i,1]
                c = self.param_map[i,2]
                d = self.param_map[i,3]
                e = self.param_map[i,4]
                temp_array = self.sim_params[i][:]
                self.set_params_2d(temp_array[0],temp_array[1],temp_array[2],temp_array[3],temp_array[4])
                if(i%self.timing_every_N_sims==0):
                    t1 = timeit.default_timer()
                self.result_space[a,b,c,d,e] = self.sim_instance.sim()
                if(i%self.timing_every_N_sims==0):
                    t2 = timeit.default_timer()
                    print("Elapsed time for sim is "+str(t2-t1)+" seconds")
            t_end = timeit.default_timer()
            print("Total elapsed time of " + str(self.num_sims) + " sims is " + str(t_end-t_start) + " seconds")
            
            return self.result_space
            
    def set_params_2d(self,launch_omega,launch_x,launch_y,launch_angle,launch_speed):
        # call the set functions in BBall2D to set the current simulation parameters
        #print("In set_params_2d...")
        self.sim_instance.setLaunchOmega(launch_omega)
        self.sim_instance.setLaunchX(launch_x)
        self.sim_instance.setLaunchY(launch_y)
        self.sim_instance.setLaunchAngle(launch_angle)
        self.sim_instance.setLaunchSpeed(launch_speed)
        
        
    def cartesian(self, arrays, out=None):
        # compute the cartesian product between any number of arrays, 
        # i.e. get every combination of the elements of the arrays, and 
        # return one big array with all these combinations
        # for example, using cartesian on [a,b] and [c,d,e]
        # should yield [[a,c],[a,d],[a,e],[b,c],[b,d],[b,e]]
        arrays = [np.asarray(x) for x in arrays]
        dtype = arrays[0].dtype
    
        n = np.prod([x.size for x in arrays])
        if out is None:
            out = np.zeros([n, len(arrays)], dtype=dtype)
    
        m = int(n / arrays[0].size)
        out[:,0] = np.repeat(arrays[0], m)
        if arrays[1:]:
            self.cartesian(arrays[1:], out=out[0:m,1:])
            for j in range(1, arrays[0].size):
                out[j*m:(j+1)*m,1:] = out[0:m,1:]
        return out

    def jsonify_params(self):
        #This method creates the param file, at the moment it only stores the last ran sim
        from datetime import datetime
        now = datetime.now() # current date and time
        z =pd.DataFrame(simHelper3.param_map)
        if path.exists('params.json')!= True:
            z.to_json(r'params.json')
        else:
            print('hello')
            date_time = now.strftime("%m_%d_%Y_%H_%M_%S")
            z.to_json(date_time +'.json')

    def load_json(self):
        #This method loads the json file, future code should
        print('hi')
        if path.exists('params1.json') == True:
           param_map_df =  pd.read_json(r'params1.json')
           param_map_df  = param_map_df.rename(columns={0: "Launch Omega", 1: "Launch X", 2: "Launch Y",3: "Launch Angle",4: "Launch Speed"})
           param_space_arr = []
           param_space_arr.append(param_map_df['Launch Omega'].max())
           param_space_arr.append(param_map_df['Launch Omega'].min())
           #param_space_arr.append(param_map_df['Launch Omega']
           param_space_arr.append(param_map_df['Launch X'].max())
           param_space_arr.append(param_map_df['Launch X'].min())
           #param_space_arr.append(param_map_df['Launch X']
           param_space_arr.append(param_map_df['Launch Y'].max())
           param_space_arr.append(param_map_df['Launch Y'].min())
           #param_space_arr.append(param_map_df['Launch Y']
           param_space_arr.append(param_map_df['Launch Angle'].max())
           param_space_arr.append(param_map_df['Launch Angle'].min())
          # param_space_arr.append(param_map_df['Launch Angle'])
           param_space_arr.append(param_map_df['Launch Speed'].max())
           param_space_arr.append(param_map_df['Launch Speed'].min())
          # param_space_arr.append(param_map_df['Launch Speed']
           print(param_space_arr)
        else:
            param_map_df = pd.DataFrame()
            print('hi')
        return param_map_df
    
    def generate_graphs(self):
            dataProcessor = data_processor(simHelper3.run_sims())
            desired_slice = 5 # User should input the desired slice; this should be accomplished via line edit
            f,(ax1,ax2,ax3) = plt.subplots(1,3,sharey=False)
            plt.imshow(dataProcessor.hits_array[:,0,0,:,desired_slice], cmap='hot', interpolation='nearest')
            plt.imshow(dataProcessor.hits_array[:,0,0,desired_slice,:], cmap='hot', interpolation='nearest')
            plt.imshow(dataProcessor.hits_array[desired_slice,0,0,:,:], cmap='hot', interpolation='nearest')
            # Legacy code for graphing the heatmap; if result output changes to be more like original txt adapt this
            # plt.imshow(dataProcessor.hits_array[0,0,0,:,:], cmap='hot', interpolation='nearest')
            # def plot_backspin_speed(df ,desired_slice):
            #     df = df[df.angle == desired_slice[2]]
            #     df = df.drop(columns=['index', 'angle', 'useless'])
            #     df = df.drop(df.index[9273:])
            #     result = df.pivot(index='backspin', columns='speed', values='score')
            #     sns.heatmap(result,cmap= 'binary',cbar=False,ax=ax1)
            # def plot_angle_speed(df ,desired_slice):
            #     df = df[df.backspin == desired_slice[0]]
            #     df = df.drop(columns=['index', 'backspin', 'useless'])
            #     result = df.pivot(index='angle', columns='speed', values='score')
            #     sns.heatmap(result,cmap= 'binary',cbar=False,ax=ax2)
            # def plot_angle_backspin(df ,desired_slice):
            #     df = df[df.speed == desired_slice[1]]
            #     df = df.drop(columns=['index', 'speed', 'useless'])
            #     result = df.pivot(index='backspin', columns='angle', values='score')
            #     sns.heatmap(result,cmap= 'binary',cbar=False,ax=ax3)      
            # plot_angle_backspin(df,desired_slice)
            # plot_backspin_speed(df ,desired_slice)
            # plot_angle_speed(df ,desired_slice)
                
            
if __name__ == "__main__":
    

    backspin_ref = 0.0
    backspin_range =1.0
    backspin_min = backspin_ref-backspin_range*0.5
    backspin_max = backspin_ref+backspin_range*0.5
    backspin_step = 0.1
    
    speed_ref = 7.9
    speed_range = 2.0
    speed_min = speed_ref-speed_range*0.5
    speed_max = speed_ref+speed_range*0.5
    speed_step = 0.04
    
    deg2rad = 3.14159265358979/180.0
    
    angle_ref = 59.0*deg2rad
    angle_range = 0.5*deg2rad
    angle_min = angle_ref-angle_range*0.5
    angle_max = angle_ref+angle_range*0.5
    angle_step = 0.008*deg2rad
    
    
    x_ref = 4.191 #meters, free throw line from cpp
    y_ref = 4*0.3048 #meters, from defaults in cpp
    
    simHelper3 = sim_helper("2D")
    simHelper3.load_json()
    simHelper3.init_param_space()
    simHelper3.update_param_space("Launch Omega",backspin_min,backspin_max,backspin_step)
    simHelper3.update_param_space("Launch X",x_ref)
    simHelper3.update_param_space("Launch Y",y_ref)
    simHelper3.update_param_space("Launch Angle",angle_min,angle_max,angle_step)
    simHelper3.update_param_space("Launch Speed",speed_min,speed_max,speed_step)
    simHelper3.allocate_result_space()
    simHelper3.map_param_space()
    simHelper3.jsonify_params()


    dataProcessor = data_processor(simHelper3.run_sims())
    dataProcessor.create_gaussian_weights(7, 2.0, 1.0)
    dataProcessor.compute_hits_volatility(1)
    dataProcessor.compute_sobel_edges()
    plt.imshow(dataProcessor.hits_array[0,0,0,:,:], cmap='hot', interpolation='nearest')
    plt.show()
    plt.imshow(dataProcessor.convolved_changes[0,0,0,:,:], cmap='hot', interpolation='nearest')
    plt.show()
    plt.imshow(dataProcessor.sobel_edges[0,0,0,:,:], cmap='hot', interpolation='nearest')
    plt.show()

