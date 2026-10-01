import cdsapi
from pathlib import Path


# ============================================================
# SETTINGS
# ============================================================

YEAR = "2018"
MONTH = "01"

DAYS = [
    "01", "02", "03", "04", "05",
    "06", "07", "08", "09", "10",
]

AREA = [10.0, 79.0, 5.5, 82.5]

OUTPUT_DIR = Path("data/raw")


# ============================================================
# DOWNLOAD HOURLY WEATHER DATA
# ============================================================

def download_weather():

    print("\n========================================")
    print("DOWNLOADING HOURLY ERA5 WEATHER DATA")
    print("========================================")

    client = cdsapi.Client()

    request = {
        "product_type": ["reanalysis"],

        "variable": [
            "2m_temperature",
            "2m_dewpoint_temperature",
            "total_precipitation",
            "mean_sea_level_pressure",
            "10m_u_component_of_wind",
            "10m_v_component_of_wind",
        ],

        "year": [YEAR],
        "month": [MONTH],
        "day": DAYS,

        # Every hour
        "time": [
            "00:00",
            "01:00",
            "02:00",
            "03:00",
            "04:00",
            "05:00",
            "06:00",
            "07:00",
            "08:00",
            "09:00",
            "10:00",
            "11:00",
            "12:00",
            "13:00",
            "14:00",
            "15:00",
            "16:00",
            "17:00",
            "18:00",
            "19:00",
            "20:00",
            "21:00",
            "22:00",
            "23:00",
        ],

        "data_format": "netcdf",
        "download_format": "unarchived",

        "area": AREA,
    }

    output_file = OUTPUT_DIR / "era5_hourly_2018_01.nc"

    print(f"Saving to: {output_file}")
    print("Starting download...")

    client.retrieve(
        "reanalysis-era5-single-levels",
        request,
        str(output_file),
    )

    print("\nDownload completed successfully!")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    download_weather()

    print("\n========================================")
    print("DONE")
    print("========================================")