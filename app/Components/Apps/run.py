import os
from app import root_dir    # This returns the absolute path of the application (\"app")
from configparser import ConfigParser
import re

def make_imports():
    """
    Takes all needed information from app\template\Template_Config_Handler.py
    and creates a new file app\outputs\Config_Handler_Output.py
    """
    # Get the root directory of the app.
    ROOT_DIR = root_dir()

    # Load config file.
    cfg_path = os.path.join(ROOT_DIR, "inputs/config.ini")
    cfg = ConfigParser()
    cfg.read(cfg_path)
    
    # Open Template_Config_Handler.py(tch) and Config_Handler_Output.py(cho) as text.
    tch_path = os.path.join(ROOT_DIR, "template/Template_Config_Handler.py")
    cho_path = os.path.join(ROOT_DIR, "outputs/Config_Handler_Output.py")
    with open(tch_path, "r+") as tch:
        # Get all content from the file
        content = tch.readlines()
        with open(cho_path, "w") as cho:
            cho.writelines(content)
            for i, line in enumerate(content):
                # Get class attributes
                if "# Start: Insert Cfg Objects" in line:
                    for section in range(len(cfg.sections())):
                        content.insert(i + 1, f"\n\t# {cfg.sections()[section].upper()} section\n")
                        for key, value in cfg.items(cfg.sections()[section]):
                            if (key.startswith("b_") or key.startswith("lsb_") or key.startswith("i_")
                                    or key.startswith("f_") or key.startswith("str_") or key.startswith("lsi_")
                                    or key.startswith("lsf_") or key.startswith("lstr_")):
                                regex = re.match(r"^[A-Z-a-z]{,9999}\_", key)
                                key = f"{regex.group(0)}{cfg.sections()[section]}_{key[len(regex.group(0)):].title()}"
                                # Add the key-value pairs as class attributes.
                                if key.startswith("str_"):
                                    content.insert(i + 2, f"\t{key} = ''\n")
                                if key.startswith("i_"):
                                    content.insert(i + 2, f"\t{key} = 0\n")
                                if key.startswith("f_"):
                                    content.insert(i + 2, f"\t{key} = 0.0\n")
                                if (key.startswith("lsi_") or key.startswith("lsf_") or key.startswith("lstr_")
                                    or key.startswith("lsb_")):
                                    content.insert(i + 2, f"\t{key} = []\n")
                                if key.startswith("b_"):
                                    content.insert(i + 2, f"\t{key} = False\n")
                # Create class "get" functions
                if "# Start: Insert Get Methods" in line:
                    for section in range(len(cfg.sections())):
                        for key, value in cfg.items(cfg.sections()[section]):
                            if (key.startswith("b_") or key.startswith("lsb_") or key.startswith("i_")
                                    or key.startswith("f_") or key.startswith("str_") or key.startswith("lsi_")
                                    or key.startswith("lsf_") or key.startswith("lstr_")):
                                regex = re.match(r"^[A-Z-a-z]{,9999}\_", key)
                                key = f"{regex.group(0)}{cfg.sections()[section]}_{key[len(regex.group(0)):].title()}"
                                # Create "get" functions from class attributes.
                                content.insert(i + 2,
                                               f"\t@classmethod\n\tdef Get_{key}(cls):"
                                               f"\n\t\tif cls.b_Class_Init_flg is False:"
                                               f"\n\t\t\tcls.Import_Config()"
                                               f"\n\t\treturn cls.{key}\n")
                # Create Config Init Vars.
                if "# Start: Insert Config Init Vars" in line:
                    for section in range(len(cfg.sections())):
                        for key, value in cfg.items(cfg.sections()[section]):
                            if (key.startswith("b_") or key.startswith("lsb_") or key.startswith("i_")
                                    or key.startswith("f_") or key.startswith("str_") or key.startswith("lsi_")
                                    or key.startswith("lsf_") or key.startswith("lstr_")):
                                regex = re.match(r"^[A-Z-a-z]{,9999}\_", key)
                                class_key = f"{regex.group(0)}{cfg.sections()[section]}_{key[len(regex.group(0)):].title()}"
                                # Write values to class attributes.
                                if key.startswith("b_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                   f"cls.Clean_Convert_Boolean(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("lsb_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                      f"cls.Clean_Convert_List_Boolean(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("lsb_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"cls.Clean_Convert_Boolean(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("i_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"cls.Clean_Convert_Int(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("f_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"cls.Clean_Convert_Float(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("str_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"str(obj_Proj_Config['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("lsi_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"cls.Clean_Convert_List_Int(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("lsf_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"cls.Clean_Convert_List_Float(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                                if key.startswith("lstr_"):
                                    content.insert(i + 1, f"\n\t\tcls.{class_key} = "
                                                          f"cls.Clean_Convert_List_String(obj_Proj_Config"
                                                          f"['{cfg.sections()[section]}']['{key}'])")
                           
            # Delete everything from file and go to line 0.
            cho.seek(0)
            cho.truncate(0)
            # Write everything back to file.
            cho.writelines(content)
