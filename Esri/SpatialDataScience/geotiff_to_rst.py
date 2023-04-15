import sys
import os
from osgeo import gdal

# Get the input and output file paths from the command line arguments
if len(sys.argv) != 3:
    print('Usage: python geotiff_to_idrisi.py [input_file] [output_file]')
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Open the input GeoTIFF file
input_ds = gdal.Open(input_file)

# Get the driver for the output file format (IDRISI .rst)
output_driver = gdal.GetDriverByName('RST')

# Get the data type of the input file
input_dtype = input_ds.GetRasterBand(1).DataType

# Convert the data type if necessary
if input_dtype == gdal.GDT_UInt16:
    temp_file = 'temp.tif'
    gdal.Translate(temp_file, input_ds, format='GTiff', outputType=gdal.GDT_Byte)
    input_ds = gdal.Open(temp_file)

# Create the output file
output_ds = output_driver.CreateCopy(output_file, input_ds)

# Close the input and output datasets
input_ds = None
output_ds = None

# Remove the temporary file if it was created
if input_dtype == gdal.GDT_UInt16:
    os.remove(temp_file)
