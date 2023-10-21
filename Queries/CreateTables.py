create_cab_table = '''CREATE TABLE IF NOT EXISTS CAB (
   Cab_id integer NOT NULL,
   Registration_no VARCHAR(20),
   Cab_Model VARCHAR(20),
   Cab_Year DATE,
   Cab_type VARCHAR(20),
   Status VARCHAR(20),
   Driver_id integer,
   PRIMARY KEY (Cab_id),
   UNIQUE (Registration_no)
);'''

create_user_table = '''CREATE TABLE IF NOT EXISTS USER_TBL (
   Usr_id integer NOT NULL,
   F_name VARCHAR(20),
   L_name VARCHAR(20),
   Contat_no integer,
   Gender VARCHAR(10),
   Address VARCHAR(50),
   Cab_id integer,
   PRIMARY KEY (Usr_id)
);'''

create_driver_table = '''CREATE TABLE IF NOT EXISTS DRIVER (
   Driver_id integer NOT NULL,
   F_name VARCHAR(10),
   L_name VARCHAR(20),
   Gender VARCHAR(10),
   Conatct_no VARCHAR(20),
   Rating integer,
   Age integer,
   PRIMARY KEY (Driver_id)
);'''

create_existstrip_detail_table = '''CREATE TABLE IF NOT EXISTSTRIP_DETAILS (
   Trip_id integer NOT NULL,
   Trip_date DATE,
   Trip_amt decimal(10,2),
   Driver_id integer,
   Usr_id integer,
   Cab_id integer,
   Strt_time TIMESTAMP,
   End_time TIMESTAMP,
   PRIMARY KEY (Trip_id)
);'''

create_existsbill_detail_table = '''CREATE TABLE IF NOT EXISTSBILL_DETAILS (
   Bill_no integer NOT NULL,
   Bill_date DATE,
   Advance_amt decimal(10,2),
   Discount_amt decimal(10,2),
   Total_amt decimal(10,2),
   Usr_id integer,
   Trip_id integer,
   PRIMARY KEY (Bill_no),
   UNIQUE (Trip_id)
);'''

create_existscustomer_service_table = '''CREATE TABLE IF NOT EXISTSCUSTOMER_SERVICE (
   Emp_id integer NOT NULL,
   F_name VARCHAR(20),
   L_name VARCHAR(20),
   PRIMARY KEY (Emp_id)
);'''

create_existsfeedback_table = '''CREATE TABLE IF NOT EXISTSFEEDBACK (
   Fbk_id integer NOT NULL,
   Message VARCHAR(140),
   Email VARCHAR(50),
   Emp_id integer,
   Usr_id integer,
   Trip_id integer,
   PRIMARY KEY (Fbk_id),
   UNIQUE (Emp_id)
);'''

create_existsowns_table = '''CREATE TABLE IF NOT EXISTSOWNS (
   Owner_id integer NOT NULL,
   No_Cars  integer,
   PRIMARY KEY (Owner_id)
);'''

create_exists_cab_owner_table = '''CREATE TABLE IF NOT EXISTSOWNER_CAB (
   Owner_id integer NOT NULL,
   Cab_id integer,
   PRIMARY KEY (Owner_id, Cab_id)
);'''

create_exists_individual_table = '''CREATE TABLE IF NOT EXISTSINDIVIDUAL (
   Ssn integer NOT NULL,
   Name VARCHAR(20),
   Owner_id integer,
   PRIMARY KEY (Ssn)
);'''

create_exists_cab_service_table = '''CREATE TABLE IF NOT EXISTSCAB_SERVICE_COMPANY (
   Csc_id integer NOT NULL,
   Csc_name VARCHAR(20),
   Owner_id integer,
   PRIMARY KEY (Csc_id)
);'''