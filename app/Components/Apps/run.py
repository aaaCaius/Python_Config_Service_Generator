import os
from app import root_dir    # This returns the absolute path of the application (\"app")
from configparser import ConfigParser
from app.template import Template_Config_Handler

def make_imports():
    """
    This function adds all needed variables to the Template_Config_Handler class and runs it.
    """
    ROOT_DIR = root_dir()
    cfg_path = os.path.join(ROOT_DIR, "config\\config.ini")
    cfg = ConfigParser()
    cfg.read(cfg_path)
    # to continue


