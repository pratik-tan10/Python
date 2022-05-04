arcpy.MakeFeatureLayer_management(r"C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg/al_tuscaloosa.gpkg/main.al_tuscaloosa", "main.al_tuscaloosa")
arcpy.management.AddJoin("main.al_tuscaloosa", "ogc_fid", "zs", "ogc_fid", "KEEP_ALL")
arcpy.management.SelectLayerByAttribute("main.al_tuscaloosa", "NEW_SELECTION", "zs:MAJORITY IS NULL", None)
arcpy.env.workspace = "C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch"
arcpy.FeatureToPoint_management("main.al_tuscaloosa", "parcels_center.shp", 
                                "INSIDE")
###################################
# IMPORTING DATA

uri = '/Users/ep9k/Desktop/TestZipCodes/TestZipCodes.shp'
join_layer = iface.addVectorLayer(uri, 'Patients by Zip Code', 'ogr')	#adds layer to map
target_field = 'PatCNT'

def calculate_attributes():
    """Calculates values for 'PatCNT' by copying attributes from Patient_Da column
    and adds them to 'PatCNT' column in US Zip Codes table"""

    with edit(join_layer):
        for feature in join_layer.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('PatCNT'), feature['Patient_Da'])
            join_layer.updateFeature(feature)
    print(f"Attribute calculated for {target_field} field")

calculate_attributes()
