import xarray as xr
from pathlib import Path


# ============================================================
# FILE PATHS
# ============================================================

INPUT_FILE = Path(
    "data/processed/weather_features_2018_01.nc"
)

OUTPUT_DIR = Path("data/processed")

OUTPUT_FILE = OUTPUT_DIR / "ml_features_2018_01.nc"


# ============================================================
# LOAD DATA
# ============================================================

print("Loading weather feature dataset...")

ds = xr.open_dataset(
    INPUT_FILE,
    engine="netcdf4"
)

print("Data loaded successfully.")


# ============================================================
# PRECIPITATION FEATURES
# ============================================================

print("Creating rainfall accumulation features...")


# Rainfall during the previous 3 hours
ds["rainfall_3h"] = (
    ds["precipitation_mm"]
    .rolling(valid_time=3)
    .sum()
)


# Rainfall during the previous 6 hours
ds["rainfall_6h"] = (
    ds["precipitation_mm"]
    .rolling(valid_time=6)
    .sum()
)


# Rainfall during the previous 12 hours
ds["rainfall_12h"] = (
    ds["precipitation_mm"]
    .rolling(valid_time=12)
    .sum()
)


# Rainfall during the previous 24 hours
ds["rainfall_24h"] = (
    ds["precipitation_mm"]
    .rolling(valid_time=24)
    .sum()
)


# Rainfall during the previous 72 hours
ds["rainfall_72h"] = (
    ds["precipitation_mm"]
    .rolling(valid_time=72)
    .sum()
)


# ============================================================
# PRESSURE CHANGE
# ============================================================

print("Creating pressure-change features...")


# Pressure change over 3 hours
ds["pressure_change_3h"] = (
    ds["pressure_pa"]
    - ds["pressure_pa"].shift(valid_time=3)
)


# Pressure change over 6 hours
ds["pressure_change_6h"] = (
    ds["pressure_pa"]
    - ds["pressure_pa"].shift(valid_time=6)
)


# ============================================================
# TEMPERATURE CHANGE
# ============================================================

print("Creating temperature-change features...")


# Temperature change over 6 hours
ds["temperature_change_6h"] = (
    ds["temperature_c"]
    - ds["temperature_c"].shift(valid_time=6)
)


# ============================================================
# WIND CHANGE
# ============================================================

print("Creating wind-change features...")


# Wind-speed change over 6 hours
ds["wind_change_6h"] = (
    ds["wind_speed"]
    - ds["wind_speed"].shift(valid_time=6)
)


# ============================================================
# REMOVE INITIAL NaN VALUES
# ============================================================

print("Removing incomplete initial time steps...")

ds = ds.dropna(
    dim="valid_time"
)


# ============================================================
# SAVE
# ============================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

ds.to_netcdf(
    OUTPUT_FILE
)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n========================================")
print("ML FEATURES CREATED")
print("========================================")

print(ds)

print("\n===== VARIABLES =====")

for variable in ds.data_vars:
    print(variable)

print("\nSaved to:")
print(OUTPUT_FILE)

print("\nFeature engineering completed successfully!")