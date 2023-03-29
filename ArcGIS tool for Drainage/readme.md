This is a tool for ArcGIS pro.
Built with ArcGIS pro 2.8.0
Python version 3.4.3

This is a hydrology tool to calculate for each cell in a raster,
the area of upstream cells that drain water to it.
It takes a input elevation raster (DEM) and
outputs a raster showing drainage area value for each cell. The (underlying)step involved are:
	1.	Fill potential sinks in the DEM
	2.	Calculate Flow direction
	3.	Calculate Flow accumulation
	4.	Calculate Drainage Area
	
	D = F~ac~*Cellsize
	where,
	D = Drainage Area
	F~ac~ = Flow accumulation
	Cellsize = Area of single pixel of input raster

This tool is used to compute the total area of upstream that contribute drain water of at a location.

Input required:

Input DEM:
	A Digital Elevation model raster representing the terrain of area of interest.
	It can be in any valid raster format.

Output Raster:
	Provide the name to store the output drainage raster.
	If full path is provided, the output raster will be saved to that file.
	If only name is provided output raster will be saved in the same location as input raster file.
	If the input was a raster from a geodatabase, you should not provide file extension of output raster.
	If no file extension is provided, file will be saved as default GRID format of ArcGIS.
	Some valid file extensions are:
	•	.tif for TIFF file
	•	.img for ERDAS IMAGINE file

Demo data is included in the "Samples" folder in the same directory as the tool.
For using as a geoprocessing python tool and other things, please refer to item description metadata
within the tool from ArcGIS Pro.

Credit:
Prepared by: Pratik Dhungana
Email : pdhungana@crimson.ua.edu
As part of GY 539 Assignment

