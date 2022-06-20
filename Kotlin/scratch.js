//IMPORT SEN2 IMAGE
var S2 = ee.ImageCollection('COPERNICUS/S2_SR') 
  .filterDate('2019-09-01','2019-09-30')
  .filterBounds(poly)

// Define an index function (return only NDVI).
var NDVI = function(image) {
  return image.expression(
    '(NIR - RED) / (NIR + RED)', 
    {
      'NIR': image.select('B8'), 
      'RED': image.select('B4'), 
    }).rename('NDVI').copyProperties(image, image.propertyNames());
};

// Calculate NDVI for each image
var NDVIS2 = S2.map(NDVI)

// Empty Collection to fill
var ft = ee.FeatureCollection(ee.List([]))

var fill = function(img, ini) {
  // type cast
  var inift = ee.FeatureCollection(ini)

  // gets the values for the points in the current img
  var ft2 = img.reduceRegions(poly, ee.Reducer.first(),30)

  // gets the date of the img
  var date = img.date().format()

  // writes the date in each feature
  var ft3 = ft2.map(function(f){return f.set("date", date)})

  // merges the FeatureCollections
  return inift.merge(ft3)
}

// Iterates over the ImageCollection
var newft = ee.FeatureCollection(NDVIS2.iterate(fill, ft))

// Export
Export.table.toDrive(newft,
"anyDescription",
"anyFolder",
"anyNameYouWant")

//--------------------------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1> Window Resizing</h1>
    <h2>Press a key on keyboard</h2>
<script>
    window.addEventListener("resize", function(){
        console.log(`The window width is ${window.innerWidth}`);
        console.log(`The window height is ${window.innerHeight}`);
    });
    document.addEventListener("keydown", function(event){
        alert(`the ${event.key} key was pressed`);
    });
</script>
</body>
</html>
