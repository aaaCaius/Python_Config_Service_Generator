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

   ## Category1 ## - Marker comment, Just a Note, Not need to be generated
   b_Category1_Switch = False
   lsb_Category1_Switches = ''
   i_Category1_Generic_Number = 0
   f_Category1_Generic_Float_Number = 0.0
   str_Category1_Generic_Text = ''
   lsi_Category1_Generic_Array = []
   lsf_Category1_Generic_Float_Array = []
   lstr_Category1_Generic_Text_List = []

   ## Category2 ## - Marker comment, Just a Note, Not need to be genereated

   str_Category2_Generic_Text_New_Line = []
   lsi_Category2_Generic_Array_New_Line = []
   lsf_Category2_Generic_Float_Array_New_Line = []

   lsb_Category2_Switches = []

   ## Category3 ## - Marker comment, Just a Note, Not need to be genereated

   lsb_Category3_Switches = []
   # Stop: Insert Cfg Objects

   # Class Get Methods:
   @classmethod
   def Get_str_App_Root_Path(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.str_App_Root_Path

   # Start: Insert Get Methods
   ## Category1 ## - Marker comment, Just a Note, Not need to be genereated
   @classmethod
   def Get_b_Category1_Switch(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.b_Category1_Switch

   @classmethod
   def Get_lsb_Category1_Switches(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsb_Category1_Switches

   @classmethod
   def Get_i_Category1_Generic_Number(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.i_Category1_Generic_Number

   @classmethod
   def Get_f_Category1_Generic_Float_Number(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.f_Category1_Generic_Float_Number

   @classmethod
   def Get_str_Category1_Generic_Text(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.str_Category1_Generic_Text

   @classmethod
   def Get_lsi_Category1_Generic_Array(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsi_Category1_Generic_Array

   @classmethod
   def Get_lsf_Category1_Generic_Float_Array(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsf_Category1_Generic_Float_Array

   @classmethod
   def Get_lstr_Category1_Generic_Text_List(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lstr_Category1_Generic_Text_List

   ## Category2 ## - Marker comment, Just a Note, Not need to be genereated

   def Get_str_Category2_Generic_Text_New_Line(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.str_Category2_Generic_Text_New_Line

   @classmethod
   def Get_lsi_Category2_Generic_Array_New_Line(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsi_Category2_Generic_Array_New_Line

   @classmethod
   def Get_lsf_Category2_Generic_Float_Array_New_Line(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsf_Category2_Generic_Float_Array_New_Line

   @classmethod
   def Get_lsb_Category2_Switches(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsb_Category2_Switches

   ## Category3 ## - Marker comment, Just a Note, Not need to be genereated

   def Get_lsb_Category3_Switches(cls):
      if cls.b_Class_Init_flg is False:
         cls.Import_Config()
      return cls.lsb_Category3_Switches

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
         str_element = str_element.replace('\n','')
         str_element = str_element.replace('\s','')
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
      str_cfg_file_path = os.path.join(cls.str_App_Root_Path,"Config\\config.ini")

      #Import and parse config file
      obj_Proj_Config = ConfigParser()
      obj_Proj_Config.read(str_cfg_file_path)

      # Start: Insert Config Init Vars
      cls.b_Category1_Switch = cls.Clean_Convert_Boolean(obj_Proj_Config['Category1']['b_Switch'])
      cls.lsb_Category1_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Category1']['lsb_Switches'])
      cls.i_Category1_Generic_Number = cls.Clean_Convert_Int(obj_Proj_Config['Category1']['i_Generic_Number'])
      cls.f_Category1_Generic_Float_Number = cls.Clean_Convert_Float(obj_Proj_Config['Category1']['f_Generic_Float_Number'])
      cls.str_Category1_Generic_Text = str(obj_Proj_Config['Category1']['str_Generic_Text'])
      cls.lsi_Category1_Generic_Array = cls.Clean_Convert_List_Int(obj_Proj_Config['Category1']['lsi_Generic_Array'])
      cls.lsf_Category1_Generic_Float_Array = cls.Clean_Convert_List_Float(obj_Proj_Config['Category1']['lsf_Generic_Float_Array'])
      cls.lstr_Category1_Generic_Text_List = cls.Clean_Convert_List_String(obj_Proj_Config['Category1']['lstr_Generic_Text_List'])

      cls.str_Category2_Generic_Text_New_Line = str(obj_Proj_Config['Category2']['str_Generic_Text_New_Line'])
      cls.lsi_Category2_Generic_Array_New_Line = cls.Clean_Convert_List_Int(obj_Proj_Config['Category2']['lsi_Generic_Array_New_Line'])
      cls.lsf_Category2_Generic_Float_Array_New_Line = cls.Clean_Convert_List_Float(obj_Proj_Config['Category2']['lsf_Generic_Float_Array_New_Line'])
      cls.lsb_Category2_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Category2']['lsb_Switches'])

      cls.lsb_Category3_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Category3']['lsb_Switches'])
      # Stop: Insert Config Init Vars
      
      cls.b_Class_Init_flg = True
