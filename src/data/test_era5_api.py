import cdsapi

print("Connecting to Copernicus Climate Data Store...")

client = cdsapi.Client()

print("Connection successful!")
print("Requesting a tiny ERA5 dataset...")

dataset = "reanalysis-era5-single-levels"

request = {
    "product_type": ["reanalysis"],
    "variable": ["2m_temperature"],
    "year": ["2024"],
    "month": ["01"],
    "day": ["01"],
    "time": ["12:00"],
    "data_format": "netcdf",
}

target = "data/raw/test_era5.nc"

client.retrieve(dataset, request, target)

print("Download successful!")
print(f"Saved to: {target}")