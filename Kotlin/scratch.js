require([
  "esri/Map",
  "esri/geometry/Point",
  "esri/views/MapView",
  "dojo/domReady!"
 ], function(Map, Point, 
MapView) {

  var map = new Map({
    basemap: "streets"
  });

  var pt = new Point({
    latitude: 27,
    longitude: 84
  })

  var view = new MapView({
    container: "viewDiv",
    map: map,
    zoom: 4,
    center: pt
  });
});
