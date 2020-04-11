# TIPOLOGIA I CICLE DE VIDA DE LES DADES

# PRÀCTICA 1 - WEB SCRAPING 

# WORLD HEALTH INDICATORS DATASET

# Integrants del Grup: Xavier Ventura i Anna De la Torre.

# Llenguatge de programació: Python.

# Data de captura de dades: 12 d'Abril de 2020.


# Descripció:

# web scraping de diverses URL del lloc web de les Nacions Unides que contenen indicadors econòmics i socials pels diferents països 
# del món. L'índex d'URLs es pot trobar al següent link: http://data.un.org/en/index.html. S'utilitza la llibreria Selenium de Python.

# S'obtenen diversos indicadors demogràfics i de salut pública dels diferents països del món del lloc web del Banc Mundial a través d'API. L'índex dels diferents indicadors existents es pot trobar a: https://data.worldbank.org/indicator.

# Es capturen els valors del indicadors pels anys 2005, 2010 i 2019.

# S'obté la nomenclatura ISO pels països a través d'un procés de web scraping mitjançacnt la llibreria BeautifulSoup de Python.

# Es crea un únic dataframe que aglutina els valors de diversos indicadors donats per les dues institucions i es guarda en un arxiu 
# en format .csv. 



# Llista indicadors UN data
indicadors_UN = ["GDP: Gross domestic product (million current US$)", "GDP per capita (current US$)",
                 "GDP growth rate (annual %, const. 2010 prices)", "Unemployment (% of labour force)",
                 "Infant mortality rate (per 1000 live births)", "Health: Current expenditure (% of GDP)"]


# Llista d'indicadors World Bank

indicadors_BM = ["SP.POP.TOTL", "SP.DYN.CBRT.IN", "SP.DYN.CDRT.IN", "SP.DYN.LE00.FE.IN", "SP.DYN.LE00.MA.IN",
                 "SP.POP.65UP.TO.ZS", "SH.DTH.COMM.ZS", "SN.ITK.DEFC.ZS", "SH.DYN.AIDS.ZS", "SH.DTH.NCOM.ZS",
                 "SH.MED.BEDS.ZS", "SH.MED.PHYS.ZS", "SH.SGR.PROC.P5"]

# Population, total
#https://data.worldbank.org/indicator/SP.POP.TOTL?view=chart

# Birth rate, crude (per 1,000 people)
# https://data.worldbank.org/indicator/SP.DYN.CBRT.IN?view=chart

# Death rate, crude (per 1,000 people)
#https://data.worldbank.org/indicator/SP.DYN.CDRT.IN?view=chart

# Life expectancy at birth, female (years)
#https://data.worldbank.org/indicator/SP.DYN.LE00.FE.IN?view=chart

# Life expectancy at birth, male (years)
#https://data.worldbank.org/indicator/SP.DYN.LE00.MA.IN?view=chart

# Population ages 65 and above (% of total population)
#https://data.worldbank.org/indicator/SP.POP.65UP.TO.ZS?view=chart

# Prevalence of undernourishment (% of population)
#https://data.worldbank.org/indicator/SN.ITK.DEFC.ZS?view=chart

# Prevalence of HIV, total (% of population ages 15-49)
#https://data.worldbank.org/indicator/SH.DYN.AIDS.ZS?view=chart

# Cause of death, by communicable diseases and maternal, prenatal and nutrition conditions (% of total)
#https://data.worldbank.org/indicator/SH.DTH.COMM.ZS?view=chart

# Cause of death, by non-communicable diseases (% of total)
#https://data.worldbank.org/indicator/SH.DTH.NCOM.ZS?view=chart

# Hospital beds (per 1,000 people)
#https://data.worldbank.org/indicator/SH.MED.BEDS.ZS?view=chart

# Physicians (per 1,000 people)
#https://data.worldbank.org/indicator/SH.MED.PHYS.ZS?view=chart

# Number of surgical procedures (per 100,000 population)
#https://data.worldbank.org/indicator/SH.SGR.PROC.P5?view=chart


