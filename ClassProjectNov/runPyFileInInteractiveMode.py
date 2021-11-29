import runpy
runpy.run_path(path_name='hello.py')

#Change processing extent
def setExtent(clipper):
  desc = arcpy.Describe(clipper)

  xmin = desc.extent.XMin
  xmax = desc.extent.XMax
  ymin = desc.extent.YMin
  ymax = desc.extent.YMax

  arcpy.env.extent = arcpy.Extent(xmin, ymin, xmax, ymax)

  def setExtentAlternative(clipper):
    try:arcpy.env.extent = clipper.extent
    except: arcpy.env.extent = row[0].extent
