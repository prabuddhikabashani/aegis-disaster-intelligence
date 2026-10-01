import xarray as xr


file_path = "data/raw/era5_test_region_2018_01.nc"

dataset = xr.open_dataset(file_path, engine="netcdf4")


print("\n===== DATASET =====")
print(dataset)


print("\n===== VARIABLES =====")

for variable in dataset.data_vars:
    print(variable)


print("\n===== DIMENSIONS =====")

for dimension, size in dataset.sizes.items():
    print(f"{dimension}: {size}")


print("\n===== TIME RANGE =====")

print("First:", dataset.valid_time.values[0])
print("Last:", dataset.valid_time.values[-1])


print("\n===== LATITUDE =====")

print("Minimum:", float(dataset.latitude.min()))
print("Maximum:", float(dataset.latitude.max()))


print("\n===== LONGITUDE =====")

print("Minimum:", float(dataset.longitude.min()))
print("Maximum:", float(dataset.longitude.max()))