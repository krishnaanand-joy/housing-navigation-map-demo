# Architecture

This demo converts spreadsheet-based housing navigation records into structured outputs that can support nonprofit operations.

## Workflow

```text
CSV inputs
  families_mock.csv
  landlords_mock.csv
  resources_mock.csv
  placements_mock.csv
        ↓
clean_data.py
  validates required fields
  checks relationship integrity
        ↓
build_database.py
  creates SQLite tables
  loads cleaned synthetic records
        ↓
generate_map.py
  creates placement summary
  creates Google My Maps import CSV
  creates interactive HTML map
```

## Design principles

1. **Privacy first:** no real names, addresses, case notes, or partner information.
2. **Spreadsheet compatible:** inputs remain easy for nontechnical users to understand.
3. **Structured enough to scale:** cleaned records are loaded into a relational database.
4. **Map-ready:** landlord and resource points can be plotted for planning and outreach.
5. **Case-management aware:** placements connect family needs, landlord opportunities, and next steps.

## What a private production version could add

- User login and role-based access
- Google Sheets or Airtable sync
- Encrypted database storage
- Audit logs
- Caseworker dashboard
- Reminder workflow for follow-ups
- Address-level geocoding inside a private environment
- Permissions separating client data from landlord data
