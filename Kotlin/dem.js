//Filter by AOI
var colxn = imageCollection.filterBounds(Alabama)

//Create Mosaic
var mosaic = colxn.mosaic().toFloat();
Map.centerObject(Alabama, 12);
Map.addLayer(mosaic, imageVisParam, 'spatial mosaic');

//Get projection info
var projection = mosaic.projection().getInfo();
print(projection)

// Export the image, specifying the CRS, transform, and region.
Export.image.toDrive({
  image: mosaic,
  description: 'ALOS30Alabama',
  crs: projection.crs,
  crsTransform: projection.transform,
  region: Alabama,
  scale: 30,
  maxPixels: 1e13
});
