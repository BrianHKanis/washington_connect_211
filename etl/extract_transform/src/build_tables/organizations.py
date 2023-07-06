from ..airtable_client import build_dict, rename_columns, delete_columns, add_required_if_missing

required_keys= ['id', 'name', 'description']
organizations_columns = ['id', 'name', 'alternate_name', 'description', 'email', 'website',
                         'tax_status', 'tax_id', 'year_incorporated', 'legal_status', 'logo',
                         'uri', 'parent_organization', 'funding', 'contacts',
                         'locations', 'programs', 'organization_identifiers', 'attributes'
                         'metadata']
columns_to_rename = {'url': 'website'}

def complete_table():
    org_records = build_dict('organizations')
    orgs_hsds = rename_columns(org_records, columns_to_rename)
    orgs_with_deletes = delete_columns(orgs_hsds, organizations_columns)
    orgs = add_required_if_missing(orgs_with_deletes, required_keys)
    return orgs