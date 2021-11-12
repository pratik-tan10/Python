data = ep.data.get_data('vignette-landsat') 

landsat_path = glob("vignette-landsat/LC08_L1TP_034032_20160621_20170221_01_T1_sr_band*_crop.tif")

landsat_path.sort()

# Stacking Bands
arr_st, meta = es.stack(landsat_path, nodata=-9999)

# Prints meta data 
for i,j in meta.items():
  print("%10s : %s"%(i, str(j)))
