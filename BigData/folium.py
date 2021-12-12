import folium


m = folium.Map(location=[45.5236, -122.6750])

m

m.save("index.html")
folium.Map(location=[45.5236, -122.6750], zoom_start=13)

folium.Map(location=[45.5236, -122.6750],
           tiles='Mapbox',
           API_key='your.API.key')
folium.Map(location=[45.372, -121.6972],
           zoom_start=12,
           tiles='http://{s}.tiles.yourtiles.com/{z}/{x}/{y}.png',
           attr='My Data Attribution')

ax = sns.heatmap(flights, annot=True, fmt="d")
ax = sns.heatmap(flights, linewidths=.5)

ax = sns.heatmap(flights, cmap="YlGnBu")
ax = sns.heatmap(flights, center=flights.loc["Jan", 1955])

data = np.random.randn(50, 20)
ax = sns.heatmap(data, xticklabels=2, yticklabels=False)
ax = sns.heatmap(flights, cbar=False)

grid_kws = {"height_ratios": (.9, .05), "hspace": .3}
f, (ax, cbar_ax) = plt.subplots(2, gridspec_kw=grid_kws)
ax = sns.heatmap(flights, ax=ax,
                 cbar_ax=cbar_ax,
                 cbar_kws={"orientation": "horizontal"})

corr = np.corrcoef(np.random.randn(10, 200))
mask = np.zeros_like(corr)
mask[np.triu_indices_from(mask)] = True
with sns.axes_style("white"):
    f, ax = plt.subplots(figsize=(7, 5))
    ax = sns.heatmap(corr, mask=mask, vmax=.3, square=True)
