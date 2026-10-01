import xarray as xr


FILE = "data/raw/era5_precipitation_2018_01.nc"


print("Loading precipitation data...")

dataset = xr.open_dataset(FILE)

tp = dataset["tp"]


print("\n===== PRECIPITATION SUMMARY =====")

print("Shape:")
print(tp.shape)

print("\nMinimum precipitation:")
print(float(tp.min()))

print("\nMaximum precipitation:")
print(float(tp.max()))

print("\nMean precipitation:")
print(float(tp.mean()))


print("\n===== FIRST GRID LOCATION =====")

sample = tp.isel(
    latitude=0,
    longitude=0
)

print(sample)


print("\n===== FIRST 20 VALUES IN MILLIMETERS =====")

for time, value in zip(
    tp.valid_time.values,
    sample.values
):
    print(
        f"{time} -> {float(value) * 1000:.4f} mm"
    )


print("\nInspection completed.")