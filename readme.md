# Whatcom County Airtable Connector

## About
The Whatcom County Airtable Connector retrieves data from Whatcom's Data Utility in Airtable, transforms this data as per the HSDS 3.0 Schema, then pushes it to the Whatcom Writer API. Designed to be deployed as a Dockerized container in Digital Ocean.


## USAGE
1. Install Required Libraries
pip3 install -r requirements.txt

2. Set Environmental Variables:  
    etl.extract_transform.env -> AIRTABLE_KEY, BASE_ID (Table ID)  
    etl.load_export.env -> API_WRITER_ROOT_URL (Endpoint)  

3. Run
python3 run.py

4. Debugging - Execution Time
python3 -i console.py



# To Run the program
run.py  
    - Builds and exports tables to the whatcom-writer API.    
  
console.py  
    - For testing and debugging.


## Building and Transforming Tables
extract_transform.src
    build_tables  
        - Contains information and functions specific to it's coresponding table.  
          
    airtable_client.py  
        - Contains functions for connecting to Airtable and transforming tables.  
          
    load_all.py  
        - Loads all tables in a list.  
        

## Exporting
load_export.src  
    api_export.py  
        - Merges tables with their coresponding endpoint as a dictionary then exports through a put request.  

# Architecture

![Alt text](architecture_diagram.png?raw=true "Title")
