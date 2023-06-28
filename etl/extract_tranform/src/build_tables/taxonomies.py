from ..airtable_client import build_dict, add_dpmgid
from ...data.hsds_columns import taxonomy_columns

required= ['id', 'name', 'description']

def rename_columns(core_dict: list) -> list:
    for record in core_dict:
        if 'term' in record.keys():
            record['name'] = record['term']
        if 'x-taxonomies' in record.keys():
            record['taxonomy_id'] = record['x-taxonomies']
    return core_dict

def delete_columns(core_dict):
    for record in core_dict:
        for k, v in list(record.items()):
            if k not in taxonomy_columns:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict):
    for record in core_dict:
        for required_key in required:
            if required_key not in record.keys():
                record[required_key] = ' '
    return core_dict

def complete_table():
    taxonomy_table = build_dict('x-taxonomies')
    taxonomy_hsds = rename_columns(taxonomy_table)
    taxonomy_with_deletes = delete_columns(taxonomy_hsds)
    taxonomies = add_required_if_missing(taxonomy_with_deletes)
    taxonomies_with_dpmgid = add_dpmgid(taxonomies)
    return taxonomies_with_dpmgid