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
from practica_1.practica1funcions import *
from practica_1.practica1selenium import *


pd.set_option("display.width", 320)
pd.set_option("display.max_columns", 50)


# Obtenir els indicadors de la web de les Nacions Unides
dfUN = obtenir_indicadors_UN()


# Per poder incorporar els indicadors del banc mundial, cal obtenir el codi ISO de 3 lletres dels paisos
iso3166 = obtenir_llista_iso3166()
dfUN = dfUN.merge(iso3166,how="left",on=['ISO2'])

# Incorporar indicadors obtinguts via API del BancMundial

# Llista d'indicadors World Bank
indicadors_BM = ["SP.POP.TOTL", "SP.POP.GROW", "SP.POP.0014.TO.ZS", "SP.POP.65UP.TO.ZS", "SP.DYN.LE00.FE.IN",
                 "SP.DYN.LE00.MA.IN", "SH.DTH.NCOM.ZS", "SH.DTH.COMM.ZS", "SH.TBS.INCD", "SH.DYN.AIDS.ZS",
                 "SN.ITK.DEFC.ZS", "SH.MED.BEDS.ZS"]

for indBM in indicadors_BM:
    print(indBM)
    dfBM = llegir_indicador_world_bank(indBM)
    dfUN = dfUN.merge(dfBM, how='left', on=['ISO3', 'year'])

# Reordenem el dataframe i canviem el nom dels atributs
del dfUN['ISO2']
dfUN = dfUN[["ISO3", "country", "year", "SP.POP.TOTL", "SP.POP.GROW", "SP.POP.0014.TO.ZS", "SP.POP.65UP.TO.ZS",
                 "GDP: Gross domestic product (million current US$)", "GDP growth rate (annual %, const. 2010 prices)",
                 "Unemployment (% of labour force)", "Education: Government expenditure (% of GDP)",
                 "Health: Current expenditure (% of GDP)", "SP.DYN.LE00.FE.IN", "SP.DYN.LE00.MA.IN", "SH.DTH.NCOM.ZS",
                 "SH.DTH.COMM.ZS", "SH.TBS.INCD", "SH.DYN.AIDS.ZS", "Infant mortality rate (per 1 000 live births)",
                 "SN.ITK.DEFC.ZS", "SH.MED.BEDS.ZS", "Health: Physicians (per 1 000 pop.)"]]

dfUN = dfUN.rename(
    columns={"ISO3": "country_code", "country": "country", "year": "year", "SP.POP.TOTL":"population",
             "SP.POP.GROW": "population_grow", "SP.POP.0014.TO.ZS": "population_under_14",
             "SP.POP.65UP.TO.ZS": "population_above_65", "GDP: Gross domestic product (million current US$)": "gdp",
             "GDP growth rate (annual %, const. 2010 prices)": "gdp_growth_rate",
             "Unemployment (% of labour force)": "unemployment",
             "Education: Government expenditure (% of GDP)": "education_gov_expenditure",
             "Health: Current expenditure (% of GDP)": "health_expenditure", "SP.DYN.LE00.FE.IN": "life_expectancy_fem",
             "SP.DYN.LE00.MA.IN": "life_expectancy_male", "SH.DTH.NCOM.ZS": "non_commun_disease_death",
             "SH.DTH.COMM.ZS": "commun_disease_death", "SH.TBS.INCD": "tuberculosis",
             "SH.DYN.AIDS.ZS": "hiv", "Infant mortality rate (per 1 000 live births)": "infant_mortality",
             "SN.ITK.DEFC.ZS": "undernourishment", "SH.MED.BEDS.ZS": "hospital_beds",
             "Health: Physicians (per 1 000 pop.)": "physicians"})

# Eliminem territoris dels quals considerem que la quantitat de dades de la que disposem és insuficient,
# molts d'ells són territoris no autònoms i petites illes.
dfUN = dfUN.replace('~0.0', '0.0').replace('', np.nan).dropna(thresh=13)

# Arrodonim les posicions decimals dels valors d'algunes columnes
dfUN = dfUN.round({"population": 0, "population_grow": 2, "population_under_14": 2, "population_above_65": 2,
                   "life_expectancy_fem": 2, "life_expectancy_male": 2})

# Finalment guardem el DataFrame dfUN en format .csv
dfUN.to_csv("world_health_indicators.csv",index=False)


