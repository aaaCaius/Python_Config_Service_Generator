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
    # Load Template_Config_Handler.
    tch_path = os.path.join(ROOT_DIR, "template/Template_Config_Handler.py")
    # Open Template_Config_Handler.py as text.
    with open(tch_path, "r+") as tch:
        content = tch.readlines()
        for line in range(len(content)):
            if "# Start: Insert Cfg Objects" in content[line]:
                for section in cfg.sections():
                    for key, value in cfg.items(section):
                        content[line + 1] = f"\n\t{key} = {value}\n"
        # Delete everything from file.
        tch.seek(0)
        tch.truncate(0)
        tch.writelines(content)



