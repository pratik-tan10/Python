from ipywidgets import widgets 
from IPython.display import display 
 
def onButtonClick(b):
    print("Button " + b.description + " has been clicked")
 
for i in range(1,4):
    button = widgets.Button(description=str(i))
    display(button)
    button.on_click(onButtonClick)
