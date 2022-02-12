require(["esri/Map", "esri/views/MapView", "esri/geometry/Point","esri/symbols/SimpleMarkerSymbol","esri/Graphic"], (Map, MapView, Point,SimpleMarkerSymbol,Graphic) => {
    const map = new Map({
        basemap: "topo-vector"
    });
	
    const view = new MapView({
        container: "viewDiv", // Reference to the view div created in step 5
        map: map, // Reference to the map object created before the view
        zoom: 10, // Sets zoom level based on level of detail (LOD)
        center: [84, 27] // Sets center point of view using longitude,latitude
    });
    
	var pt = new Point({
	  latitude: 27,
	  longitude: 84
	});
	
	var sym = new SimpleMarkerSymbol({
	  color: "red",
	  style: "square",
	  size: 12
	});
	
	var ptGraphic = new Graphic({
	  geometry:pt,
	  symbol:sym
	});
	view.graphics.add(ptGraphic);
});
