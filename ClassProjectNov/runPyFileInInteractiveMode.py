import runpy
runpy.run_path(path_name='hello.py')

#Change processing extent
desc = arcpy.Describe(clipper)

xmin = desc.extent.XMin
xmax = desc.extent.XMax
ymin = desc.extent.YMin
ymax = desc.extent.YMax

arcpy.env.extent = arcpy.Extent(xmin, ymin, xmax, ymax)
