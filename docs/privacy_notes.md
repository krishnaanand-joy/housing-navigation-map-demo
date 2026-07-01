# Privacy Notes

This repository is intentionally synthetic.

## What is not included

The demo does not include:

- client names
- landlord names
- street addresses
- phone numbers
- emails
- real family circumstances
- case notes
- real partner organizations
- real coordinates
- internal documents

## Why synthetic data is used

Housing-navigation workflows involve sensitive information about families, property owners, locations, eligibility, and case progress. Publishing real data could expose vulnerable families or partner relationships.

Synthetic data allows the workflow to be demonstrated without exposing private information.

## Recommended safeguards for a real deployment

A real private deployment should include:

- Role-based access controls
- Authentication
- Encrypted storage
- Encrypted backups
- Audit logs
- Data-retention policy
- Redaction rules for exports
- Clear separation between public reporting and private case data
- Training for users handling sensitive data

## Public demo rule

The public repository should show the method, not the people.
