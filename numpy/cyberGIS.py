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
