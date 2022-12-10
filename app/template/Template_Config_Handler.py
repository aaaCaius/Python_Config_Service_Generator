
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

	# TEMPLATE section
	str_Template_Add_Config_Vals_Row_Indicator = '\[\t#\s]+Start:\sInsert\sConfig\sInit\sVars'
	str_Template_Add_Class_Methods_Row_Indicator = '[\t#\s]+Start:\sInsert\sGet\sMethods'
	str_Template_Add_Class_Objects_Row_Indicator = '[\t#\s]+Start:\sInsert\sCfg\sObjects'

	# CONFIG_INI section
	str_Config_Ini_List_String_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_List_Float_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_List_Int_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_List_Boolean_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_String_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_Float_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_Int_Regex = '^[A-Z-a-z]{,9999}\_'
	str_Config_Ini_Boolean_Regex = '^[A-Z-a-z]{,9999}\_'

	# ENVIRONMENT section
	str_Environment_Outputs_Config_Handler_Relative_Path = 'outputs/Config_Handler.py'
	str_Environment_Template_Config_Handler_Relative_Path = 'templates/Config_Handler.py'
	str_Environment_Inputs_Config_Ini_Relative_Path = 'inputs/config.ini'
	
	
	# Stop: Insert Cfg Objects
	# Methodss
	

	@classmethod
	def Get_str_App_Root_Path(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_App_Root_Path

		# Start: Insert Get Methods

	@classmethod
	def Get_str_Template_Add_Config_Vals_Row_Indicator(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Template_Add_Config_Vals_Row_Indicator
	@classmethod
	def Get_str_Template_Add_Class_Methods_Row_Indicator(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Template_Add_Class_Methods_Row_Indicator
	@classmethod
	def Get_str_Template_Add_Class_Objects_Row_Indicator(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Template_Add_Class_Objects_Row_Indicator
	@classmethod
	def Get_str_Config_Ini_List_String_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_List_String_Regex
	@classmethod
	def Get_str_Config_Ini_List_Float_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_List_Float_Regex
	@classmethod
	def Get_str_Config_Ini_List_Int_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_List_Int_Regex
	@classmethod
	def Get_str_Config_Ini_List_Boolean_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_List_Boolean_Regex
	@classmethod
	def Get_str_Config_Ini_String_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_String_Regex
	@classmethod
	def Get_str_Config_Ini_Float_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_Float_Regex
	@classmethod
	def Get_str_Config_Ini_Int_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_Int_Regex
	@classmethod
	def Get_str_Config_Ini_Boolean_Regex(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Config_Ini_Boolean_Regex
	@classmethod
	def Get_str_Environment_Outputs_Config_Handler_Relative_Path(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Environment_Outputs_Config_Handler_Relative_Path
	@classmethod
	def Get_str_Environment_Template_Config_Handler_Relative_Path(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Environment_Template_Config_Handler_Relative_Path
	@classmethod
	def Get_str_Environment_Inputs_Config_Ini_Relative_Path(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Environment_Inputs_Config_Ini_Relative_Path

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
		str_cfg_file_path = os.path.join(cls.str_App_Root_Path,"Config/config.ini")


		#Import and parse config file
		obj_Proj_Config = ConfigParser()
		obj_Proj_Config.read(str_cfg_file_path)

		# Start: Insert Config Init Vars

		cls.str_Template_Add_Config_Vals_Row_Indicator = 
		cls.str_Template_Add_Class_Methods_Row_Indicator = 
		cls.str_Template_Add_Class_Objects_Row_Indicator = 
		cls.str_Config_Ini_List_String_Regex = 
		cls.str_Config_Ini_List_Float_Regex = 
		cls.str_Config_Ini_List_Int_Regex = 
		cls.str_Config_Ini_List_Boolean_Regex = 
		cls.str_Config_Ini_String_Regex = 
		cls.str_Config_Ini_Float_Regex = 
		cls.str_Config_Ini_Int_Regex = 
		cls.str_Config_Ini_Boolean_Regex = 
		cls.str_Environment_Outputs_Config_Handler_Relative_Path = 
		cls.str_Environment_Template_Config_Handler_Relative_Path = 
		cls.str_Environment_Inputs_Config_Ini_Relative_Path = 

		# Stop: Insert Config Init Vars

		cls.b_Class_Init_flg = True



