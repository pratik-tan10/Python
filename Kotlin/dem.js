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

var geometry = 
    /* color: #98ff00 */
    /* shown: false */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-88.52031250000002, 35.14490813851336],
          [-88.52031250000002, 30.03849693437951],
          [-84.78496093750002, 30.03849693437951],
          [-84.78496093750002, 35.14490813851336]]], null, false);

/// Bands of interest

var L8bands = ['B7', 'B3', 'B2']

var L7bands =['B7', 'B2', 'B1']

var L5bands = ['B7', 'B2', 'B1']



//ViszParams
var L8vis = {
  bands: L8bands,
  min: 0,
  max: 0.5,
  gamma: [0.95, 1.1, 1]
};


var L7vis = {
  bands: L7bands,
  min: 0,
  max: 0.5,
  gamma: [0.95, 1.1, 1]
};


var L5vis = {
  bands: L5bands,
  min: 0,
  max: 0.5,
  gamma: [0.95, 1.1, 1]
};

//mask clouds
function maskLandsatclouds(image) {
  var qa = image.select('BQA')
  var cloudBitMask = ee.Number(2).pow(4).int()
  var mask = qa.bitwiseAnd(cloudBitMask).eq(0)
  return image.updateMask(mask)
      .select("B.*")
      .copyProperties(image, ["system:time_start"])
}


