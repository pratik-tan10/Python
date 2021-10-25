#To display within the notebook
%matplotlib inline

#plot 0 - 9
plt.plot(range(10))

plt.plot(range(10), 'r--', markersize = 10, label = 'inc')
plt.legend()

plt.plot(range(1)[::-1], 'b*:', label = 'dec')
plt.plot([4.5]*10, 'gx-', label = 'fix')
plt.plot(range(10), 'ko-', label = 'ver')
plt.legend();

plt.plot(range(10))
plt.gca().add_patch(patches.Circle((5,5),2, edgecolor = 'red', facecolor = 'cyan'))
plt.gca().add_patch(patches.rectangle((0,0),9,9, linewidth = 10, edgecolor = 'cyan'))

plt.figure(figsize = (6,5))

mu, sigma = 150, 20
x = mu +sigma*np.random.rand(10000)

n,bins,_ = plt.hist(x,10, density = 1, facecolor = 'g', alpha = 0.75)
plt.xlabel('Value', fontsize = 22)
plt.ylabel('Probability', fontsize = 22)
plt.title('Histogram', fontsize = 22)
plt.tick_params(labelsize = 20)
plt.text(100, 0.25, r'$\mu = 150, \ \sigma = 20$', fontsize = 22)
plt.axis([75,225,0,0.03])
plt.grid(True)

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cf

ax = plt.axes(projection = cccrs.AlbersEqualArea())
ax.add_feature(cf.COASTLINE)
ax.set_title("Coastline")

ax = plt.axes(projection = ccrs.Mercator())
ax.add_feature(cf.COASTLINE)
ax.add_feature(cf.BORDERS)
ax.add_feature(cf.OCEAN)
ax.add_feature(cf.LAKES)
ax.set_title("WORLD")
ax.figure.set_size_inches(9,7.5)

rivers_50m = cf.NaturalEarthFeature('physical', 'rivers_lake_centerlines', '50m')
land_50m = cf.NautralEarthFeature('physical', 'land', '50m', edgecolor = 'face', facecolor = cf.COLORS['land'])
ax = plt.axes(projection = ccrs.Mercator())
ax.add_feature(land_50m)
ax.add_feature(rivers_50m)
ax.set_title("Natural Earth")
ax.figure.set_size_inches(6,5)

central_lon, central_lat = -105, 40
extent = [-130, 30, -80, 50]
ax = plt.axes(projection = ccrs.Orthographic(central_lon, central_lat))
ax.set_extent(extent)
ax.gridlines()
ax.coastlines(resolution = '50m')
ax.add_fefature(cf.BORDERS)
ax.figure.set_size_inches(12,10)

new_york = dict(lon = -74.00, lat = 40.72)
london = dict(lon = 0.08, lat = 51.53)
extent = [-80, 39, 2, 52]

fig = plt.figure(figsize = (12,6))
ax = plt.axes(projection = ccrs.PlateCarree())

ax.set_extent(extent)
ax.gridlines()
ax.coastlines(resolution = '50m')

plt.title('Great Circle V/S straight line from New York to London')

lons = [new_york['lon'], london['lon']]
lats = [new_york['lat'], london['lat']]

ax.plt(lons, lats, label = 'Equirectangular straight line')
ax.plot(lons, lats, label = 'Great Circle', transform = ccrs.Geodetic())

ax.legend()

from mpl_toolkits.basemap import Basemap
import matplotlib.patches as patches

#set up map
bmap = Basemap(width = 12000000, height = 9000000, projection = 'lcc', \
               resolution = 'c', lat_1=45., lat_2 = 55, lat0 = 50, lon_0 = -107.0)
bmap.drawcoastlines()
bmap.drawmapboundary(fill_color = 'lightblue')

#fill continents, set lake color same as ocean color
bmap.fillcontinents(color = 'lightgreen', lake_color = 'lightblue')

#blue marble
bmap = Basemap(projection = 'robin', lon_0 = -0.)
bmap.bluemarble()

#ETOPO1 Global Relief Model
bmap = Basemap(width = 12000000, height = 9000000, projection = 'lcc',
               resolution = None, lat_1 = 45.0, lat_3 = 55, lat_0 = 50, lon_0 =-107.)
bmap.etopo()

#setup LCC basemap
m = Basemap( width = 9000000, height = 6000000, projection = 'lcc', resoultion = 'c', lat_1 = 45., lat_2 = 55, lat_0 = 50, lon_0 =-107.)
m.drawcoastlines()
m.drawmapboundary(fill_color = 'aqua')
m.fillcontinents(color = 'coral', lake_color = 'aqua')

#draw parallels and meridians

parallels = np.arange(20., 61, 10.)
m.drawparallels(parallels, labels = [True, True, False, False])

meridianns = np.arange(220., 351., 10.)
m.drawmeridians(meridians, labels = [False, False, False, True])


