def printf(lst):
    for each in lst:
        print(each)
gdbName = "myGDB.gdb"
arcpy.env.workspace=gdbName
polygons = arcpy.ListFeatureClasses(gdbName, "POLYGON")
printf(polygons)
print(len(polygons))
