from ..airtable_client import build_dict, single_string_value_from_list, rename_columns, delete_columns, add_required_if_missing

required_keys = ['id', 'name', 'description']
taxonomy_terms_columns = ['id', 'code', 'name', 'description', 
                          'parent_id', 'taxonomy', 'taxonomy_detail', 'language', 
                          'taxonomy_id', 'term_uri', 'metadata']
columns_to_rename = {'term': 'name', 'x-taxonomies': 'taxonomy_id'}
columns_with_lists = ['taxonomy_id', 'parent_id']

def complete_table():
    taxonomy_terms_table = build_dict('taxonomy_terms')
    taxonomy_terms_hsds = rename_columns(taxonomy_terms_table, columns_to_rename)
    taxonomy_terms_with_deletes = delete_columns(taxonomy_terms_hsds, taxonomy_terms_columns)
    taxonomy_terms = add_required_if_missing(taxonomy_terms_with_deletes, required_keys)
    taxonomy_terms_with_strings = single_string_value_from_list(taxonomy_terms, columns_with_lists)
    return taxonomy_terms_with_strings