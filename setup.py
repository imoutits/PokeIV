#!/usr/bin/env python

#-- Setup file for py2exe

from distutils.core import setup
import py2exe
import sys, os
import Cryptodome
import requests

#find POGOProtos
sys.path.append("pgoapi\protos")

mydata = list()
path = Cryptodome.__path__[0]
root_end = path.find('Cryptodome')
for folder,folder_name,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.pyd':
            mydata.append((folder[root_end:], [os.path.join(folder,file)]))

path = requests.__path__[0]
root_end = path.find('requests')
for folder,folder_name,files in os.walk(path):
    for file in files:
        if file == 'cacert.pem':
            mydata.append((folder[root_end:], [os.path.join(folder,file)]))


path = os.path.join(os.path.dirname(os.path.realpath(__file__)),'pgoapi')
root_end = 'pgoapi'
for folder,folder_name,files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1] == '.json':
            mydata.append((root_end, [os.path.join(folder,file)]))

mydata.extend(('families.tsv','evolves.tsv','german-names.tsv','config.json'))

setup(data_files=mydata,
      windows = [{'script': "pokeIV.py"}],
      zipfile = None,
	  options= {
        "py2exe":{
            "packages": ['s2sphere',
                        'six',
                        'gpsoauth',
                        'geopy',
                        'requests',
                        'Cryptodome',
                        'POGOProtos',
                        'POGOProtos.Networking.Requests',
                        'POGOProtos.Networking.Requests.Messages_pb2',
                        'POGOProtos.Networking.Responses_pb2']
            ,'bundle_files': 1
            ,'compressed': True
			,'dll_excludes': [ 'crypt32.dll', 'mpr.dll']
		}
     })
