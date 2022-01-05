import arcpy

infc = arcpy.GetParameterAsText(0)
output_folder = arcpy.GetParameterAsText(1)
cleanName = arcpy.GetParameterAsText(2)

outfname = os.path.join(output_folder,cleanName)

if os.path.exists(outfname):
    os.remove(outfname)

def fwrite(message):
    with open(outfname,'a') as of:
        of.writelines(str(message)+'\n')

for row in arcpy.da.SearchCursor(infc, ["OID@", "SHAPE@WKT"]):
    
    fwrite("Feature {0}:".format(row[0]))
    partnum = 0

    for part in row[1]:

        for pnt in part:
            if pnt:
                fwrite("{0}, {1}".format(pnt.X, pnt.Y))
            else:
                fwrite("Interior Ring:")
        partnum += 1
