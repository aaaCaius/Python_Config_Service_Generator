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

   ## Categroty1 ## - Marker comment, Just a Note, Not need to be genereated
   b_Categoty1_Switch = False
   lsb_Categoty1_Switches = ''
   i_Categoty1_Generic_Number = 0
   f_Categoty1_Generic_Float_Number = 0.0
   str_Categoty1_Generic_Text = ''
   lsi_Categoty1_Generic_Array = []
   lsf_Categoty1_Generic_Float_Array = []
   lstr_Categoty1_Generic_Text_List = []

   ## Categroty2 ## - Marker comment, Just a Note, Not need to be genereated

   str_Categoty2_Generic_Text_New_Line = []
   lsi_Categoty2_Generic_Array_New_Line = []
   lsf_Categoty2_Generic_Float_Array_New_Line = []

   lsb_Categoty2_Switches = []

   ## Categroty3 ## - Marker comment, Just a Note, Not need to be genereated

   lsb_Categroty3_Switches = []
   # Stop: Insert Cfg Objects

   # Class Get Methods:
   @classmethod
   def Get_str_App_Root_Path(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_App_Root_Path

   # Start: Insert Get Methods
   ## Categroty1 ## - Marker comment, Just a Note, Not need to be genereated
   @classmethod
   def Get_b_Categoty1_Switch(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.b_Categoty1_Switch

   @classmethod
   def Get_lsb_Categoty1_Switches(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsb_Categoty1_Switches

   @classmethod
   def Get_i_Categoty1_Generic_Number(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.i_Categoty1_Generic_Number

   @classmethod
   def Get_f_Categoty1_Generic_Float_Number(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.f_Categoty1_Generic_Float_Number

   @classmethod
   def Get_str_Categoty1_Generic_Text(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Categoty1_Generic_Text

   @classmethod
   def Get_lsi_Categoty1_Generic_Array(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsi_Categoty1_Generic_Array

   @classmethod
   def Get_lsf_Categoty1_Generic_Float_Array(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsf_Categoty1_Generic_Float_Array

   @classmethod
   def Get_lstr_Categoty1_Generic_Text_List(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lstr_Categoty1_Generic_Text_List

   ## Categroty2 ## - Marker comment, Just a Note, Not need to be genereated

   def Get_str_Categoty2_Generic_Text_New_Line(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.str_Categoty2_Generic_Text_New_Line

   @classmethod
   def Get_lsi_Categoty2_Generic_Array_New_Line(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsi_Categoty2_Generic_Array_New_Line

   @classmethod
   def Get_lsf_Categoty2_Generic_Float_Array_New_Line(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsf_Categoty2_Generic_Float_Array_New_Line

   @classmethod
   def Get_lsb_Categoty2_Switches(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsb_Categoty2_Switches

   ## Categroty3 ## - Marker comment, Just a Note, Not need to be genereated

   def Get_lsb_Categroty3_Switches(cls):
      if cls.Class_Init_sts is False:
         cls.Import_Config()
      return cls.lsb_Categroty3_Switches

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
      cls.b_Categoty1_Switch = cls.Clean_Convert_Boolean(obj_Proj_Config['Categoty1']['b_Switch'])
      cls.lsb_Categoty1_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Categoty1']['lsb_Switches'])
      cls.i_Categoty1_Generic_Number = cls.Clean_Convert_Int(obj_Proj_Config['Categoty1']['i_Generic_Number'])
      cls.f_Categoty1_Generic_Float_Number = cls.Clean_Convert_Float(obj_Proj_Config['Categoty1']['f_Generic_Float_Number'])
      cls.str_Categoty1_Generic_Text = str(obj_Proj_Config['Categoty1']['str_Generic_Text'])
      cls.lsi_Categoty1_Generic_Array = cls.Clean_Convert_List_Int(obj_Proj_Config['Categoty1']['lsi_Generic_Array'])
      cls.lsf_Categoty1_Generic_Float_Array =cls.Clean_Convert_List_Float(obj_Proj_Config['Categoty1']['lsf_Generic_Float_Array'])
      cls.lstr_Categoty1_Generic_Text_List =cls.Clean_Convert_List_String(obj_Proj_Config['Categoty1']['lstr_Generic_Text_List'])


      cls.str_Categoty2_Generic_Text_New_Line = str(obj_Proj_Config['Categoty2']['str_Generic_Text_New_Line'])
      cls.lsi_Categoty2_Generic_Array_New_Line = cls.Clean_Convert_List_Int(obj_Proj_Config['Categoty2']['lsi_Generic_Array_New_Line'])
      cls.lsf_Categoty2_Generic_Float_Array_New_Line = cls.Clean_Convert_List_Float(obj_Proj_Config['Categoty2']['lsf_Generic_Float_Array_New_Line'])
      cls.lsb_Categoty2_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Categoty2']['lsb_Switches'])

      cls.lsb_Categroty3_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Categroty3']['lsb_Switches'])
      # Stop: Insert Config Init Vars


      cls.b_Class_Init_flg = True



