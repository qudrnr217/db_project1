DROP TABLE IF EXISTS phone_info;
DROP TABLE IF EXISTS purchase_info;
DROP TABLE IF EXISTS customer_info;

CREATE TABLE phone_info(
    name VARCHAR(80) PRIMARY KEY,
    price VARCHAR(80),
    b_data VARCHAR(80),
    manufacturer VARCHAR(80)
);

CREATE TABLE customer_info(
    c_name VARCHAR(80),
    c_age INTEGER(80),
    c_sex VARCHAR(80),
    c_SSN VARCHAR(80) PRIMARY KEY
);

CREATE TABLE purchase_info(
    p_name VARCHAR(80),
    p_SSN VARCHAR(80),
    FOREIGN KEY(p_name) REFERENCES phone_info(name),
    FOREIGN KEY(p_SSN) REFERENCES customer_info(c_SSN),
    PRIMARY KEY (p_name, p_SSN)
);

CREATE TABLE sign_info(
    si_name VARCHAR(80),
    si_id VARCHAR(80),
    si_pwd VARCHAR(80),
    PRIMARY KEY (si_id)
)
