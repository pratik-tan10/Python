#In jupyter notebook markup cell
# Simple example of reading a web page and converting it to plain text 
How the code works: 
* package **requests** is used to load web page from URL given in variable *documentURL* 
* package **BeautifulSoup4 (bs4)** is used to parse content of loaded web page 
* the call of *soup.get_text()* in the last line provides the content of page as plain text 
#_______________________________________________________________________
import os, rpy2
os.environ['R_HOME'] = r'C:\Users\username\anaconda3\envs\AC37\lib\R' # workaround for R.dll issue occurring on some systems
%load_ext rpy2.ipython

#_______________________________________________________________________
	
?%R 


#_______________________________________________________________________

?BeautifulSoup


#_______________________________________________________________________

?soup.get_text()


#_______________________________________________________________________
#WIDGETS

from ipywidgets import widgets 
from IPython.display import display 
 
def onButtonClick(b):
    print("Button " + b.description + " has been clicked")
 
for i in range(1,4):
    button = widgets.Button(description=str(i))
    display(button)
    button.on_click(onButtonClick)

#_______________________________________________________________________
from ipywidgets import widgets 
from IPython.display import display 
 
def onButtonClick(b):
    print("Button " + b.description + " has been clicked")
 
for i in range(1,4):
    button = widgets.Button(description=str(i))
    display(button)
    button.on_click(onButtonClick)


#_______________________________________________________________________

require('dismo')
bc <- bioclim(predictorRasters, observationPoints)



#_______________________________________________________________________


pb <- predict(predictorRasters, bc)
plot(pb, main='Bioclim, raw values')

#_______________________________________________________________________


%load_ext rpy2.ipython

#_______________________________________________________________________


