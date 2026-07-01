"""
clean_data.py

Purpose:
Validate the synthetic CSV files before they are loaded into the database or map.

Why this matters:
In a real nonprofit housing workflow, staff may maintain data in spreadsheets.
Before using those spreadsheets for reporting, mapping, or case tracking, the
system should check that required columns exist and that linked records are valid.

Privacy note:
This script only processes fictional demo data. It does not contain or require
real client, landlord, address, phone, email, or case-note information.
"""

from pathlib import Path
import pandas as pd

# Resolve project folders relative to this script, so the script can be run
# from the repository root without hard-coding a local machine path.
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

# Required columns for each input file.
# Keeping this in one dictionary makes the validation rules easy to review
# and update as the workflow grows.
REQUIRED_COLUMNS = {
    "families_mock.csv": [
        "family_id", "household_size", "target_city", "target_zip",
        "move_in_deadline", "priority_level", "current_status", "assigned_caseworker"
    ],
    "landlords_mock.csv": [
        "landlord_id", "property_type", "city", "zip", "bedrooms",
        "rent_min", "rent_max", "accepts_vouchers", "contact_status",
        "last_contact_date", "latitude", "longitude"
    ],
    "resources_mock.csv": [
        "resource_id", "category", "resource_name", "city", "zip",
        "eligibility_notes", "latitude", "longitude"
    ],
    "placements_mock.csv": [
        "placement_id", "family_id", "landlord_id", "status", "next_step", "last_updated"
    ],
}


def load_csv(filename: str) -> pd.DataFrame:
    """Load one CSV file from the data folder."""
    path = DATA_DIR / filename

    # Fail fast with a readable message if an expected spreadsheet is missing.
    if not path.exists():
        raise FileNotFoundError(f"Missing expected data file: {path}")

    return pd.read_csv(path)


def validate_columns(filename: str, df: pd.DataFrame) -> None:
    """Confirm that a dataset contains every required column."""
    missing = [col for col in REQUIRED_COLUMNS[filename] if col not in df.columns]

    # A real deployment could log this error for staff or show it in a dashboard.
    if missing:
        raise ValueError(f"{filename} is missing required columns: {missing}")


def main() -> None:
    """Run all validation checks for the synthetic demo datasets."""
    datasets = {filename: load_csv(filename) for filename in REQUIRED_COLUMNS}

    # Check each file's schema.
    for filename, df in datasets.items():
        validate_columns(filename, df)

    families = datasets["families_mock.csv"]
    landlords = datasets["landlords_mock.csv"]
    placements = datasets["placements_mock.csv"]

    # Relationship check:
    # Every placement should point to a known synthetic family and landlord.
    unknown_families = set(placements["family_id"]) - set(families["family_id"])
    unknown_landlords = set(placements["landlord_id"]) - set(landlords["landlord_id"])

    if unknown_families:
        raise ValueError(f"Placements reference unknown family IDs: {sorted(unknown_families)}")

    if unknown_landlords:
        raise ValueError(f"Placements reference unknown landlord IDs: {sorted(unknown_landlords)}")

    print("Validation complete.")
    print(f"Families: {len(families)}")
    print(f"Landlords/properties: {len(landlords)}")
    print(f"Resources: {len(datasets['resources_mock.csv'])}")
    print(f"Placements: {len(placements)}")


if __name__ == "__main__":
    main()
