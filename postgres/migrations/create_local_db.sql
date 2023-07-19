-- Create table for Organization
DROP TABLE IF EXISTS organization;
CREATE TABLE organization (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  name VARCHAR(255),
  alternate_name VARCHAR(255),
  description VARCHAR,
  email VARCHAR(255),
  website VARCHAR(255),
  tax_status VARCHAR(255),
  tax_id VARCHAR(255),
  year_incorporated BIGINT,
  legal_status VARCHAR(255),
  logo VARCHAR(255),
  uri VARCHAR(255),
  parent_organization_id VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for OrganizationIdentifier
DROP TABLE IF EXISTS organization_identifier;
CREATE TABLE organization_identifier (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  identifier_scheme VARCHAR(255),
  identifier_type VARCHAR(255),
  identifier VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Program
DROP TABLE IF EXISTS program;
CREATE TABLE program (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  name VARCHAR(255),
  alternate_name VARCHAR(255),
  description VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Service
DROP TABLE IF EXISTS service;
CREATE TABLE service (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  program_id VARCHAR(255),
  name VARCHAR(255),
  alternate_name VARCHAR(255),
  description VARCHAR,
  url VARCHAR(255),
  email VARCHAR(255),
  status VARCHAR(255),
  interpretation_services VARCHAR(255),
  application_process VARCHAR,
  fees_description VARCHAR(255),
  wait_time VARCHAR(255),
  fees VARCHAR(255),
  accreditations VARCHAR(255),
  eligibility_description VARCHAR(255),
  minimum_age BIGINT,
  maximum_age BIGINT,
  assured_date VARCHAR(255),
  assurer_email VARCHAR(255),
  licenses VARCHAR(255),
  alert VARCHAR(255),
  last_modified VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Attribute
DROP TABLE IF EXISTS attribute;
CREATE TABLE attribute (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  link_id VARCHAR(255),
  taxonomy_term_id VARCHAR(255),
  link_type VARCHAR(255),
  link_entity VARCHAR(255),
  value VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for ServiceAtLocation
DROP TABLE IF EXISTS service_at_location;
CREATE TABLE service_at_location (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  location_id VARCHAR(255),
  description VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Location
DROP TABLE IF EXISTS location;
CREATE TABLE location (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_type VARCHAR(255),
  url VARCHAR(255),
  organization_id VARCHAR(255),
  name VARCHAR(255),
  alternate_name VARCHAR(255),
  description VARCHAR(255),
  transportation VARCHAR(255),
  latitude FLOAT,
  longitude FLOAT,
  external_identifier VARCHAR(255),
  external_identifier_type VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Phone
DROP TABLE IF EXISTS phone;
CREATE TABLE phone (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_id VARCHAR(255),
  service_id VARCHAR(255),
  organization_id VARCHAR(255),
  contact_id VARCHAR(255),
  service_at_location_id VARCHAR(255),
  number VARCHAR(255),
  extension BIGINT,
  type VARCHAR(255),
  description VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Contact
DROP TABLE IF EXISTS contact;
CREATE TABLE contact (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  service_id VARCHAR(255),
  service_at_location_id VARCHAR(255),
  location_id VARCHAR(255),
  name VARCHAR(255),
  title VARCHAR(255),
  department VARCHAR(255),
  email VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Address
DROP TABLE IF EXISTS address;
CREATE TABLE address (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_id VARCHAR(255),
  attention VARCHAR(255),
  address_1 VARCHAR(255),
  address_2 VARCHAR(255),
  city VARCHAR(255),
  region VARCHAR(255),
  state_province VARCHAR(255),
  postal_code VARCHAR(255),
  country VARCHAR(255),
  address_type VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Schedule
DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  location_id VARCHAR(255),
  service_at_location_id VARCHAR(255),
  valid_from VARCHAR(255),
  valid_to VARCHAR(255),
  dtstart VARCHAR(255),
  timezone FLOAT,
  until VARCHAR(255),
  count BIGINT,
  wkst VARCHAR(255),
  freq VARCHAR(255),
  interval BIGINT,
  byday VARCHAR(255),
  byweekno VARCHAR(255),
  bymonthday VARCHAR(255),
  byyearday VARCHAR(255),
  description VARCHAR(255),
  opens_at VARCHAR(255),
  closes_at VARCHAR(255),
  schedule_link VARCHAR(255),
  attending_type VARCHAR(255),
  notes VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Funding
DROP TABLE IF EXISTS funding;
CREATE TABLE funding (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  service_id VARCHAR(255),
  source VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for ServiceArea
DROP TABLE IF EXISTS service_area;
CREATE TABLE service_area (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR(255),
  extent VARCHAR(255),
  extent_type VARCHAR(255),
  uri VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for RequiredDocument
DROP TABLE IF EXISTS required_document;
CREATE TABLE required_document (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  document VARCHAR(255),
  uri VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Language
DROP TABLE IF EXISTS language;
CREATE TABLE language (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  location_id VARCHAR(255),
  phone_id VARCHAR(255),
  name VARCHAR(255),
  code VARCHAR(255),
  note VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Accessibility
DROP TABLE IF EXISTS accessibility;
CREATE TABLE accessibility (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_id VARCHAR(255),
  description VARCHAR(255),
  details VARCHAR(255),
  url VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for CostOption
DROP TABLE IF EXISTS cost_option;
CREATE TABLE cost_option (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  valid_from VARCHAR(255),
  valid_to VARCHAR(255),
  option VARCHAR(255),
  currency VARCHAR(255),
  amount FLOAT,
  amount_description VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Taxonomy
DROP TABLE IF EXISTS taxonomy;
CREATE TABLE taxonomy (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR(255),
  uri VARCHAR(255),
  version VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for TaxonomyTerm
DROP TABLE IF EXISTS taxonomy_term;
CREATE TABLE taxonomy_term (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  code VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR,
  parent_id VARCHAR(255),
  taxonomy VARCHAR(255),
  language VARCHAR(255),
  taxonomy_id VARCHAR(255),
  term_uri VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for Metadata
DROP TABLE IF EXISTS metadata;
CREATE TABLE metadata (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  resource_id VARCHAR(255),
  resource_type VARCHAR(255),
  last_action_date VARCHAR(255),
  last_action_type VARCHAR(255),
  field_name VARCHAR(255),
  previous_value VARCHAR(255),
  replacement_value VARCHAR(255),
  updated_by VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

-- Create table for MetaTableDescription
DROP TABLE IF EXISTS meta_table_description;
CREATE TABLE meta_table_description (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  name VARCHAR(255),
  language VARCHAR(255),
  character_set VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);