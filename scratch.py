arcpy.MakeFeatureLayer_management(r"C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg/al_tuscaloosa.gpkg/main.al_tuscaloosa", "main.al_tuscaloosa")
arcpy.management.AddJoin("main.al_tuscaloosa", "ogc_fid", "zs", "ogc_fid", "KEEP_ALL")
arcpy.management.SelectLayerByAttribute("main.al_tuscaloosa", "NEW_SELECTION", "zs:MAJORITY IS NULL", None)
arcpy.env.workspace = "C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch"
arcpy.FeatureToPoint_management("main.al_tuscaloosa", "parcels_center.shp", 
                                "INSIDE")
###################################
class Computer():
    def __init__(self):
        self.name = "PC001"
        self.os = self.OS()
        self.cpu = self.CPU()
    
    class OS():
        def system(self):
            return "Windows 10"

    class CPU():
        def make(self):
            return "Intel"
        def model(self):
            return "Core-i7"


from os_work import OS
from cpu_work import CPU

class Computer():
    def __init__(self):
        self.name = "PC001"
        self.os = OS()
        self.cpu = CPU()

if __name__ == "__main__":
    my_comp = Computer()
    my_os = my_comp.os
    my_cpu = my_comp.cpu
    print(my_comp.name)
    print(my_os.system())
    print(my_cpu.make())
    print(my_cpu.model())
