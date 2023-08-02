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

CREATE TABLE program (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  name VARCHAR(255),
  alternate_name VARCHAR(255),
  description VARCHAR,
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

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

CREATE TABLE service_at_location (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  location_id VARCHAR(255),
  description VARCHAR,
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

CREATE TABLE location (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_type VARCHAR(255),
  url VARCHAR(255),
  organization_id VARCHAR(255),
  name VARCHAR(255),
  alternate_name VARCHAR(255),
  description VARCHAR,
  transportation VARCHAR(255),
  latitude FLOAT,
  longitude FLOAT,
  external_identifier VARCHAR(255),
  external_identifier_type VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

CREATE TABLE phone (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_id VARCHAR(255),
  service_id VARCHAR(255),
  organization_id VARCHAR(255),
  contact_id VARCHAR(255),
  service_at_location_id VARCHAR(255),
  number VARCHAR(255),
  extension VARCHAR,
  type VARCHAR(255),
  description VARCHAR,
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

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
  interval VARCHAR(255),
  byday VARCHAR(255),
  byweekno VARCHAR(255),
  bymonthday VARCHAR(255),
  byyearday VARCHAR(255),
  description VARCHAR,
  opens_at VARCHAR(255),
  closes_at VARCHAR(255),
  schedule_link VARCHAR(255),
  attending_type VARCHAR(255),
  notes VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

CREATE TABLE funding (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  organization_id VARCHAR(255),
  service_id VARCHAR(255),
  source VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

CREATE TABLE service_area (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  name VARCHAR(255),
  description VARCHAR,
  extent VARCHAR(255),
  extent_type VARCHAR(255),
  uri VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

CREATE TABLE required_document (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  document VARCHAR(255),
  uri VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

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

CREATE TABLE accessibility (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  location_id VARCHAR(255),
  description VARCHAR,
  details VARCHAR(255),
  url VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

CREATE TABLE cost_option (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  service_id VARCHAR(255),
  valid_from VARCHAR(255),
  valid_to VARCHAR(255),
  option VARCHAR(255),
  currency VARCHAR(255),
  amount FLOAT,
  amount_description VARCHAR,
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);

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

CREATE TABLE meta_table_description (
  dpmgid VARCHAR(255),
  id VARCHAR(255),
  name VARCHAR(255),
  language VARCHAR(255),
  character_set VARCHAR(255),
  source_id VARCHAR(255),
  PRIMARY KEY (dpmgid, id)
);