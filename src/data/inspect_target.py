import xarray as xr
import numpy as np


# ============================================================
# LOAD TARGET DATA
# ============================================================

INPUT_FILE = "data/processed/target_rainfall_2018_01.nc"

print("Loading target dataset...")

ds = xr.open_dataset(INPUT_FILE)

rainfall = ds["future_rainfall_6h"]


# ============================================================
# CALCULATE PERCENTILES
# ============================================================

percentiles = [50, 75, 90, 95, 99]

print()
print("Future 6-hour rainfall percentiles:")
print()

for percentile in percentiles:
    value = rainfall.quantile(percentile / 100).item()

    print(f"{percentile}th percentile: {value:.3f} mm")


# ============================================================
# BASIC INFORMATION
# ============================================================

print()
print("Minimum:", float(rainfall.min()))
print("Maximum:", float(rainfall.max()))
print("Mean:", float(rainfall.mean()))


# ============================================================
# COUNT EXTREME EVENTS
# ============================================================

threshold = rainfall.quantile(0.95)

extreme_count = int((rainfall >= threshold).sum())
total_count = rainfall.size

percentage = (extreme_count / total_count) * 100

print()
print("95th percentile threshold:", float(threshold))
print("Extreme rainfall observations:", extreme_count)
print("Total observations:", total_count)
print(f"Percentage classified as extreme: {percentage:.2f}%")