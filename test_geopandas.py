import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Maak een lijst van punten (bijv. coördinaten van steden)
geometry = [Point(4.9, 52.4), Point(5.1, 52.0), Point(6.6, 53.2)]
data = {'city': ['Amsterdam', 'Utrecht', 'Groningen']}

gdf = gpd.GeoDataFrame(data, geometry=geometry)

print(gdf)
gdf.plot()
plt.show()