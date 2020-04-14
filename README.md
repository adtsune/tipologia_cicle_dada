# TIPOLOGIA I CICLE DE VIDA DE LES DADES

## PRÀCTICA 1 - WEB SCRAPING 

## WORLD HEALTH INDICATORS DATASET

- Integrants del Grup: Xavier Ventura i Anna De la Torre.

- Llenguatge de programació: Python.

- Data de captura de dades: 14 d'Abril de 2020.


## Descripció del dataset:

El dataset World Health Indicators conté dades relacionades amb l'àmbit de la salut pública i dades socioeconòmiques referents a 227 països i regions del món. Ha estat elaborat a partir de dades proporcionades per l'Organització de les Nacions Unides i pel Banc Mundial a través dels seus llocs web. Ambdues són organitzacions que treballen pel desenvolupament humà, la seguretat i l'erradicació de la pobresa al món.


## Descripció de fitxers

### Fitxer descriptiu

- Pràctica_1_Web_Scraping.pdf - Fitxer que conté la descripció de la pràctica, inclosa l'explicació dels diferents atributs del dataset presentat.

### Fitxers de codi

El codi està compost per tres arxius en llenguatge Python:

- practica1.py – Arxiu principal, que crida a diverses funcions dels dos arxius següents, i obté el dataset i el guarda en un arxiu tipus .csv.

- practica1selenium.py – Arxiu que conté les funcions que realitzen el web scraping i la manipulació de dades del lloc web de les Nacions Unides utilitzant la llibreria Selenium de Python.

- practica1funcions.py – Arxiu que conté les funcions que obtenen les dades del lloc web del Banc Mundial a través d'API, i la nomenclatura ISO pels països amb web scraping utilitzant la llibreria BeautifulSoup de Python.

### Fitxer.csv

- indicadors_practica1.csv - Es tracta del fitxer generat en format csv amb el dataset resultant.


## Referències

1. Subirats, L., Calvo, M. (2018). _Web Scraping_. Editorial UOC.
2. Masip, D. (2010). _El lenguaje Python_. Editorial UOC.
3. Lawson, R. (2015). _Web Scraping with Python_. Packt Publishing Ltd. Chapter 2. Scraping the Data.
4. Mitchel, R. (2015). _Web Scraping with Python: Collecting Data from the Modern Web_. O’Reilly Media, Inc., 1005 Gravenstein Highway North, Sebastopol, CA 95472.
