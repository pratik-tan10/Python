import requests
from bs4 import BeautifulSoup


# specify the URL of the archive here
template_url = "https://biogeo.ucdavis.edu/data/gadm3.6/shp/gadm36_{}_shp.zip"
sp = input('Enter your country name.\n')

cdict = {}
with open("countriesShortform.txt",'r') as f:
    lines = f.readlines()
    for line in lines:
        a = line.split(',')
        if len(a)>1:
            cdict[a[0]]=a[1].rstrip()

def findcd(sp):
    for key, val in cdict.items():
        if sp.replace(' ','').lower()==val.lower():
            return(key, val, sp)
    return None
