from .build_tables import organizations, locations, services, service_at_locations, contacts, schedules, phones, taxonomy_terms, taxonomies

def load_all_tables():
    organizations_table = organizations.complete_table()
    locations_table = locations.complete_table()
    services_table = services.complete_table()
    service_at_locations_table = service_at_locations.complete_table()
    contacts_table = contacts.complete_table()
    schedules_table = schedules.complete_table()
    phones_table = phones.complete_table()
    taxonomy_terms_table = taxonomy_terms.complete_table()
    taxonomies_table = taxonomies.complete_table()
    files = [organizations_table, locations_table, services_table, service_at_locations_table,
        contacts_table, schedules_table, phones_table, taxonomies_table, taxonomy_terms_table]
    return files