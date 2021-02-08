from solaris.data import data_dir
import os
import skimage
import geopandas as gpd
from matplotlib import pyplot as plt
from shapely.ops import cascaded_union

image = skimage.io.imread(os.path.join(data_dir, 'sample_geotiff.tif'))
f, axarr = plt.subplots(figsize=(10, 10))
plt.imshow(image, cmap='gray')

#gdf = gpd.read_file(os.path.join(data_dir, 'geotiff_labels.geojson'))
#cascaded_union(gdf.geometry.values)
