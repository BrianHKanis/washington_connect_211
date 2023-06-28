from ..airtable_client import build_dict, single_string_value_from_list, add_dpmgid
from ...data.hsds_columns import taxonomy_terms_columns

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
            if k not in taxonomy_terms_columns:
                del record[k]
    return core_dict

def add_required_if_missing(core_dict):
    for record in core_dict:
        for required_key in required:
            if required_key not in record.keys():
                record[required_key] = ' '
    return core_dict

def complete_table():
    taxonomy_terms_table = build_dict('taxonomy_terms')
    taxonomy_terms_hsds = rename_columns(taxonomy_terms_table)
    taxonomy_terms_with_deletes = delete_columns(taxonomy_terms_hsds)
    taxonomy_terms = add_required_if_missing(taxonomy_terms_with_deletes)
    taxonomy_terms_with_strings = single_string_value_from_list(taxonomy_terms, ['taxonomy_id', 'parent_id'])
    taxonomy_terms_with_dpmgid = add_dpmgid(taxonomy_terms_with_strings)
    return taxonomy_terms_with_dpmgid