# Include Sesction
import os
from configparser import ConfigParser

# Class Deffinition
class Config_Handler:
   # Self Generated interfaces
   b_Class_Init_flg = False
   str_App_Root_Path = ''

   # Imported Objects from Cfg

   # Start: Insert Cfg Objects

   str_Envirament_Inputs_Config_Ini_Relative_Path = ''
   str_Envirament_Template_Config_Handler_Relative_Path = ''
   str_Envirament_Outputs_Config_Handler_Relative_Path = ''

   str_Config_Ini_Boolean_Regex = ''
   str_Config_Ini_Int_Regex = ''
   str_Config_Ini_Float_Regex = ''
   str_Config_Ini_String_Regex = ''
   str_Config_Ini_List_Boolean_Regex = ''
   str_Config_Ini_List_Int_Regex = ''
   str_Config_Ini_List_Float_Regex = ''
   str_Config_Ini_List_String_Regex = ''
   str_Config_Ini_Section_Regex = ''


   str_Template_Add_Class_Objects_Raw_Indicator = ''
   str_Template_Add_Class_Methods_Raw_Indicator = ''
   str_Template_Add_Config_Vals_Raw_Indicator = ''


   # Stop: Insert Cfg Objects
   # Methodss


   @classmethod
   def Get_str_App_Root_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_App_Root_Path


   # Start: Insert Get Methods

   @classmethod
   def Get_str_Envirament_Inputs_Config_Ini_Relative_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Envirament_Inputs_Config_Ini_Relative_Path

   def Get_str_Envirament_Template_Config_Handler_Relative_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Envirament_Template_Config_Handler_Relative_Path

   def Get_str_Envirament_Outputs_Config_Handler_Relative_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Envirament_Outputs_Config_Handler_Relative_Path

   def Get_str_Config_Ini_Boolean_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_Boolean_Regex

   def Get_str_Config_Ini_Int_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_Int_Regex

   def Get_str_Config_Ini_Float_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_Float_Regex

   def Get_sstr_Config_Ini_String_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_String_Regex

   def Get_str_Config_Ini_List_Boolean_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_List_Boolean_Regex

   def Get_str_Config_Ini_List_Int_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_List_Int_Regex

   def Get_str_Config_Ini_List_Float_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_List_Float_Regex

   def Get_str_Config_Ini_List_String_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_List_String_Regex


   def Get_str_Config_Ini_Section_Regex(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Config_Ini_Section_Regex

   def Get_str_Template_Add_Class_Objects_Raw_Indicator(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Template_Add_Class_Objects_Raw_Indicator

   def Get_str_Template_Add_Class_Methods_Raw_Indicator(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Template_Add_Class_Methods_Raw_Indicator

   def Get_str_Template_Add_Config_Vals_Raw_Indicator(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Template_Add_Config_Vals_Raw_Indicator

   # Stop: Insert Get Methods

   # Class Private Methods:

   @staticmethod
   def Clean_Convert_Boolean(str_value):
      b_retrun_value = False

      str_value = str_value.replace('/n','')
      str_value = str_value.replace('/s','')

      if str_value == 'True':
         b_retrun_value = True

      return b_retrun_value

   @staticmethod
   def Clean_Convert_List_Boolean(str_values):
      lsb_retrun_values = []
      lstr_values = str_values.split(",")
      for str_element in lstr_values:
         str_element = str_element.replace('/n','')
         str_element = str_element.replace('/s','')

         if str_element == 'True':
            lsb_retrun_values.append(True)
         else:
            lsb_retrun_values.append(False)

      return lsb_retrun_values

   @staticmethod
   def Clean_Convert_Int(i_value):
      i_retrun_value = 0

      try:
         i_retrun_value = int(i_value)
      except:
         i_retrun_value = 0

      return i_retrun_value

   @staticmethod
   def Clean_Convert_List_Int(str_values):
      lsi_retrun_values = []
      i_aux = 0
      lstr_values = str_values.split(",")
      for str_element in lstr_values:
         str_element = str_element.replace('/n','')
         str_element = str_element.replace('/s','')

         try:
            i_aux = int(str_element)
         except:
            i_aux = 0

         lsi_retrun_values.append(i_aux)

      return lsi_retrun_values

   @staticmethod
   def Clean_Convert_Float(f_value):
      f_retrun_value = float(0)

      try:
         f_retrun_value = float(f_value)
      except:
         f_retrun_value = float(0)

      return f_retrun_value


   @staticmethod
   def Clean_Convert_List_Float(str_values):
      lsf_retrun_values = []
      f_aux = float(0)
      lstr_values = str_values.split(",")
      for str_element in lstr_values:
         str_element = str_element.replace('/n','')
         str_element = str_element.replace('/s','')

         try:
            f_aux = float(str_element)
         except:
            f_aux = 0

         lsf_retrun_values.append(f_aux)

      return lsf_retrun_values

   @staticmethod
   def Clean_Convert_List_String(str_values):
      lstr_retrun_values = []
      lstr_retrun_values = str_values.split(",")
      return lstr_retrun_values

   @classmethod
   def Import_Config(cls):
      #Creating path to project config file
      cls.str_App_Root_Path = os.path.dirname(os.path.abspath('App'))
      str_cfg_file_path = os.path.join(cls.str_App_Root_Path,"Config\\config.ini")


      #Import and parse config file
      obj_Proj_Config = ConfigParser()
      obj_Proj_Config.read(str_cfg_file_path)


      # Start: Insert Config Init Vars
      cls.str_Envirament_Inputs_Config_Ini_Relative_Path = str(obj_Proj_Config['Envirament']['str_Inputs_Config_Ini_Relative_Path'])
      cls.str_Envirament_Template_Config_Handler_Relative_Path = str(obj_Proj_Config['Envirament']['str_Template_Config_Handler_Relative_Path'])
      cls.str_Envirament_Outputs_Config_Handler_Relative_Path = str(obj_Proj_Config['Envirament']['str_Envirament_Outputs_Config_Handler_Relative_Path'])

      cls.str_Config_Ini_Boolean_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_Boolean_Regex'])
      cls.str_Config_Ini_Int_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_Int_Regex'])
      cls.str_Config_Ini_Float_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_Float_Regex'])
      cls.str_Config_Ini_String_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_String_Regex'])
      cls.str_Config_Ini_List_Boolean_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_List_Boolean_Regex'])
      cls.str_Config_Ini_List_Int_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_List_Int_Regex'])
      cls.str_Config_Ini_List_Float_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_List_Float_Regex'])
      cls.str_Config_Ini_List_String_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_List_String_Regex'])
      cls.str_Config_Ini_Section_Regex = str(obj_Proj_Config['Categoty1']['str_Config_Ini_Section_Regex'])

      cls.str_Template_Add_Class_Objects_Raw_Indicator = str(obj_Proj_Config['Categoty1']['str_Template_Add_Class_Objects_Raw_Indicator'])
      cls.str_Template_Add_Class_Methods_Raw_Indicator = str(obj_Proj_Config['Categoty1']['str_Template_Add_Class_Methods_Raw_Indicator'])
      cls.str_Template_Add_Config_Vals_Raw_Indicator = str(obj_Proj_Config['Categoty1']['str_Template_Add_Config_Vals_Raw_Indicator'])

      # Stop: Insert Config Init Vars


      cls.b_Class_Init_flg = True



