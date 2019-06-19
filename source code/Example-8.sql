-- Example-8.sql

CREATE TABLE IF NOT EXISTS domains (
    domain_name varchar(80),
    ipaddress varchar(15) DEFAULT NULL,
    PRIMARY KEY(domain_name)
    );

CREATE TABLE IF NOT EXISTS jobs (
    domain_name varchar(80),
    job_name varchar(80),
    userid varchar(20),
    cmd varchar(256),
    PRIMARY KEY(domain_name)
    );
