import xarray as xr


# ============================================================
# INSPECT INSTANTANEOUS DATA
# ============================================================

print("Loading instantaneous data...")

instant = xr.open_dataset(
    "data/raw/era5_instantaneous_2018_01.nc"
)

print("\n===== INSTANTANEOUS DATA =====")
print(instant)


# ============================================================
# INSPECT PRECIPITATION DATA
# ============================================================

print("\nLoading precipitation data...")

precipitation = xr.open_dataset(
    "data/raw/era5_precipitation_2018_01.nc"
)

print("\n===== PRECIPITATION DATA =====")
print(precipitation)


# ============================================================
# PRECIPITATION VARIABLES
# ============================================================

print("\n===== PRECIPITATION VARIABLES =====")

for variable in precipitation.data_vars:
    print(variable)


# ============================================================
# PRECIPITATION ATTRIBUTES
# ============================================================

print("\n===== PRECIPITATION ATTRIBUTES =====")

tp = precipitation["tp"]

print(tp.attrs)


# ============================================================
# COORDINATES
# ============================================================

print("\n===== PRECIPITATION COORDINATES =====")

for coordinate in precipitation.coords:
    print(coordinate)
    print(precipitation[coordinate].values)


print("\nInspection completed.")