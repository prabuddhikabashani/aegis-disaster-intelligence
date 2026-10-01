import xarray as xr


# Open the downloaded ERA5 file
file_path = "data/raw/test_era5.nc"

dataset = xr.open_dataset(file_path)


print("\n===== DATASET =====")
print(dataset)


print("\n===== VARIABLES =====")

for variable in dataset.data_vars:
    print(variable)


print("\n===== DIMENSIONS =====")

for dimension, size in dataset.sizes.items():
    print(f"{dimension}: {size}")


print("\n===== COORDINATES =====")

for coordinate in dataset.coords:
    print(coordinate)