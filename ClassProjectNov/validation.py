import arcpy
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""

  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    self.params = arcpy.GetParameterInfo()

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    self.params[3].value = 'Select the Field'
    self.params[3].filter.list=[]
    f1 = []
    return

  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    if self.params[0].altered:
      self.params[3].clearMessage()
      cp = arcpy.Describe(self.params[0].value).catalogPath
      fl = arcpy.ListFields(cp)
      self.params[3].filter.list = [s.name for s in fl]
      self.params[3].clearMessage()      
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    return
