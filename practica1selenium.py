from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd
import re


# La implentació de l'Scrapping amb Selenium te aquests requeriments:

# WebDriver (en aquest cas hem triat Chrome)
#
# https://chromedriver.chromium.org/getting-started
#

def obtenir_urls_paisos_UN(navegador):

  # return ["http://data.un.org/en/iso/af.html"]

  # Obtenir la llista de països a partir de la pàgina index
  navegador.get("http://data.un.org/en/index.html")

  # Els paisos es mostren en una llista amb la següent estructura
  #<section>
  #  <ul id='myUL'>
  #    <li><a href='iso/af.html'> ... </li>
  #    <li><a href='iso/al.html'> ... </li>
  #    ...
  #  </ul>

  # Obtenim les URLs de tots els països
  paisos = [x.get_attribute("href") for x in navegador.find_elements_by_xpath("//*[@id='myUL']//a")]

  return paisos


# Cada taula es un objecte Selenium WebElement 
# Retornem un panda DataFrame amb tantes columnes com indicadors i tantes files com anys.
# Les files estan indexades per la tupla (pais,any)
def analitzar_taula(ISO2, taula):

  df = pd.DataFrame()

  # Només s'han d'analitzar les taules amb indicadors.
  # S'identifiquen perque tenen la paraula "indicator" a l'element <summary>
  summary = taula.find_element_by_tag_name("summary").text

  if not re.search('indicators',summary): 
    return df;

  print (summary + "...", end=" ", flush=True)

  # La taula presenta els indicadors en files i els anys en columnes
  # La primera columna de la taula conté el nom de l'indicador
  # i la resta de columnes els anys.

  # Obtenim els anys de l'encapçalament de la taula

  years = [x.get_attribute("innerText") for x in taula.find_elements_by_xpath("table/thead/tr/td")][1:]

  # Obtenim els indicadors de les files

  for fila in taula.find_elements_by_xpath("table/tbody/tr"):

    indicador = fila.find_element_by_tag_name("td").get_attribute("innerText").replace(u'\xa0', u' ')
    valors = [x.get_attribute("innerText").replace(" ","") for x in fila.find_elements_by_tag_name("small")][1:]
#    print(indicador)
#    print(valors)

    # Incorporar els valors al dataframe
    for year,valor in zip(years,valors):
      df = df.combine_first(pd.DataFrame(data=[valor],columns=[indicador],index=[(ISO2,year)]))

  return df


def analitzar_pais(navegador,url_pais):
  # les Url dels paisos tenen el format http://data.un.org/en/iso/<codiISO2>.html
  # Obtenim el codi ISO2 (en majuscules)
  ISO2 = re.search('(?<=iso/)..',url_pais).group(0).upper()

  print("Analitzant pais " + ISO2 + " ... ", end="", flush=True)

  # Descarregar la pàgina del pais
  navegador.get(url_pais)

  # Eliminem, usant javascript, els elements <sup> que dificulten l'anàlisi del contingut
  navegador.execute_script("var elements = document.getElementsByTagName('sup'); while (elements[0]) elements[0].parentNode.removeChild(elements[0]);")

  # Els indicadors de cada pais s'organitzen en diferents taules dins d'un element <details>
  taules = navegador.find_elements_by_tag_name("details")

  dfpais = pd.DataFrame()
  for taula in taules:
    dftaula = analitzar_taula(ISO2, taula)
    dfpais = dfpais.combine_first(dftaula)

  print(" fet.")

  return dfpais

#  Scrapping de la web de UN amb Selenium
def obtenir_indicadors_UN():

  # Iniciar el navegador (Chrome)

  # Crear una nova instancia de Chrome en mode incognit
  print("Obrint el navegador...." , end = " ")

  option = webdriver.ChromeOptions()
  option.add_argument("--incognito")

  navegador = webdriver.Chrome(executable_path='./chromedriver', options=option)

  print ("fet.")

  # Els indicadors de cada pais s'aniran integrant en un data frame amb tantes columnes com indicadors
  # Els dataframes estaran indexats per la tupla ("ISO2","year")

  indicadors_UN = pd.DataFrame()

  url_paisos = obtenir_urls_paisos_UN(navegador)

  for url_pais in url_paisos[:5]:
    df_pais = analitzar_pais(navegador,url_pais)
    indicadors_UN = indicadors_UN.combine_first(df_pais)

  # Generar les columnes "ISO2" i "year" a partir de l'index del dataframe
  dfindex = pd.DataFrame(indicadors_UN.index.to_list(),columns=["ISO2","year"],index=indicadors_UN.index)
  indicadors_UN.insert(0,"year",dfindex['year'])
  indicadors_UN.insert(0,"ISO2",dfindex['ISO2'])

  # Tanquem el navegador
  navegador.quit()


  return indicadors_UN


 


