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
  
    
    # Load Template_Config_Handler.
    tch_path = os.path.join(ROOT_DIR, "template/Template_Config_Handler.py")
    # Open Template_Config_Handler.py as text.
    with open(tch_path, "r+") as tch:
        # Get all content from the file
        content = tch.readlines()
        keys_in_cfg = []
        for line in range(len(content)):
            if "# Start: Insert Cfg Objects" in content[line]:
                first_line = line
                for section in cfg_dict.keys():
                    # Get the number of keys for each section and add them to the keys_in_cfg list.
                    keys_in_cfg.append(len(cfg_dict[section]))
                    for key, value in cfg_dict[section].items():
                        # Add as many empty rows as the sum of all keys in cfg.ini.
                        content[line + 1] = "\n" * sum(keys_in_cfg)
                        # To continue
                        
                        
        
        # Delete everything from file.
        tch.seek(0)
        tch.truncate(0)
        tch.writelines(content)



