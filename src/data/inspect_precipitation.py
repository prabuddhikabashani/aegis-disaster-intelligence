import xarray as xr

FILE = "data/raw/era5_extracted/data_stream-oper_stepType-accum.nc"

print("Loading precipitation data...")

dataset = xr.open_dataset(FILE)

print("\n===== PRECIPITATION DATA =====")
print(dataset)

print("\n===== PRECIPITATION VALUES =====")

tp = dataset["tp"]

# Select the first grid location
sample = tp.isel(latitude=0, longitude=0)

print(sample)

print("\n===== PRECIPITATION ATTRIBUTES =====")
print(tp.attrs)