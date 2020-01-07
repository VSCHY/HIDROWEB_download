#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Download daily discharge from HIDROWEB (Brazil)
Main Script

@author: A. Schrapffer
@Institution: Centro de Investigacion del Mar y el Oceano (CIMA/UBA/CONICET)

"""

#############################
######## LIBRARY ############
#############################

import pandas as pd
import subprocess
import os
import unidecode

#############################

# Directory where the data will be saved
# To complete
homedir = ""
workdir = os.path.dirname(os.path.realpath(__file__)) + "/"

if homedir == "":
    print("Test - don't forget to change homedir further !")
    homedir = workdir
 
#############################

file_stations = "./stations.csv"

stations = pd.read_csv(file_stations, sep = ",", header = None)


for ID, NAME in stations.values:
  print("**",ID, NAME,"**")
  NAME_alt = NAME.replace(" ", "_")
  NAME_alt = unidecode.unidecode(NAME_alt)
  
  home = homedir + "BR-{0}/".format(NAME_alt)

  #####
  print("**Preparation Directories**")

  if os.path.exists(home) == False:
    subprocess.check_call(["mkdir", home])
  else:
    reply = ""
    while reply != "n" and reply != "y":
        reply = str(input("Repertory already exists, process {0}?".format(NAME)+' (y/n): ')).lower().strip()
    if reply[0] == 'n':
      continue

  #####
  print("**Download data - be attentive for captcha**")
  try:
    subprocess.check_call(["python3", workdir+"Hidroweb_get.py", "-i", str(ID), "-n", NAME, "-d", home])
  except:
    continue

  #####
  print("**Process data**")  
  subprocess.check_call(["unzip", home+"Medicoes_convencionais.zip", "-d", home])
  subprocess.check_call(["unzip", home+"vazoes_C_"+str(ID)+".zip", "-d", home]) 

  subprocess.check_call(["sed", "-i", "-e" ,'s/,/./g', home+"vazoes_C_"+str(ID)+".csv"])
  subprocess.check_call(["sed", "-i", "-e" ,'s/\;/,/g', home+"vazoes_C_"+str(ID)+".csv"])

  subprocess.check_call(["soffice", "--headless", "--convert-to", "xlsx", "--outdir",home, home+"vazoes_C_"+str(ID)+".csv"])

  subprocess.check_call(["mv", home+"vazoes_C_"+str(ID)+".xlsx", home+NAME_alt+"_Caudal_Mensual.xlsx"])


