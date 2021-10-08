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

if sp.lower()=='world':
    slink = 'https://biogeo.ucdavis.edu/data/gadm3.6/gadm36_shp.zip'
    savename = 'world.zip'
else:
    k,v,s = findcd(sp)
    slink=template_url.format(k)
    savename = slink.split('/')[-1]

def download_shp_zip(slink, savename):

    print( "Downloading file:%s"%savename)
    
    # create response object
    r = requests.get(slink, stream = True)
    
    # download started
    with open(savename, 'wb') as f:
        for chunk in r.iter_content(chunk_size = 1024*1024):
            if chunk:
                f.write(chunk)
    
    print( "%s downloaded!\n"%savename )
    print ("File {} downloaded!".format(savename))
    return

download_shp_zip(slink, savename)

