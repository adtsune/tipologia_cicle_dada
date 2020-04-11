import builtwith
import whois
from bs4 import BeautifulSoup
import requests
import re
import numpy as np
import pandas as pd
from nested_dict import nested_dict
import time
import csv
import itertools
import sys
import os.path


# Obtenim informació sobre amb quines tecnologies s'ha elaborat el lloc web.
# print(builtwith.builtwith("http://data.un.org/en/index.html"))
# print(builtwith.builtwith("http://data.un.org/en/iso/af.html"))

# Obtenim informació sobre el propietari del lloc web:
# print(whois.whois("http://data.un.org/en/index.html"))

# Funcions d'utilitats
from practica1funcions import *
from practica1selenium import *


# Pendent:
# - Dividir els indicadors amb 2 valors en 2 indicadors diferents
# - Eliminar "~"
# - Passar a valors numèrics els valors dels indicadors
# - No tots els paisos tenen els mateixos indicadors



# Obtenir els indicadors de la web de les Nacions Unides
dfUN = obtenir_indicadors_UN()

# Per poder incorporar els indicadors del banc mundial, cal obtenir el codi ISO de 3 lletres dels paisos
iso3166 = obtenir_llista_iso3166()
dfUN = dfUN.merge(iso3166,how="left",on=['ISO2'])

# Incorporar indicadors obtinguts via API del BancMundial

indicadors_BM = ["SP.DYN.LE00.IN", "SP.POP.TOTL"]

for indBM in indicadors_BM:
    print(indBM)
    dfBM = llegir_indicador_world_bank(indBM)
    # dfUN = dfUN.merge(df1[df1['year'].isin(['2005', '2010', '2019'])], how='outer', on=['country', 'year'])
    dfUN = dfUN.merge(dfBM, how='left', on=['ISO3', 'year'])

# Pas final guardem el DataFrame dfUN en format .csv
dfUN.to_csv("indicadors_practica1.csv",index=False)

