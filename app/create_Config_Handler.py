import os
from configparser import ConfigParser
from pprint import pprint

def create_Config_Handler():
	"""
	A function that automatically creates the Config_Handler class.

	"""

	# Create aabsolute path for the .ini file
	ROOT_DIR = os.path.dirname(os.path.abspath('App'))
	cfg_file_path = os.path.join(ROOT_DIR,"Config\\config.ini")
	# Instantiate ConfigParser()
	config = ConfigParser()
	# Read the .ini file.
	config.read(cfg_file_path)

	# Create the path where to save the new .py file.
	save_path = os.path.join(ROOT_DIR,"Output\\Config_Handler_Output.py")

	# Open/Create the new .py file.
	# Creating class attributes.
	with open(save_path, "w") as new_file:
		new_file.write("import os" + "\n")
		new_file.write("from configparser import ConfigParser" + "\n" * 2)
		new_file.write("class Config_Handler:" + "\n")
		new_file.write("\tClass_Init_sts = False" + "\n" * 2)

		# Set a flag to check when section changes.
		current_section = ""

		# This section creates all class attributes.
		# Loop ever the sections in .ini file
		for section in config.sections():
			# Leave a blank row if there was a section change.
			if current_section != section:
				current_section = section
				new_file.write("\n")
				# Loop over the key-values in the section.
			for key, value in config.items(section):
				key = key.title()
				sw = "_Sw"
				if sw  in key:
					sw_index = key.index(sw)
					key = list(key)
					key[sw_index +1] = "S"
					key[sw_index + 2] = "W"
					key = "".join(key)
					new_file.write(f"\t{key} = ''\n")
				else:	
					# Write the section content to .py file.
					new_file.write(f"\t{key.title()} = ''\n")

		# This section creates all class methods.
		# Loop over the section in .ini file.
		for section in config.sections():
			# Loop over the key-value pairs in each section.
			for key, value in config.items(section):
				# This section tries to find "Sw" in key name, and if it's found it 
				# will convert it to uppercase, and usese titlecase to create methods.
				key = key.title()
				sw = "_Sw"
				if sw  in key:
					sw_index = key.index(sw)
					key = list(key)
					key[sw_index +1] = "S"
					key[sw_index + 2] = "W"
					key = "".join(key)
					new_file.write("\n\t@classmethod\n")
					new_file.write(f"\tdef Get_{key}(cls):\n")
					new_file.write(f"\t\tif cls.Class_Init_sts is False:\n")
					new_file.write(f"\t\t\tcls.Import_Config()\n")
					new_file.write(f"\t\treturn cls.{key}" + "\n" * 2)
				# If there is no "Sw" in key name, 
				# create the method using titlecase names.	
				else:	
					new_file.write("\n\t@classmethod\n")
					new_file.write(f"\tdef Get_{key.title()}(cls):\n")
					new_file.write(f"\t\tif cls.Class_Init_sts is False:\n")
					new_file.write(f"\t\t\tcls.Import_Config()\n")
					new_file.write(f"\t\treturn cls.{key.title()}" + "\n" * 2)


		# # Create a dictionary with everything in .ini file.
		# dictionary = {}
		# for section in config.sections():
		#     dictionary[section] = {}
		#     for option in config.options(section):
		#     	option = option.title()
		#     	sw = "_Sw"
		#     	if sw  in option:
		#     		sw_index = option.index(sw)
		#     		option = list(option)
		#     		option[sw_index +1] = "S"
		#     		option[sw_index + 2] = "W"
		#     		option = "".join(option)
		#     		dictionary[section][option] = config.get(section, option)
		#     	else:
		#     		dictionary[section][option] = config.get(section, option)
		# new_file.write(f"\n\n\t@classmethod\n")
		# new_file.write(f"\tdef Import_Config(cls):\n")
		# new_file.write(f"\t\t#Creating path to project config file\n")
		# new_file.write(f"\t\tROOT_DIR = os.path.dirname(os.path.abspath('App'))\n")
		# new_file.write(f"\t\tcfg_file_path = os.path.join(ROOT_DIR,'Config/config.ini')\n\n") 
		# new_file.write(f"\t\t#Import and parse config file\n")
		# new_file.write(f"\t\tproj_config = ConfigParser()\n")
		# new_file.write(f"\t\tproj_config.read(cfg_file_path)\n")
		# new_file.write(f"\t\t#Import all sections from config file\n\n")
		# for key in dictionary.keys():
		# 	for key_of_key, value in dictionary[key].items():
		# 		new_file.write(f"\t\tcls.{key_of_key} = {value}\n")
		# new_file.write(f"\t\tcls.Class_Init_sts = True\n")


		# Iterate over all sections.
		for section in config.sections():
			# Iterate over keys and values in each section.
			for key, value in config.items(section):
				# Turn all keys to uppercase.
				key = key.title()
				# Set a variable to look for _Sw string.
				sw = "_Sw"
				# If sw variable is found, get it's index.
				if sw in key:
					sw_index = key.index(sw)
					# Turn the key into a list so we can change it.
					key = list(key)
					# Make desired modifications.
					key[sw_index + 1] = "S"
					key[sw_index + 2] = "W"
					# Turn key list back into a string.
					key = "".join(key)
				else:
					pass
		new_file.write(f"\n\n\t@classmethod\n")
		new_file.write(f"\tdef Import_Config(cls):\n")
		new_file.write(f"\t\t#Creating path to project config file\n")
		new_file.write(f"\t\tROOT_DIR = os.path.dirname(os.path.abspath('App'))\n")
		new_file.write(f"\t\tcfg_file_path = os.path.join(ROOT_DIR,'Config/config.ini')\n\n") 
		new_file.write(f"\t\t#Import and parse config file\n")
		new_file.write(f"\t\tproj_config = ConfigParser()\n")
		new_file.write(f"\t\tproj_config.read(cfg_file_path)\n")
		new_file.write(f"\t\t#Import all sections from config file\n\n")	

		# Create a for loop inside the new class.
		new_file.write(f"\t\tfor section in proj_config.sections():\n")
		new_file.write(f"\t\t\tfor key, value in proj_config.items(section):\n")
		new_file.write(f"\t\t\t\tkey = key.title()\n")
		new_file.write(f"\t\t\t\tsw = '_Sw'\n")
		new_file.write(f"\t\t\t\tif sw in key:\n")
		new_file.write(f"\t\t\t\t\tsw_index = key.index(sw)\n")
		new_file.write(f"\t\t\t\t\tkey = list(key)\n")
		new_file.write(f"\t\t\t\t\tkey[sw_index + 1] = 'S'\n")
		new_file.write(f"\t\t\t\t\tkey[sw_index + 2] = 'W'\n")
		new_file.write(f"\t\t\t\t\tkey = ''.join(key)\n")	
		new_file.write(f"\t\t\t\tcls.key = str(proj_config[section][key])\n")
		new_file.write(f"\t\tcls.Class_Init_sts = True\n")




		# # Iterate over all sections.
		# for section in config.sections():
		# 	# Iterate over keys and values in each section.
		# 	for key, value in config.items(section):
		# 		# Turn all keys to uppercase.
		# 		key = key.title()
		# 		# Set a variable to look for _Sw string.
		# 		sw = "_Sw"
		# 		# If sw variable is found, get it's index.
		# 		if sw in key:
		# 			sw_index = key.index(sw)
		# 			# Turn the key into a list so we can change it.
		# 			key = list(key)
		# 			# Make desired modifications.
		# 			key[sw_index + 1] = "S"
		# 			key[sw_index + 2] = "W"
		# 			# Turn key list back into a string.
		# 			key = "".join(key)
				
		# 		# new_file.write(f"\t\t\t\tcls.{key} = str(proj_config['{section}']['{key}']\n")
				
create_Config_Handler()