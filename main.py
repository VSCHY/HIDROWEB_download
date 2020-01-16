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
import glob
import time

#############################
#############################

# Directory where the data will be saved
# To complete
homedir = ""
workdir = os.path.dirname(os.path.realpath(__file__)) + "/"

if homedir == "":
    print("Test - don't forget to change homedir further !")
    homedir = workdir
 
#############################
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

  D = {"vazoes":"Caudal", "cotas":"Altura"}
  
  for varn in ["vazoes", "cotas"]:
      filename = home+"{0}_C_{1}.zip".format(varn,ID)
      if os.path.exists(filename):
          subprocess.check_call(["unzip", filename, "-d", home]) 

          subprocess.check_call(["sed", "-i", "-e" ,'s/,/./g', filename.replace("zip","csv")])
          subprocess.check_call(["sed", "-i", "-e" ,'s/\;/,/g', filename.replace("zip","csv")])

          subprocess.check_call(["soffice", "--headless", "--convert-to", "xlsx", "--outdir",home, filename.replace("zip","csv")])
          time.sleep(5)

          subprocess.check_call(["mv", filename.replace("zip","xlsx"), home+NAME_alt+"_{0}_Mensual.xlsx".format(D[varn])])
      
          os.remove(filename.replace("zip","csv"))

  #####

