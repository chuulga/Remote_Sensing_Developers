import os
import imageio
import imageio.v2 as imageio
import numpy as np
import geopandas as gpd
import pandas
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.pyplot as mplot
import matplotlib.image as mpimg
import matplotlib.colors as colors
from matplotlib.colors import ListedColormap
import rasterio
from  rasterio.plot import show, show_hist

inDir = "/Users/munkhchuulgaenkhbayar/Documents/Machine Learning/NDVI/images"
os.chdir(inDir)
outDir = os.path.normpath(os.path.split(inDir)[0] + os.sep + 'animation') + '/'
if not os.path.exists((outDir)): os.makedirs((outDir))

fileList = [file for file in os.listdir() if file.endswith('.tif')]
for f in fileList:
    lcpri_file = rasterio.open(f)
    lcpri = lcpri_file.read(1)

    cmap = "YlGn"
    cmap_reversed = matplotlib.cm.get_cmap('YlGn_r')
    plt.figure(figsize=(20,15))
    plt.imshow(lcpri, cmap=cmap, vmin= 1, vmax= -1)
    parts = f.split("_")
    fileName = parts[1][:-4]
    print("Processing:  {}" .format((fileName)))
    plt.title('NDVI' + '' + fileName, fontsize = 28, fontweight = 'bold')
    cur_axes = mplot.gca()
    cur_axes.axes.get_xaxis().set_visible(False)
    cur_axes.axes.get_yaxis().set_visible(False)
    cb = plt.colorbar()
    cb.set_label('NDVI Time Series', size= 24)
    cb.ax.tick_params(labelsize = 18)
    plt.tight_layout()
    plt.savefig('{} {}_NDVI.png'.format(outDir, fileName, dpi=150))
    plt.close()
