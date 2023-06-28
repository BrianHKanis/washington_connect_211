from build_tables.other_tables import taxonomy_terms
from data.test_data.test_data_other_tables import taxonomy_terms_dict_test




def test_rename_keys():
    assert "name" not in taxonomy_terms_dict_test[0].keys()
    taxonomy_terms.rename_columns(taxonomy_terms_dict_test)
    assert "name" in taxonomy_terms_dict_test[0].keys()

def test_delete_columns():
    assert "extra" in taxonomy_terms_dict_test[0].keys()
    taxonomy_terms.delete_columns(taxonomy_terms_dict_test)
    assert "extra" not in taxonomy_terms_dict_test[0].keys()

def test_add_required_if_missing():
    assert "id" not in taxonomy_terms_dict_test[0].keys()
    taxonomy_terms.add_required_if_missing(taxonomy_terms_dict_test)
    assert "id" in taxonomy_terms_dict_test[0].keys()

def test_complete_table():
    complete_table = taxonomy_terms.complete_table()
    assert type(complete_table) == list
    assert type(complete_table[0]) == dict