import xarray as xr
import pandas as pd
from pathlib import Path


# ============================================================
# FILE PATHS
# ============================================================

FEATURE_FILE = "data/processed/ml_features_2018_01.nc"
TARGET_FILE = "data/processed/target_rainfall_2018_01.nc"

OUTPUT_FILE = "data/processed/training_data.csv"


# ============================================================
# EXTREME RAINFALL THRESHOLD
# ============================================================

# We previously calculated the 95th percentile as approximately
# 0.911 mm of rainfall in the next 6 hours.

EXTREME_THRESHOLD = 0.9112358


# ============================================================
# LOAD DATA
# ============================================================

print("Loading feature data...")

features = xr.open_dataset(
    FEATURE_FILE,
    engine="netcdf4"
)

print("Loading target data...")

target = xr.open_dataset(
    TARGET_FILE,
    engine="netcdf4"
)


# ============================================================
# FIND COMMON TIMES
# ============================================================

print("Finding common timestamps...")

common_times = features.valid_time.values[
    features.valid_time.values <= target.valid_time.values[-1]
]

features = features.sel(valid_time=common_times)
target = target.sel(valid_time=common_times)


print("Common time points:", len(common_times))


# ============================================================
# CONVERT XARRAY DATA TO PANDAS
# ============================================================

print("Converting data to table...")

feature_df = features.to_dataframe().reset_index()

target_df = target.to_dataframe().reset_index()


# ============================================================
# MERGE FEATURES AND TARGET
# ============================================================

print("Combining features and target...")

df = pd.merge(
    feature_df,
    target_df,
    on=["valid_time", "latitude", "longitude"],
    how="inner"
)


# ============================================================
# CREATE BINARY TARGET
# ============================================================

# 0 = normal rainfall
# 1 = extreme rainfall

df["extreme_rainfall"] = (
    df["future_rainfall_6h"] >= EXTREME_THRESHOLD
).astype(int)


# ============================================================
# REMOVE MISSING VALUES
# ============================================================

df = df.dropna()


# ============================================================
# SAVE DATASET
# ============================================================

Path(OUTPUT_FILE).parent.mkdir(
    parents=True,
    exist_ok=True
)

df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ============================================================
# DISPLAY INFORMATION
# ============================================================

print()
print("========================================")
print("TRAINING DATA CREATED")
print("========================================")

print("Rows:", len(df))
print("Columns:", len(df.columns))

print()
print("Extreme rainfall distribution:")

print(
    df["extreme_rainfall"].value_counts()
)

print()
print("Extreme rainfall percentage:")

print(
    df["extreme_rainfall"].mean() * 100,
    "%"
)

print()
print("Saved to:")

print(OUTPUT_FILE)