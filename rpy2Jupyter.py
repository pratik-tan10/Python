#In jupyter notebook markup cell
# Simple example of reading a web page and converting it to plain text 
How the code works: 
* package **requests** is used to load web page from URL given in variable *documentURL* 
* package **BeautifulSoup4 (bs4)** is used to parse content of loaded web page 
* the call of *soup.get_text()* in the last line provides the content of page as plain text 
