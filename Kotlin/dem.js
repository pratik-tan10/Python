//Filter by AOI
var colxn = imageCollection.filterBounds(Alabama)

//Create Mosaic
var mosaic = colxn.mosaic().toFloat();
Map.centerObject(Alabama, 12);
Map.addLayer(mosaic, imageVisParam, 'spatial mosaic');

//Get projection info
var projection = mosaic.projection().getInfo();
print(projection)

