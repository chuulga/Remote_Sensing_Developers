import os
import h5py
import rasterio
from rasterio.transform import from_origin

# Step 1: Specify the HDF5 file path
hdf5_file = 'test.h5'

# Step 2: Get the directory of the HDF5 file
hdf5_dir = os.path.dirname(os.path.abspath(hdf5_file))
print(f'HDF5 file directory: {hdf5_dir}')

# Step 3: Define the output path for the GeoTIFF file
output_tiff_path = os.path.join(hdf5_dir, 'output.tif')

# Step 4: Open the HDF5 file and print its structure
with h5py.File(hdf5_file, 'r') as hdf:
    print("Top-level keys:", list(hdf.keys()))  # ['All_Data', 'Data_Products']

    # Explore 'All_Data'
    all_data_group = hdf['All_Data']
    data_product = hdf['Data_Products']
    print("All_Data keys:", list(all_data_group.keys()))
    print("Data_Products keys:", list(data_product.keys()))

    # Access a dataset inside 'VIIRS-M4-SDR_All'
    viirs_group = all_data_group['VIIRS-M4-SDR_All']
    print("VIIRS-M4-SDR_All keys:", list(viirs_group.keys()))  # Check what is inside this group

    # Assuming Radiance dataset contains the image data
    dataset = viirs_group['Radiance'][:]

    # Placeholder: Manually define bounding box and pixel size if not available in the file
    lon_min, lat_max = -180.0, 90.0  # Example for global data
    pixel_size = 0.01  # Example pixel size, adjust according to actual data resolution

# Step 5: Define the GeoTIFF parameters (bounding box, resolution, etc.)
transform = from_origin(lon_min, lat_max, pixel_size, pixel_size)

# Step 6: Write data to GeoTIFF using rasterio
with rasterio.open(
        output_tiff_path,
        'w',
        driver='GTiff',
        height=dataset.shape[0],
        width=dataset.shape[1],
        count=1,
        dtype=dataset.dtype,
        crs='+proj=latlong',
        transform=transform,
) as dst:
    dst.write(dataset, 1)

print(f"GeoTIFF saved to: {output_tiff_path}")
