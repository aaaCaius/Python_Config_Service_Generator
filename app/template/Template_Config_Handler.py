
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
    # Methods
    

    @classmethod
    def Get_str_App_Root_Path(cls):
        """
        Get the root path of the app.
        """
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.str_App_Root_Path

        # Start: Insert Get Methods

        # Stop: Insert Get Methods
        # Class Private Methods:


    @staticmethod
    def Clean_Convert_Boolean(str_value):
        """
        Cleans(removes special characters like new line or space) the str_value.
        :param str_value: the string that has to be cleaned.
        :return: a cleaned version of str_value.
        """
        b_return_value = False
        str_value = str_value.replace('/n', '')
        str_value = str_value.replace('/s', '')
        if str_value == 'True':
            b_return_value = True
        return b_return_value


    @staticmethod
    def Clean_Convert_List_Boolean(str_values):
        """
        Cleans(removes special characters like new line or space) the str_values.
        This time this is a list of strings. Actually it is a long string that gets converted into a list of strings.
        :param str_values: the list of strings that has to be cleaned.
        :return: a list containing only clean strings.
        """
        lsb_return_values = []
        lstr_values = str_values.split(",")
        for str_element in lstr_values:
            str_element = str_element.replace('/n', '')
            str_element = str_element.replace('/s', '')
            if str_element == 'True':
                lsb_return_values.append(True)
            else:
                lsb_return_values.append(False)
        return lsb_return_values


    @staticmethod
    def Clean_Convert_Int(i_value):
        """
        Converts a number stored as string into an integer.
        :param i_value: a number stored as string.
        :return: an integer of i_value.
        """
        i_return_value = 0
        try:
            i_return_value = int(i_value)
        except:
            i_return_value = 0
        return i_return_value


    @staticmethod
    def Clean_Convert_List_Int(str_values):
        """
        Converts a list of numbers stored as string into integers.
        :param str_values: a list of numbers stored as string into integers. Actually it is a long string of numbers that
         gets converted into a list of integers.
        :return: a list of integers.
        """
        lsi_return_values = []
        i_aux = 0
        lstr_values = str_values.split(",")
        for str_element in lstr_values:
            str_element = str_element.replace('/n', '')
            str_element = str_element.replace('/s', '')
            try:
                i_aux = int(str_element)
            except:
                i_aux = 0
            lsi_return_values.append(i_aux)
        return lsi_return_values


    @staticmethod
    def Clean_Convert_Float(f_value):
        """
        Converts a float stored as string into an integer.
        :param f_value: float stored as string.
        :return: a float.
        """
        f_return_value = float(0)
        try:
            f_return_value = float(f_value)
        except:
            f_return_value = float(0)
        return f_return_value


    @staticmethod
    def Clean_Convert_List_Float(str_values):
        """
        Converts a list of floats stored as string into an integer. Actually it is a long string of floats that
         gets converted into a list of floats.
        :param str_values: a long string of floats.
        :return: a list of floats.
        """
        lsf_return_values = []
        f_aux = float(0)
        lstr_values = str_values.split(",")
        for str_element in lstr_values:
            str_element = str_element.replace('/n', '')
            str_element = str_element.replace('/s', '')
            str_element = str_element.replace("'","")
            str_element = str_element.replace(" ,",",")
            try:
                f_aux = float(str_element)
            except:
                f_aux = 0
        lsf_return_values.append(f_aux)
        return lsf_return_values


    @staticmethod
    def Clean_Convert_List_String(str_values):
        """
        Cleans(removes special characters like new line or space) from str_values. Actually str_values is a long string
        separated by ","s.
        :param str_values: a long string separated by ",".
        :return: a list of strings.
        """
        lstr_return_values = []
        str_values = str_values.replace('\n','')
        str_values = str_values.replace('\t','')
        str_values = str_values.replace("'","")
        str_values = str_values.replace(' ','')
        str_values = str_values.replace("]", "")
        str_values = str_values.replace("[", "")
        lstr_return_values = str_values.split(",")
        return lstr_return_values


    @staticmethod
    def Clean_Convert_List_of_Lists_String(str_values):
        """
        Cleans(removes special characters like new line or space) from str_values. Actually str_values is a long string
        separated by ","s.
        :param str_values: a long string separated by ",".
        :return: a list of lists of strings.
        """
        aux = []
        lstr_return_values = []
        str_values = str_values.replace('\n','')
        str_values = str_values.replace('\t','')
        str_values = str_values.replace('], [','],[')
        str_values = str_values.replace('[[','')
        str_values = str_values.replace(']]','')
        aux = str_values.split("],[")
        for el in aux:
            el = el.replace("'","")
            el = el.replace(", ",",")
            lstr_return_values.append(el.split(','))
        return lstr_return_values


    @classmethod
    def Import_Config(cls):
    	"""
        Import the config file.
        """
        # Creating path to project config file
        cls.str_App_Root_Path = os.path.dirname(os.path.abspath('App'))
        str_cfg_file_path = os.path.join(cls.str_App_Root_Path,"inputs/config.ini")
       
        # Import and parse config file
        obj_Proj_Config = ConfigParser()
        obj_Proj_Config.read(str_cfg_file_path)

        # Start: Insert Config Init Vars

        # Stop: Insert Config Init Vars

        cls.b_Class_Init_flg = True



