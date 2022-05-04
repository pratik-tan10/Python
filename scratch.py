arcpy.MakeFeatureLayer_management(r"C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg/al_tuscaloosa.gpkg/main.al_tuscaloosa", "main.al_tuscaloosa")
arcpy.management.AddJoin("main.al_tuscaloosa", "ogc_fid", "zs", "ogc_fid", "KEEP_ALL")
arcpy.management.SelectLayerByAttribute("main.al_tuscaloosa", "NEW_SELECTION", "zs:MAJORITY IS NULL", None)
arcpy.env.workspace = "C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch"
arcpy.FeatureToPoint_management("main.al_tuscaloosa", "parcels_center.shp", 
                                "INSIDE")
###################################
# IMPORTING DATA

import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

pic=misc.face() #reading an image from misc in scipy
plt.imshow(pic) #displaying the image using imshow() function in matplot
pic=misc.imread(location_of_image) 
misc.imsave(‘picture_name_to_be_stored’,pic) #here pic is the name of the variable holding the image

path = glob.glob("D:/New folder/*.png") #storing the location of all the images in variable path
imgs = [] #creating an empty list
for img in path: #running a loop to iterate through every image in the file
    pic = plt.imread(img) #reading the image using matplotlib
    imgs.append(pic) #adding the image to the list
    
