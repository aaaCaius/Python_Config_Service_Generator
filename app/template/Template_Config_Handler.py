
# Include Section
import os
from configparser import ConfigParser


# Class Deffinition
class Config_Handler:
    # Self Generated interfaces
    b_Class_Init_flg = False
    str_App_Root_Path = ''
   
    # Imported Objects from Cfg
    # Start: Insert Cfg Objects
    
    
    # Stop: Insert Cfg Objects
    # Methodss
    

    @classmethod
    def Get_str_App_Root_Path(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.str_App_Root_Path

        # Start: Insert Get Methods


        # Stop: Insert Get Methods

        # Class Private Methods:

    @staticmethod
    def Clean_Convert_Boolean(str_value):
        b_return_value = False

        str_value = str_value.replace('/n','')
        str_value = str_value.replace('/s','')

        if str_value == 'True':
            b_return_value = True

        return b_return_value


    @staticmethod
    def Clean_Convert_List_Boolean(str_values):
        lsb_return_values = []
        lstr_values = str_values.split(",")
        for str_element in lstr_values:
            str_element = str_element.replace('/n','')
            str_element = str_element.replace('/s','')

            if str_element == 'True':
                lsb_return_values.append(True)
            else:
                lsb_return_values.append(False)

        return lsb_return_values


    @staticmethod
    def Clean_Convert_Int(i_value):
        i_return_value = 0

        try:
            i_return_value = int(i_value)
        except:
            i_return_value = 0

        return i_return_value


    @staticmethod
    def Clean_Convert_List_Int(str_values):
        lsi_return_values = []
        i_aux = 0
        lstr_values = str_values.split(",")
        for str_element in lstr_values:
            str_element = str_element.replace('/n','')
            str_element = str_element.replace('/s','')

            try:
                i_aux = int(str_element)
            except:
                i_aux = 0

            lsi_return_values.append(i_aux)

        return lsi_return_values


    @staticmethod
    def Clean_Convert_Float(f_value):
        f_return_value = float(0)

        try:
            f_return_value = float(f_value)
        except:
            f_return_value = float(0)

        return f_return_value


    @staticmethod
    def Clean_Convert_List_Float(str_values):
        lsf_return_values = []
        f_aux = float(0)
        lstr_values = str_values.split(",")
        for str_element in lstr_values:
            str_element = str_element.replace('/n','')
            str_element = str_element.replace('/s','')

            try:
                f_aux = float(str_element)
            except:
                f_aux = 0

            lsf_return_values.append(f_aux)

        return lsf_return_values


    @staticmethod
    def Clean_Convert_List_String(str_values):
        lstr_return_values = []
        lstr_return_values = str_values.split(",")
        return lstr_return_values


    @classmethod
    def Import_Config(cls):
        #Creating path to project config file
        cls.str_App_Root_Path = os.path.dirname(os.path.abspath('App'))
        str_cfg_file_path = os.path.join(cls.str_App_Root_Path,"config/config.ini")


        #Import and parse config file
        obj_Proj_Config = ConfigParser()
        obj_Proj_Config.read(str_cfg_file_path)

        # Start: Insert Config Init Vars


        # Stop: Insert Config Init Vars

        cls.b_Class_Init_flg = True



