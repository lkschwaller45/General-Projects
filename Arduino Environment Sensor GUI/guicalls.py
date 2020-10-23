
import enviroment_old


class guiBackend(enviroment_old.Ui_MainWindow):
    def __init__(self, guiInstance):
        self.guiInstance = guiInstance
        self.init_signals()


    def init_signals(self):
        print('The following mode is toggeled... ')
        self.humidity = self.guiInstance.Humidity_box.clicked.connect(self.sayhi)
        self.temperature = self.guiInstance.Temp_box.clicked.connect(self.sayhi)
        self.pressure = self.guiInstance.Pressure_box.clicked.connect(self.sayhi)
        self.UVA_intens = self.guiInstance.UVA_Intensity_box.clicked.connect(self.sayhi)
        self.UVB_intens = self.guiInstance.UVB_Intesity_box.clicked.connect(self.sayhi)
        self.UvIndex = self.guiInstance.UVIndex_box.clicked.connect(self.sayhi)
        self.Light_intens = self.guiInstance.LightIntens_box.clicked.connect(self.sayhi)

    def sayhi(self):
        i = 0

        while i < len(self.guiInstance.variablelist):
            if self.guiInstance.variablelist[i].isChecked( ) == True:
                print(i)
                print('checked')

            i+=1

    def plot_graph(self):
        self.variablelist_str = ['Humidity_box', 'Temp_box', 'Pressure_box', 'UVA_Intensity_box',
                             'UVIndex_box', 'LightIntens_box', 'UVB_Intesity_box']