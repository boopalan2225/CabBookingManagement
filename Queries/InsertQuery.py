insert_cab = '''INSERT INTO CAB (Cab_id, Registration_no, Cab_Model, Cab_Year, Cab_type, Status, Driver_id)
VALUES (1,'KA-15R-3367','BENZ 300',STR_TO_DATE('01 01 2017', '%m %e %Y'),'SUV','Available',1),
(2, 'AB123CD', 'Toyota Camry', '01 01 2017, 'Sedan', 'Available', 101),
(3, 'XY456ZW', 'Honda Accord', 01 01 2017, 'Sedan', 'Available', 102);'''

insert_user = '''INSERT INTO USER_TBL (Usr_id, F_name, L_name, Contat_no, Gender, Address, Cab_id)
VALUES (1, 'John', 'Doe', '1234567890', 'Male', '123 Main St', 101),
(2,'USER2','LNAME','1234560000','Male','MCCAllum','1');'''

insert_driver = '''INSERT INTO DRIVER VALUES(1,'Abhi','Gowda','Male','4693805870',5,25);'''

insert_trip_detail = '''INSERT INTO TRIP_DETAILS (Trip_id, Trip_date, Trip_amt, Driver_id, Usr_id, Cab_id, Strt_time, End_time)
VALUES
    (1, '2023-10-22', 50.75, 101, 201, 301, '2023-10-22 08:00:00', '2023-10-22 09:30:00'),
    (2, '2023-10-23', 45.50, 102, 202, 302, '2023-10-23 10:15:00', '2023-10-23 11:45:00');'''

insert_bill_detail = '''INSERT INTO BILL_DETAILS VALUES(1,STR_TO_DATE('01 01 2017','%m %e %Y'),1000.10,20.11,null,1,1);'''

insert_customer_service = '''INSERT INTO CUSTOMER_SERVICE VALUES(1,'prashuk','ajmera'), (2,'abhi','gowda');'''

insert_feedback = '''INSERT INTO FEEDBACK VALUES(1,'good','prashuk.ajmera@gmail.com',1,1,1), (2,'not so good','abhi@gmail.com',2,2,2);'''

insert_owns = '''INSERT INTO OWNS VALUES(1,1), (2,1);'''

insert_owner_cab = '''INSERT INTO OWNER_CAB (Owner_id, Cab_id) VALUES (1, 101), (2, 102), (3, 103);'''

insert_individual = '''INSERT INTO INDIVIDUAL VALUES(123,'abhi owner ind',1);'''

insert_car_service_company = '''INSERT INTO CAB_SERVICE_COMPANY VALUES (1,'abhi cab comp',2);'''