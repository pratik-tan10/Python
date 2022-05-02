arcpy.MakeFeatureLayer_management(r"C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch/al_tuscaloosa.gpkg/al_tuscaloosa.gpkg/main.al_tuscaloosa", "main.al_tuscaloosa")
arcpy.management.AddJoin("main.al_tuscaloosa", "ogc_fid", "zs", "ogc_fid", "KEEP_ALL")
arcpy.management.SelectLayerByAttribute("main.al_tuscaloosa", "NEW_SELECTION", "zs:MAJORITY IS NULL", None)
arcpy.env.workspace = "C:/Users/Research Lab/BoxPratik/Box Sync/Pratik/sem2/Thesis/scratch"
arcpy.FeatureToPoint_management("main.al_tuscaloosa", "parcels_center.shp", 
                                "INSIDE")
###################################
# Load libraries
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
# Load data
iris = datasets.load_iris()
X = iris.data
y = iris.target
# Standarize features
scaler = StandardScaler()
X_std = scaler.fit_transform(X)
# Create one-vs-rest logistic regression object
clf = LogisticRegression(random_state=0, multi_class='ovr')

# Train model
model = clf.fit(X_std, y)
# Create new observation
new_observation = [[.5, .5, .5, .5]]
# Predict class
model.predict(new_observation)
# View predicted probabilities
model.predict_proba(new_observation)
