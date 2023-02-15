
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

	# PREDEFINED_TABLE section
	lstr_PREDEFINED_TABLE_Column_Type = []
    lstr_PREDEFINED_TABLE_Table_Columns = []
    lstr_PREDEFINED_TABLE_Table_Names = []

    # CATEGORY3 section
    lsb_Category3_Switches = []
    lsi_Category3_Generci_Array = []

    # CATEGORY2 section
    lsb_Category2_Switches = []
    lsf_Category2_Generic_Float_Array_New_Line = []
    lsi_Category2_Generic_Array_New_Line = []
    str_Category2_Generic_Text_New_Line = ''

    # CATEGORY1 section
    lstr_Category1_Generic_Text_List = []
    lsf_Category1_Generic_Float_Array = []
    lsi_Category1_Generic_Array = []
    str_Category1_Generic_Text = ''
    f_Category1_Generic_Float_Number = 0.0
    i_Category1_Generic_Number = 0
    lsb_Category1_Switches = []
    b_Category1_Switch = False
    
    
    # Stop: Insert Cfg Objects
    # Methodss
    

    @classmethod
    def Get_str_App_Root_Path(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.str_App_Root_Path

        # Start: Insert Get Methods


    @classmethod
    def Get_lstr_PREDEFINED_TABLE_Column_Type(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.lstr_PREDEFINED_TABLE_Column_Type


    @classmethod
    def Get_lstr_PREDEFINED_TABLE_Table_Columns(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
         return cls.lstr_PREDEFINED_TABLE_Table_Columns


    @classmethod
    def Get_lstr_PREDEFINED_TABLE_Table_Names(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.lstr_PREDEFINED_TABLE_Table_Names


    @classmethod
    def Get_lsb_Category3_Switches(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.lsb_Category3_Switches


    @classmethod
    def Get_lsi_Category3_Generci_Array(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.lsi_Category3_Generci_Array


    @classmethod
    def Get_lsb_Category2_Switches(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.lsb_Category2_Switches


    @classmethod
    def Get_lsf_Category2_Generic_Float_Array_New_Line(cls):
        if cls.b_Class_Init_flg is False:
            cls.Import_Config()
        return cls.lsf_Category2_Generic_Float_Array_New_Line


	@classmethod
	def Get_lsi_Category2_Generic_Array_New_Line(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.lsi_Category2_Generic_Array_New_Line
	@classmethod
	def Get_str_Category2_Generic_Text_New_Line(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Category2_Generic_Text_New_Line
	@classmethod
	def Get_lstr_Category1_Generic_Text_List(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.lstr_Category1_Generic_Text_List
	@classmethod
	def Get_lsf_Category1_Generic_Float_Array(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.lsf_Category1_Generic_Float_Array
	@classmethod
	def Get_lsi_Category1_Generic_Array(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.lsi_Category1_Generic_Array
	@classmethod
	def Get_str_Category1_Generic_Text(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.str_Category1_Generic_Text
	@classmethod
	def Get_f_Category1_Generic_Float_Number(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.f_Category1_Generic_Float_Number
	@classmethod
	def Get_i_Category1_Generic_Number(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.i_Category1_Generic_Number
	@classmethod
	def Get_lsb_Category1_Switches(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.lsb_Category1_Switches
	@classmethod
	def Get_b_Category1_Switch(cls):
		if cls.b_Class_Init_flg is False:
			cls.Import_Config()
		return cls.b_Category1_Switch

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
        # cls.str_App_Root_Path = os.path.dirname(os.path.abspath('App'))
		# str_cfg_file_path = os.path.join(cls.str_App_Root_Path,"inputs/config.ini")
       


        #Import and parse config file
        obj_Proj_Config = ConfigParser()
        obj_Proj_Config.read(str_cfg_file_path)

        # Start: Insert Config Init Vars

        cls.lstr_PREDEFINED_TABLE_Column_Type = cls.Clean_Convert_List_String(obj_Proj_Config['PREDEFINED_TABLE']['lstr_column_type'])
        cls.lstr_PREDEFINED_TABLE_Table_Columns = cls.Clean_Convert_List_String(obj_Proj_Config['PREDEFINED_TABLE']['lstr_table_columns'])
        cls.lstr_PREDEFINED_TABLE_Table_Names = cls.Clean_Convert_List_String(obj_Proj_Config['PREDEFINED_TABLE']['lstr_table_names'])
        cls.lsb_Category3_Switches = cls.Clean_Convert_Boolean(obj_Proj_Config['Category3']['lsb_switches'])
        cls.lsb_Category3_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Category3']['lsb_switches'])
        cls.lsi_Category3_Generci_Array = cls.Clean_Convert_List_Int(obj_Proj_Config['Category3']['lsi_generci_array'])
        cls.lsb_Category2_Switches = cls.Clean_Convert_Boolean(obj_Proj_Config['Category2']['lsb_switches'])
        cls.lsb_Category2_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Category2']['lsb_switches'])
        cls.lsf_Category2_Generic_Float_Array_New_Line = cls.Clean_Convert_List_Float(obj_Proj_Config['Category2']['lsf_generic_float_array_new_line'])
        cls.lsi_Category2_Generic_Array_New_Line = cls.Clean_Convert_List_Int(obj_Proj_Config['Category2']['lsi_generic_array_new_line'])
        cls.str_Category2_Generic_Text_New_Line = str(obj_Proj_Config['Category2']['str_generic_text_new_line'])
        cls.lstr_Category1_Generic_Text_List = cls.Clean_Convert_List_String(obj_Proj_Config['Category1']['lstr_generic_text_list'])
        cls.lsf_Category1_Generic_Float_Array = cls.Clean_Convert_List_Float(obj_Proj_Config['Category1']['lsf_generic_float_array'])
        cls.lsi_Category1_Generic_Array = cls.Clean_Convert_List_Int(obj_Proj_Config['Category1']['lsi_generic_array'])
        cls.str_Category1_Generic_Text = str(obj_Proj_Config['Category1']['str_generic_text'])
        cls.f_Category1_Generic_Float_Number = cls.Clean_Convert_Float(obj_Proj_Config['Category1']['f_generic_float_number'])
        cls.i_Category1_Generic_Number = cls.Clean_Convert_Int(obj_Proj_Config['Category1']['i_generic_number'])
        cls.lsb_Category1_Switches = cls.Clean_Convert_Boolean(obj_Proj_Config['Category1']['lsb_switches'])
        cls.lsb_Category1_Switches = cls.Clean_Convert_List_Boolean(obj_Proj_Config['Category1']['lsb_switches'])
        cls.b_Category1_Switch = cls.Clean_Convert_Boolean(obj_Proj_Config['Category1']['b_switch'])

        # Stop: Insert Config Init Vars

        cls.b_Class_Init_flg = True



