re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
ye="\033[1;33m"

import os, sys
import time

def banner():
	os.system('clear')
	print(f"""
	{cy}
████████████████████████████████
█─▄▄▄▄█▄─▄▄─█─▄─▄─█▄─██─▄█▄─▄▄─█
█▄▄▄▄─██─▄█▀███─████─██─███─▄▄▄█
▀▄▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▀▀
	""")

def requirements():
	def csv_lib():
		banner()
		print(cy+'May take a few moments to complete..')
		os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
	banner()
	input_csv = input(cy+'• Do you want to enable CSV merge (Y/N): ').lower()
	if input_csv == "y":
		csv_lib()
	else:
		pass
	print(ye+"• Installing requierments..")
	os.system("""
		pip3 install telethon requests configparser
		python3 -m pip install telethon requests configparser
		touch config.data
		""")
	banner()
	print(gr+"Requierments installed successfully!\n")


def config_setup():
	import configparser
	banner()
	cpass = configparser.RawConfigParser()
	cpass.add_section('cred')
	xid = input(ye+"• Enter API ID: "+re)
	cpass.set('cred', 'id', xid)
	xhash = input(ye+"• Enter Hash ID: "+re)
	cpass.set('cred', 'hash', xhash)
	xphone = input(ye+"• Enter Phone Number: "+re)
	cpass.set('cred', 'phone', xphone)
	setup = open('config.data', 'w')
	cpass.write(setup)
	setup.close()
	print(gr+"Setup has been completed!")

def merge_csv():
	import pandas as pd
	import sys
	banner()
	file1 = pd.read_csv(sys.argv[2])
	file2 = pd.read_csv(sys.argv[3])
	print(cy+'Merging '+sys.argv[2]+' & '+sys.argv[3]+'..')
	print(cy+'May take some time..')
	merge = file1.merge(file2, on='username')
	merge.to_csv("output.csv", index=False)
	print(gr+'Saved file as "output.csv"\n')

try:
	if any ([sys.argv[1] == '--config', sys.argv[1] == '-c']):
		config_setup()
	elif any ([sys.argv[1] == '--merge', sys.argv[1] == '-m']):
		merge_csv()
	elif any ([sys.argv[1] == '--install', sys.argv[1] == '-i']):
		requirements()
	elif any ([sys.argv[1] == '--help', sys.argv[1] == '-h']):
		banner()
		print("""
	( --config  / -c ) Setup API configuration
	( --merge   / -m ) Merge 2 .CSV files (python setup.py -m file1.csv file2.csv)
	( --install / -i ) Install Requirements
	( --help    / -h ) List commands 
			""")
	else:
		print('\n'+re+'Unknown argument: '+ sys.argv[1])
		print(cy+'For help use: ')
		print(cy+'python setup.py -h'+'\n')
except IndexError:
	print('\n'+re+'No argument given: '+ sys.argv[1])
	print(cy+'For help use : ')
	print(cy+'https://github.com/adrianeth')
	print(cy+'python setup.py -h'+'\n')
