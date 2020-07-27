import geopandas as gpd
import matplotlib.pyplot as plt

sectors = gpd.read_file("./Sector.shp")

sectors.plot()