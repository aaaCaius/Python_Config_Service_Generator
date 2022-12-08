import os
from app import root_dir    # This returns the absolute path of the application (\"app")
from configparser import ConfigParser


def make_imports():
    """
    This function adds all needed variables to the Template_Config_Handler class and runs it.
    """
    # Get the root directory of the app.
    ROOT_DIR = root_dir()

    # Load config file.
    cfg_path = os.path.join(ROOT_DIR, "config/config.ini")
    cfg = ConfigParser()
    cfg.read(cfg_path)
    # Create an empty dict to store the key-value pairs from config.ini.
    cfg_dict = {}
    for section in cfg.sections():
        cfg_dict[section] = {}
        for key, value in cfg.items(section):
            cfg_dict[section][key] = value
    
    # Open Template_Config_Handler.py as text.
    tch_path = os.path.join(ROOT_DIR, "template/Template_Config_Handler.py")
    with open(tch_path, "r+") as tch:
        # Get all content from the file
        content = tch.readlines()
        for i, line in enumerate(content):
            if "# Start: Insert Cfg Objects" in line:
                # Get the total number of keys in each section of .ini file. Add them to keys_in_cfg.
                for j in cfg_dict.keys():
                    for key, value in cfg_dict[j].items():
                        # Add the key-value pairs as class attributes.
                        content.insert(i + 1, f"\t{key} = {value}\n")
            if "# Start: Insert Get Methods" in line:
                # Get the total number of keys in each section of .ini file. Add them to keys_in_cfg.
                for j in cfg_dict.keys():
                    for key, value in cfg_dict[j].items():
                        # Add the key-value pairs as class attributes.
                        content.insert(i + 1,
                                       f"\n\t@classmethod\n\tdef Get_{key}(cls):"
                                       f"\n\t\tif cls.b_Class_Init_flg is False:"
                                       f"\n\t\t\tcls.Import_Config()"
                                       f"\n\t\treturn cls.{key}\n")
        # Delete everything from file and go to line 0.
        tch.seek(0)
        tch.truncate(0)
        # Write everything to file.
        tch.writelines(content)
