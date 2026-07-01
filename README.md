# Housing Navigation Map Demo

A privacy-preserving demo for turning nonprofit housing spreadsheets into a private database, map, and case-tracking workflow.

This project is a fictional mockup inspired by nonprofit housing-navigation workflows. It does **not** contain client, landlord, partner, address, or case data from any real organization. All data in this repository is synthetic and created only for demonstration.

## Why this project exists

Nonprofit housing programs often begin with spreadsheets: families needing housing, landlords who may have available units, community resources, placement statuses, and caseworker notes.

Those spreadsheets can become difficult to manage as the program grows. This demo shows how a spreadsheet-based workflow can be converted into a more structured and privacy-aware system:

```text
Mock spreadsheets
        ↓
Data cleaning and validation
        ↓
Private SQLite database
        ↓
Placement summaries
        ↓
Map-ready outputs
        ↓
Interactive demo map
```

## What the demo does

The demo:

1. Loads mock CSV files for families, landlords, resources, and placements.
2. Validates key fields and checks relationships between files.
3. Builds a local SQLite database.
4. Creates a placement status summary.
5. Creates a Google My Maps import file.
6. Generates an interactive HTML map showing mock landlord and resource locations.

## Repository structure

```text
housing-navigation-map-demo/
│
├── README.md
├── data/
│   ├── families_mock.csv
│   ├── landlords_mock.csv
│   ├── resources_mock.csv
│   └── placements_mock.csv
│
├── src/
│   ├── clean_data.py
│   ├── build_database.py
│   └── generate_map.py
│
├── outputs/
│   ├── housing_navigation_demo.db
│   ├── landlord_resource_map.html
│   ├── google_maps_import.csv
│   └── placement_status_summary.csv
│
└── docs/
    ├── architecture.md
    ├── data_dictionary.md
    ├── google_my_maps_import.md
    └── privacy_notes.md
```

## Data model

The demo uses four synthetic datasets:

- `families_mock.csv`: family IDs, household size, target geography, deadline, priority, and caseworker assignment.
- `landlords_mock.csv`: mock property availability, rent range, voucher status, contact status, and fake coordinates.
- `resources_mock.csv`: mock community resources with categories and fake coordinates.
- `placements_mock.csv`: placement links between families and landlords with status and next step.

No names, phone numbers, email addresses, real addresses, real landlord names, or client stories are included.

## How to run

Install dependencies:

```bash
pip install pandas folium
```

Run the workflow from the repository root:

```bash
python src/clean_data.py
python src/build_database.py
python src/generate_map.py
```

Then open:

```text
outputs/landlord_resource_map.html
```

in a browser.

## Example outputs

- `outputs/housing_navigation_demo.db`: local SQLite database for the synthetic demo.
- `outputs/placement_status_summary.csv`: count of placements by status.
- `outputs/google_maps_import.csv`: map-ready CSV for importing synthetic points into Google My Maps.
- `outputs/landlord_resource_map.html`: interactive HTML map generated from mock data.

## Privacy approach

This project is designed around the idea that nonprofit housing data should be private by default.

The public demo avoids:

- client names
- landlord names
- addresses
- phone numbers
- emails
- case notes
- real family circumstances
- real partner identities
- exact locations tied to sensitive cases

In a real deployment, this workflow would need access controls, audit logs, role-based permissions, encryption, and clear data-retention rules.

## Skills demonstrated

- Spreadsheet-to-database workflow design
- Data cleaning and validation
- SQLite database design
- Map-based operations support
- Public-sector and nonprofit workflow modeling
- Privacy-aware system design
- Technical communication for nontechnical users

## Portfolio note

This project demonstrates how a sensitive real-world service workflow can be represented publicly without exposing private data. The goal is to show the structure, design thinking, and technical approach while protecting people and partners.
