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
