import xarray as xr
import numpy as np
from pathlib import Path


# ============================================================
# FILE PATHS
# ============================================================

INSTANT_FILE = Path(
    "data/raw/era5_hourly_extracted/"
    "data_stream-oper_stepType-instant.nc"
)

PRECIP_FILE = Path(
    "data/raw/era5_hourly_extracted/"
    "data_stream-oper_stepType-accum.nc"
)

OUTPUT_DIR = Path("data/processed")

OUTPUT_FILE = OUTPUT_DIR / "weather_features_2018_01.nc"


# ============================================================
# LOAD DATA
# ============================================================

print("Loading ERA5 weather data...")

instant = xr.open_dataset(
    INSTANT_FILE,
    engine="netcdf4"
)

precip = xr.open_dataset(
    PRECIP_FILE,
    engine="netcdf4"
)

print("Data loaded successfully.")


# ============================================================
# CONVERT UNITS
# ============================================================

print("Converting units...")


# Kelvin → Celsius
temperature_c = instant["t2m"] - 273.15

dewpoint_c = instant["d2m"] - 273.15


# ============================================================
# CALCULATE WIND SPEED
# ============================================================

print("Calculating wind speed...")

wind_speed = np.sqrt(
    instant["u10"] ** 2 +
    instant["v10"] ** 2
)


# ============================================================
# CONVERT PRECIPITATION
# ============================================================

print("Converting precipitation to millimeters...")

# ERA5 precipitation is stored in metres.
# 1 metre = 1000 millimetres.

precipitation_mm = precip["tp"] * 1000


# ============================================================
# CREATE COMBINED DATASET
# ============================================================

print("Combining weather variables...")

weather = xr.Dataset(
    {
        "temperature_c": temperature_c,
        "dewpoint_c": dewpoint_c,
        "pressure_pa": instant["msl"],
        "wind_speed": wind_speed,
        "precipitation_mm": precipitation_mm,
    }
)


# ============================================================
# SAVE DATASET
# ============================================================

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True
)

weather.to_netcdf(OUTPUT_FILE)


# ============================================================
# DISPLAY RESULT
# ============================================================

print("\n========================================")
print("WEATHER FEATURES CREATED")
print("========================================")

print(weather)

print("\nSaved to:")
print(OUTPUT_FILE)

print("\nFeature engineering completed successfully!")