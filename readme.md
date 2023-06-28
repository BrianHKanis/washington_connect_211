### USAGE --> python3 run.py ###
## To Run the program ##
run.py
   - Loads the 4 core-tables into memory and exports them into the 'data' folder.
console.py
    - Testing and debugging. Writes json data to file per core table and outputs
    time for each function in the console.


# Functions that build related tables #
build_tables
    tables.py
        - Contains table IDs and information for making get requests. Also has any general
        functions for use across all tables.
    hsds_columns.py
        - Contains the specified columns by table as per HSDS.
    core_tables
        locations.py
            - Functions for locations table.
        organizations.py
            - Functions for organizations table.
        service_at_location.py
            - Functions for service_at_location table.
        services.py
            - Functions for services table.

# Output and for testing #
data
- Contains the outputted core tables in .json format.
    test_data
        - Test data for testing all functions

# Tests #
tests
    test_tables.py
        - For testing general fucntions in the tables.py file. 
    test_core_tables
        - For testing the 4 core tables.
    test_other_tables
        - For testing all other tables.
