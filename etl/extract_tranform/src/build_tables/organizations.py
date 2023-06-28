from ..airtable_client import build_dict, add_dpmgid
from ...data.hsds_columns import organizations_columns

required= ['id', 'name', 'description']

def rename_columns(core_dict: list) -> list:
    for record in core_dict:
        if 'url' in record.keys():
            record['website'] = record['url']
    return core_dict

def delete_columns(core_dict):
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in organizations_columns:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict):
    for record in core_dict:
        for required_key in required:
            if required_key not in record.keys():
                record[required_key] = ' '
    return core_dict

def complete_table():
    org_records = build_dict('organizations')
    orgs_hsds = rename_columns(org_records)
    orgs_with_deletes = delete_columns(orgs_hsds)
    orgs = add_required_if_missing(orgs_with_deletes)
    orgs_with_dpmgid = add_dpmgid(orgs)
    return orgs_with_dpmgid