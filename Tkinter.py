from tkinter import Tk, Label, Entry, Button, DISABLED, StringVar 
 
def convert(): 
    """Takes miles entered, converts them to km, and displays the result"""
    miles = float(entryMiles.get()) 
    kilometers.set(str(miles * 1.60934)) 
 
# create the GUI 
 
rootWindow = Tk() # create main window 
rootWindow.title("Miles to kilometers") 
rootWindow.geometry('500x200+0+0') 
rootWindow.grid_columnconfigure(1, weight = 1) 
 
labelMiles = Label(rootWindow, text='Distance in miles:') # create label for miles field 
labelMiles.grid(row=0, column=0) 
 
labelKm = Label(rootWindow, text='Distance in kilometers:') # create label for km field 
labelKm.grid(row=2, column=0) 
 
entryMiles = Entry(rootWindow) # create entry field for miles 
entryMiles.grid(row=0, column=1, sticky='w,e') 
 
kilometers = StringVar() # create entry field for displaying km 
entryKm = Entry(rootWindow, textvariable = kilometers, state=DISABLED) 
entryKm.grid(row=2, column=1, sticky='w,e') 
 
convertButton = Button(rootWindow, text='Convert', command = convert) # create button for running conversion 
convertButton.grid(row=1, column=1) 
 
# run the event processing loop  
 
rootWindow.mainloop() 
