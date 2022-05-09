arcpy.MakeFeatureLayer_management(r"C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg/al_tuscaloosa.gpkg/main.al_tuscaloosa", "main.al_tuscaloosa")
arcpy.management.AddJoin("main.al_tuscaloosa", "ogc_fid", "zs", "ogc_fid", "KEEP_ALL")
arcpy.management.SelectLayerByAttribute("main.al_tuscaloosa", "NEW_SELECTION", "zs:MAJORITY IS NULL", None)
arcpy.env.workspace = "C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch"
arcpy.FeatureToPoint_management("main.al_tuscaloosa", "parcels_center.shp", 
                                "INSIDE")
###################################
def password_check(pword):
  specialChar = ['$','@','#','%']
  val = True
  
  if len(pword)<6:
    print("Insuffecient length")
    val=False
  if  not any(char.isdigit() for char in pword):
    print("Password should contain at least one digit.")
    val = False
  if not any(char.isUpper() for char in pword):
    print("Password should contain at least one uppercase letter.")
    val = Flase
  if not any(char.islower() for char in pword):
    print("Password should contain at least one lowercase character.")
    val = False
  if not any(char in specialChar for char in pword):
    print("Password should contain at least one special character.")
    val = False
  return val

# Main method
def main():
    passwd = 'Hellow'
      
    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
          
# Driver Code        
if __name__ == '__main__':
    main()
