import os

def root_dir():
    """ A function that returns the abs path of the appication(\"app")"""
    root_dir = os.path.dirname(os.path.abspath(__file__))
    return root_dir

