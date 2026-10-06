import xarray as xr
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

INPUT_FILE = Path("data/processed/weather_features_2018_01.nc")
OUTPUT_FILE = Path("data/processed/target_rainfall_2018_01.nc")


# ============================================================
# LOAD DATA
# ============================================================

print("Loading weather dataset...")

ds = xr.open_dataset(INPUT_FILE)

print("Dataset loaded.")
print(ds)


# ============================================================
# GET HOURLY PRECIPITATION
# ============================================================

precipitation = ds["precipitation_mm"]


# ============================================================
# CALCULATE FUTURE 6-HOUR RAINFALL
# ============================================================
#
# At time t:
#
# future_rainfall_6h =
#     rainfall(t+1)
#   + rainfall(t+2)
#   + rainfall(t+3)
#   + rainfall(t+4)
#   + rainfall(t+5)
#   + rainfall(t+6)
#
# This means the model only uses the weather at time t
# to predict what happens during the following 6 hours.
# ============================================================

future_rainfall_6h = (
    precipitation.shift(valid_time=-1)
    + precipitation.shift(valid_time=-2)
    + precipitation.shift(valid_time=-3)
    + precipitation.shift(valid_time=-4)
    + precipitation.shift(valid_time=-5)
    + precipitation.shift(valid_time=-6)
)


# Give the variable a clear name
future_rainfall_6h.name = "future_rainfall_6h"

future_rainfall_6h.attrs["description"] = (
    "Total precipitation accumulated during the six hours "
    "following the prediction timestamp"
)

future_rainfall_6h.attrs["units"] = "mm"


# ============================================================
# CREATE OUTPUT DATASET
# ============================================================

target_ds = future_rainfall_6h.to_dataset()


# ============================================================
# REMOVE TIMES WITHOUT A COMPLETE 6-HOUR FUTURE WINDOW
# ============================================================

target_ds = target_ds.dropna(dim="valid_time", how="all")


# ============================================================
# SAVE
# ============================================================

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

target_ds.to_netcdf(OUTPUT_FILE)

print()
print("Future rainfall target created successfully!")
print(f"Saved to: {OUTPUT_FILE}")


# ============================================================
# BASIC CHECKS
# ============================================================

print()
print("Target information:")
print(target_ds)

print()
print("Statistics:")
print(target_ds["future_rainfall_6h"].to_dataframe().describe())