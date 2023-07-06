from ..airtable_client import build_dict, rename_columns, delete_columns, add_required_if_missing

required_keys = ['id', 'name', 'description']
taxonomy_columns = ['id', 'name', 'description', 'uri', 'version', 'metadata']
columns_to_rename = {'term': 'name', 'x-taxonomies': 'taxonomy_id'}

def complete_table():
    taxonomy_table = build_dict('x-taxonomies')
    taxonomy_hsds = rename_columns(taxonomy_table, columns_to_rename)
    taxonomy_with_deletes = delete_columns(taxonomy_hsds, taxonomy_columns)
    taxonomies = add_required_if_missing(taxonomy_with_deletes, required_keys)
    return taxonomies