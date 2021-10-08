import requests
from bs4 import BeautifulSoup


# specify the URL of the archive here
template_url = "https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_{}_shp.zip"
sp = input('Enter your country name.\n')
