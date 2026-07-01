"""
generate_map.py

Purpose:
Generate operational outputs from the synthetic housing-navigation data.

Outputs:
1. placement_status_summary.csv
2. google_maps_import.csv
3. landlord_resource_map.html

Mapping note:
The demo uses Folium to create an interactive HTML map without requiring a
Google Maps API key. It also exports a CSV that could be imported into Google
My Maps in a private workflow.

Privacy note:
All locations are fictional demo coordinates. Do not use real client,
landlord, or address data in a public repository.
"""

from pathlib import Path
import pandas as pd
import folium

# Project paths. Everything is relative to the repo root.
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
OUTPUT_DIR = ROOT / "outputs"


def create_status_summary(placements: pd.DataFrame) -> pd.DataFrame:
    """
    Count placement records by status.

    This is a simple operational report that helps a nonprofit team see
    how many families are searching, matched, pending, or scheduled for tours.
    """
    return (
        placements.groupby("status")
        .size()
        .reset_index(name="count")
        .sort_values(["count", "status"], ascending=[False, True])
    )


def create_google_maps_import(landlords: pd.DataFrame, resources: pd.DataFrame) -> pd.DataFrame:
    """
    Combine synthetic landlord/property points and community-resource points
    into one map-ready CSV.

    The output can be imported into Google My Maps by choosing latitude and
    longitude as the location columns.
    """

    # Format landlord/property records for mapping.
    landlord_points = landlords.assign(
        point_type="Landlord/property",
        label=landlords["landlord_id"] + " - " + landlords["city"],
        description=(
            "Type: " + landlords["property_type"].astype(str)
            + "; Bedrooms: " + landlords["bedrooms"].astype(str)
            + "; Voucher status: " + landlords["accepts_vouchers"].astype(str)
            + "; Contact status: " + landlords["contact_status"].astype(str)
        ),
    )[["point_type", "label", "description", "city", "zip", "latitude", "longitude"]]

    # Format community resource records for mapping.
    resource_points = resources.assign(
        point_type="Community resource",
        label=resources["resource_name"],
        description=(
            "Category: " + resources["category"].astype(str)
            + "; Eligibility: " + resources["eligibility_notes"].astype(str)
        ),
    )[["point_type", "label", "description", "city", "zip", "latitude", "longitude"]]

    # A single combined file is easier to upload to Google My Maps.
    return pd.concat([landlord_points, resource_points], ignore_index=True)


def build_map(points: pd.DataFrame) -> folium.Map:
    """
    Build an interactive HTML map from synthetic point data.

    Blue markers represent mock landlord/property opportunities.
    Green markers represent mock community resources.
    """
    center_lat = points["latitude"].mean()
    center_lng = points["longitude"].mean()

    # Start the map near the center of the synthetic locations.
    fmap = folium.Map(location=[center_lat, center_lng], zoom_start=10)

    for _, row in points.iterrows():
        icon_color = "blue" if row["point_type"] == "Landlord/property" else "green"

        # Popup text is intentionally operational but nonsensitive.
        popup_html = f"""
        <b>{row['label']}</b><br>
        Type: {row['point_type']}<br>
        City: {row['city']}<br>
        ZIP: {row['zip']}<br>
        {row['description']}
        """

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            popup=popup_html,
            tooltip=row["label"],
            icon=folium.Icon(color=icon_color),
        ).add_to(fmap)

    return fmap


def main() -> None:
    """Generate the demo reports and map files."""
    OUTPUT_DIR.mkdir(exist_ok=True)

    landlords = pd.read_csv(DATA_DIR / "landlords_mock.csv")
    resources = pd.read_csv(DATA_DIR / "resources_mock.csv")
    placements = pd.read_csv(DATA_DIR / "placements_mock.csv")

    # 1. Placement status report
    summary = create_status_summary(placements)
    summary.to_csv(OUTPUT_DIR / "placement_status_summary.csv", index=False)

    # 2. Google My Maps import file
    map_import = create_google_maps_import(landlords, resources)
    map_import.to_csv(OUTPUT_DIR / "google_maps_import.csv", index=False)

    # 3. Standalone interactive HTML map
    fmap = build_map(map_import)
    fmap.save(OUTPUT_DIR / "landlord_resource_map.html")

    print("Generated outputs:")
    print(f"- {OUTPUT_DIR / 'placement_status_summary.csv'}")
    print(f"- {OUTPUT_DIR / 'google_maps_import.csv'}")
    print(f"- {OUTPUT_DIR / 'landlord_resource_map.html'}")


if __name__ == "__main__":
    main()
