


# MH 1/28/2020
# 
# This module is responsible for creating a backend to the GUI, where code from other modules
# can be linked.

import interface

from sim_helper import sim_helper
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets





class guiBackend(interface.Ui_MainWindow):

    def __init__(self,guiInstance):
        
        self.gui_instance = guiInstance 
        self.sim_helper = sim_helper()
        
        self.all_params_go = False
        
        # complete gui initialization by reading states of important objects
        self.complete_gui_init() 
        
        # initialize all signal connections of gui
        self.init_signal_connections()
        
        # initialize parameter lists in preparation for running sims
        self.init_param_setting_lists()
        
    def complete_gui_init(self):
        self.sim_mode = self.gui_instance.simModeComboBox.currentText()


    def init_signal_connections(self):
        print("In init_signal_connections...")
        self.gui_instance.runSimsPushButton.clicked.connect(self.run_sims)
        self.gui_instance.simModeComboBox.activated.connect(self.change_sim_mode)
        

       
            
    def change_sim_mode(self):
        print("In change_sim_mode...")
        if(self.gui_instance.simModeComboBox.currentText()=="2D"):
            self.sim_mode = "2D"
        elif(self.gui_instance.simModeComboBox.currentText()=="3D"):
            self.sim_mode = "3D"
            
    def update_param_study(self):
        print("In update_param_study...")
        
            
    def run_sims(self):
        print("In run_sims...")
        if(self.all_params_go==False):
            print("all_params_go=False")
            self.all_params_go = True
            self.check_all_params()
        
        if(self.all_params_go==True):
            print("all_params_go=True")
            for i in range(0,len(self.param_mins)):
                self.sim_helper.update_param_space(self.param_setup_strings[i],self.param_mins[i],self.param_maxs[i],self.param_steps[i])
                

            self.sim_helper.run_sims()
            self.sim_helper.jsonify_params()
            self.sim_helper.generate_graphs()

    def check_all_params(self):
        print("In check_all_params...")
        self.check_fixed_check_boxes()
        self.check_min_line_edits()
        self.check_max_line_edits()
        self.check_step_line_edits()
        
    def init_param_setting_lists(self):
        print("In init_check_lists...")
        if(self.sim_mode=="2D"):
            print("sim_mode = 2D")
            self.param_min_line_edit_check_list = [self.gui_instance.backSpinMinimumValueLineEdit,
                                                   self.gui_instance.customDistanceXMinimumLineEdit,
                                                   self.gui_instance.customDistanceYMinimumLineEdit,
                                                   self.gui_instance.shotElevationAngleMinimumValueLineEdit,
                                                   self.gui_instance.speedMinimumValueLineEdit]
            self.param_mins = [None]*len(self.param_min_line_edit_check_list)
            self.param_study = [False]*len(self.param_min_line_edit_check_list)
            self.param_max_line_edit_check_list = [self.gui_instance.backSpinMaximumValueLineEdit,
                                                   self.gui_instance.customDistanceXMaximumLineEdit,
                                                   self.gui_instance.customDistanceYMaximumLineEdit,
                                                   self.gui_instance.shotElevationAngleMaximumValueLineEdit,
                                                   self.gui_instance.speedMaximumValueLineEdit]
            self.param_maxs = [None]*len(self.param_max_line_edit_check_list)
            self.param_step_line_edit_check_list = [self.gui_instance.backSpinStepSizeLineEdit,
                                                    self.gui_instance.customDistanceXStepSizeLineEdit,
                                                    self.gui_instance.customDistanceYStepSizeLineEdit,
                                                    self.gui_instance.shotElevationAngleStepSizeLineEdit,
                                                    self.gui_instance.speedStepSizeLineEdit]
            self.param_steps = [None]*len(self.param_step_line_edit_check_list)
            
            self.param_check_box_list = [self.gui_instance.backSpinFixedCheckBox,
                                         self.gui_instance.customDistanceXFixedCheckBox,
                                         self.gui_instance.customDistanceYFixedCheckBox,
                                         self.gui_instance.shotElevationAngleFixedCheckBox,
                                         self.gui_instance.speedFixedCheckBox]
            
            self.param_setup_strings = ["Launch Omega",
                                        "Launch X",
                                        "Launch Y",
                                        "Launch Angle",
                                        "Launch Speed"]
            
        elif(self.sim_mode=="3D"):
            print("sim_mode = 3D")
        else:
            print("Undefined sim_mode!")
            return
    

    def check_min_line_edits(self):
        print("In check_min_line_edits...")
        for i in range(0,len(self.param_min_line_edit_check_list)):
            try: 
                value = float(self.param_min_line_edit_check_list[i].text())
            except:
                print("Problem converting input value, check minimum input lines.")
                value = None
                self.all_params_go = False

            self.param_mins[i] = value
            
    def check_max_line_edits(self):
        print("In check_max_line_edits...")
        for i in range(0,len(self.param_max_line_edit_check_list)):
            if self.param_study[i]==True :
                try: 
                    value = float(self.param_max_line_edit_check_list[i].text())
                except:
                    print("Problem converting input value, check maximum input lines.")
                    value = None
                    self.all_params_go = False

                self.param_maxs[i] = value
            
    def check_step_line_edits(self):
        print("In check_step_line_edits...")
        for i in range(0,len(self.param_step_line_edit_check_list)):
            if self.param_study[i]==True :
                try: 
                    value = float(self.param_step_line_edit_check_list[i].text())
                except:
                    print("Problem converting input value, check step size input lines.")
                    value = None
                    self.all_params_go = False

                self.param_steps[i] = value
            
    def check_fixed_check_boxes(self):
        print("In check_fixed_check_boxes...")
        for i in range(0,len(self.param_check_box_list)):
            self.param_study[i] = not(self.param_check_box_list[i].isChecked())
            print("self.param_study[i]="+str(self.param_study[i]))

 
            
