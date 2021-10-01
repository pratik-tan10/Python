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

