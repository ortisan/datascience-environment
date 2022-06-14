DROP TABLE IF EXISTS phone;
DROP TABLE IF EXISTS address;
DROP TABLE IF EXISTS person;
CREATE TABLE person (id VARCHAR(36), first_name VARCHAR(100), last_name VARCHAR(100), PRIMARY KEY (id));
CREATE TABLE phone (id VARCHAR(36), person_id VARCHAR(36), phone_number int, PRIMARY KEY (id), FOREIGN KEY (person_id) REFERENCES person(id));
CREATE TABLE address (id VARCHAR(36), person_id VARCHAR(36), line1 VARCHAR(100), line2 VARCHAR(100), zipcode VARCHAR(15), city VARCHAR(100), country VARCHAR(100), PRIMARY KEY (id), FOREIGN KEY (person_id) REFERENCES person(id));
