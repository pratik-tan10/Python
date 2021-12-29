import arcpy

infc = arcpy.GetParameterAsText(0)
output_folder = arcpy.GetParameterAsText(1)
cleanName = arcpy.GetParameterAsText(2)

#Define full path of logfile
outfname = os.path.join(output_folder,cleanName)

#If the file already exists, it is deleted
if os.path.exists(outfname):
    os.remove(outfname)

#writeMessage function takes a message string and write it to the log file
def fwrite(message):
    with open(outfname,'a') as of:
        of.writelines(str(message)+'\n')

# Enter for loop for each feature
for row in arcpy.da.SearchCursor(infc, ["OID@", "SHAPE@WKT"]):
    # Write the current multipoint's ID
    
    fwrite("Feature {0}:".format(row[0]))
    partnum = 0

    # Step through each part of the feature
    #
    for part in row[1]:

        # Step through each vertex in the feature
        #
        for pnt in part:
            if pnt:
                # Write x,y coordinates of current point
                #
                fwrite("{0}, {1}".format(pnt.X, pnt.Y))
            else:
                # If pnt is None, this represents an interior ring
                #
                fwrite("Interior Ring:")
        partnum += 1
