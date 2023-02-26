from Components.Apps.run import make_imports
from outputs.Config_Handler_Output import Config_Handler


if __name__ == '__main__':
   # ___________________________________________________________________________________________________________________
   # ___________________________________________________________________________________________________________________
   make_imports()
   Config_Handler.Import_Config()
   print(Config_Handler.lstr_Category1_Generic_Text_List)
   print(Config_Handler.lsf_Category1_Generic_Float_Array)
   print(Config_Handler.lsi_Category1_Generic_Array)
   print(Config_Handler.str_Category1_Generic_Text)
   print(Config_Handler.f_Category1_Generic_Float_Number)
   print(Config_Handler.i_Category1_Generic_Number)
   print(Config_Handler.lsb_Category1_Switches)
   print(Config_Handler.b_Category1_Switch)
