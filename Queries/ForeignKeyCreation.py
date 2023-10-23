fk_cab_table = '''ALTER TABLE CabBookingManagement.CAB ADD CONSTRAINT fketadr FOREIGN KEY (Driver_id) REFERENCES CabBookingManagement.DRIVER(Driver_id) ON DELETE CASCADE;'''

fk_user_table = '''ALTER TABLE CabBookingManagement.USER_TBL ADD CONSTRAINT fkusta FOREIGN KEY (Cab_id) REFERENCES CabBookingManagement.CAB(Cab_id) ON DELETE CASCADE;'''

fk_trip_data_driver_id_table = '''ALTER TABLE CabBookingManagement.TRIP_DETAILS ADD CONSTRAINT fktddr FOREIGN KEY (Driver_id) REFERENCES CabBookingManagement.DRIVER(Driver_id) ON DELETE CASCADE;'''

fk_trip_data_user_id_table = '''ALTER TABLE CabBookingManagement.TRIP_DETAILS ADD CONSTRAINT fktdusr FOREIGN KEY (Usr_id) REFERENCES CabBookingManagement.USER_TBL(Usr_id) ON DELETE CASCADE;'''

fk_trip_data_cab_id_table = '''ALTER TABLE CabBookingManagement.TRIP_DETAILS ADD CONSTRAINT fktdtax FOREIGN KEY (Cab_id) REFERENCES CabBookingManagement.CAB(Cab_id) ON DELETE CASCADE;'''

fk_bill_data_trip_id_table = '''ALTER TABLE CabBookingManagement.BILL_DETAILS ADD CONSTRAINT fkbdtd FOREIGN KEY (Trip_id) REFERENCES CabBookingManagement.TRIP_DETAILS(Trip_id) ON DELETE CASCADE;'''

fk_bill_data_user_id_table = '''ALTER TABLE CabBookingManagement.BILL_DETAILS ADD CONSTRAINT fkbdusr FOREIGN KEY (Usr_id) REFERENCES CabBookingManagement.USER_TBL(Usr_id) ON DELETE CASCADE;'''

fk_feedback_data_emp_id_table = '''ALTER TABLE CabBookingManagement.FEEDBACK ADD CONSTRAINT fkfbemp FOREIGN KEY (Emp_id) REFERENCES CabBookingManagement.CUSTOMER_SERVICE(Emp_id) ON DELETE CASCADE;'''

fk_feedback_data_trip_id_table = '''ALTER TABLE CabBookingManagement.FEEDBACK ADD CONSTRAINT fkfbtd FOREIGN KEY (Trip_id) REFERENCES CabBookingManagement.TRIP_DETAILS(Trip_id) ON DELETE CASCADE;'''

fk_feedback_data_user_id_table = '''ALTER TABLE CabBookingManagement.FEEDBACK ADD CONSTRAINT fkfbusr FOREIGN KEY (Usr_id) REFERENCES CabBookingManagement.USER_TBL(Usr_id) ON DELETE CASCADE;'''

fk_cab_owner_data_cab_id_table = '''ALTER TABLE CabBookingManagement.OWNER_CAB ADD CONSTRAINT fkeowtax FOREIGN KEY (Cab_id) REFERENCES CabBookingManagement.CAB(Cab_id) ON DELETE CASCADE;'''

fk_cab_owner_data_owner_id_table = '''ALTER TABLE CabBookingManagement.OWNER_CAB ADD CONSTRAINT fkeowowns FOREIGN KEY (Owner_id) REFERENCES CabBookingManagement.OWNS(Owner_id) ON DELETE CASCADE;'''

fk_individual_owner_owner_cab_id_table = '''ALTER TABLE CabBookingManagement.INDIVIDUAL ADD CONSTRAINT fkeinowns FOREIGN KEY (Owner_id) REFERENCES CabBookingManagement.OWNS(Owner_id) ON DELETE CASCADE;'''

fk_csc_owner_owner_cab_id_table = '''ALTER TABLE CabBookingManagement.CAB_SERVICE_COMPANY ADD CONSTRAINT fkecscowns FOREIGN KEY (Owner_id) REFERENCES CabBookingManagement.OWNS(Owner_id) ON DELETE CASCADE;'''
