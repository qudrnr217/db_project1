DROP TABLE IF EXISTS phone_info;
DROP TABLE IF EXISTS purchase_info;
DROP TABLE IF EXISTS customer_info;

CREATE TABLE phone_info(
    SSN INTEGER PRIMARY KEY,
    name VARCHAR(80),
    price VARCHAR(80),
    b_data VARCHAR(80),
    manufacturer VARCHAR(80)
);

CREATE TABLE customer_info(
    c_name VARCHAR(80),
    c_age INTEGER(80),
    c_SSN VARCHAR(80) not null,
    c_Num VARCHAR(80) PRIMARY KEY,
    c_Addr VARCHAR(80)
);


CREATE TABLE purchase_info(
    p_SSN INTEGER,
    p_name VARCHAR(80),
    p_num VARCHAR(80),
    p_addr VARCHAR(80),
    PRIMARY KEY(p_SSN,p_num),
    FOREIGN KEY(p_SSN) REFERENCES phone_info(SSN) on delete CASCADE on UPDATE CASCADE,
    FOREIGN KEY(p_num) REFERENCES customer_info(c_Num) on delete CASCADE on UPDATE CASCADE
);

-- CREATE TABLE sign_info(
--     si_name VARCHAR(80),
--     si_id VARCHAR(80),
--     si_pwd VARCHAR(80),
--     PRIMARY KEY (si_id)
-- )
