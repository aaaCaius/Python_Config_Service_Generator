import os
from app import root_dir    # This returns the absolute path of the application (\"app")
from configparser import ConfigParser
import re

def make_imports():
    """
    This function adds all needed variables to the Template_Config_Handler class and runs it.
    """
    # Get the root directory of the app.
    ROOT_DIR = root_dir()

    # Load config file.
    cfg_path = os.path.join(ROOT_DIR, "Config/config.ini")
    cfg = ConfigParser()
    cfg.read(cfg_path)
    
    # Open Template_Config_Handler.py as text.
    tch_path = os.path.join(ROOT_DIR, "template/Template_Config_Handler.py")
    with open(tch_path, "r+") as tch:
        # Get all content from the file
        content = tch.readlines()
        for i, line in enumerate(content):
            # Get class attributes
            if "# Start: Insert Cfg Objects" in line:
                for section in range(len(cfg.sections())):
                    content.insert(i + 1, f"\n\t# {cfg.sections()[section].upper()} section\n")
                    for key, value in cfg.items(cfg.sections()[section]):
                        regex = re.match(r"^[A-Z-a-z]{,9999}\_", key)
                        key = f"{regex.group(0)}{cfg.sections()[section]}_{key[len(regex.group(0)):].title()}"
                        print(key)
                        #Add the key-value pairs as class attributes.
                        content.insert(i + 2, f"\t{key} = {value}\n")
            # Create class "get" functions
            if "# Start: Insert Get Methods" in line:
                for section in range(len(cfg.sections())):
                    for key, value in cfg.items(cfg.sections()[section]):
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
                        regex = re.match(r"^[A-Z-a-z]{,9999}\_", key)
                        key = f"{regex.group(0)}{cfg.sections()[section]}_{key[len(regex.group(0)):].title()}"
                        content.insert(i + 1,
                                       f"\n\t\tcls.{key} = ")
                                        # To continue



        # Delete everything from file and go to line 0.
        tch.seek(0)
        tch.truncate(0)
        # Write everything back to file.
        tch.writelines(content)
