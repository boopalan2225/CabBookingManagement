cab_column = ["Cab_id", "Registration_no", "Cab_Model", "Cab_Year", "Cab_type", "Status", "Driver_id"]

user_column = ["Usr_id", "F_name", "L_name", "Contat_no", "Gender", "Address", "Cab_id"]

driver_column = ["Driver_id", "F_name", "L_name", "Gender", "Contat_no", "Rating", "Age"]

trip_data_column = ["Trip_id", "Trip_date", "Trip_amt", "Driver_id", "Usr_id", "Cab_id", "Strt_time", "End_time"]

bill_detail_column = ["Bill_no", "Bill_date", "Advance_amt", "Discount_amt", "Total_amt", "Usr_id", "Trip_id"]

customer_service_column = ["Emp_id", "F_name", "L_name"]

feedback_column = ["Fbk_id", "Message", "Email", "Emp_id", "Usr_id", "Trip_id"]

owns_column = ["Owner_id", "No_Cars"]

cab_owner_column = ["Owner_id", "Cab_id"]

individual_owner_column = ["Ssn", "Name", "Owner_id"]

cab_service_owner_column = ["Csc_id", "Csc_name", "Owner_id"]

homepage_book_column = ["Customer Name", "Customer address", "Customer Contact Number", "Cab Id", "Gender", "Customer Advance amount"]

homepage_end_trip_column = ["Booking Id", "Total Discount"]