# Data Dictionary

All fields in this demo are synthetic.

## families_mock.csv

| Field | Description |
| --- | --- |
| family_id | Synthetic family identifier |
| household_size | Number of people in household |
| target_city | Preferred city |
| target_zip | Preferred ZIP code |
| move_in_deadline | Target move-in deadline |
| priority_level | Case priority for workflow planning |
| current_status | Current housing-navigation status |
| assigned_caseworker | Synthetic caseworker identifier |

## landlords_mock.csv

| Field | Description |
| --- | --- |
| landlord_id | Synthetic landlord/property identifier |
| property_type | Mock property category |
| city | City of mock property |
| zip | ZIP code of mock property |
| bedrooms | Number of bedrooms |
| rent_min | Minimum estimated rent |
| rent_max | Maximum estimated rent |
| accepts_vouchers | Mock voucher acceptance field |
| contact_status | Outreach status |
| last_contact_date | Last synthetic contact date |
| latitude | Fake latitude used for mapping |
| longitude | Fake longitude used for mapping |

## resources_mock.csv

| Field | Description |
| --- | --- |
| resource_id | Synthetic resource identifier |
| category | Type of community resource |
| resource_name | Fictional resource name |
| city | City of mock resource |
| zip | ZIP code of mock resource |
| eligibility_notes | Synthetic notes |
| latitude | Fake latitude used for mapping |
| longitude | Fake longitude used for mapping |

## placements_mock.csv

| Field | Description |
| --- | --- |
| placement_id | Synthetic placement identifier |
| family_id | Synthetic family identifier |
| landlord_id | Synthetic landlord/property identifier |
| status | Current placement status |
| next_step | Next workflow step |
| last_updated | Date record was last updated |
