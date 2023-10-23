import streamlit as st
import pandas as pd
import DbConnection as db
import Queries.CreateTables as createQuery
import Queries.InsertQuery as insertQuery
import Queries.SelectQuery as selectQuery
import Queries.ForeignKeyCreation as fk
import Utils.DataFrameColumns as df


def __CabDataView__(cursor):
    st.markdown ("<h2 style='text-align: left; '> Cab Table Data: </h3s", unsafe_allow_html=True)
    cursor.execute(selectQuery.select_cab_data_all)
    results = cursor.fetchall()
    # Print the results
    cab_table = pd.DataFrame(results, columns=df.cab_column)
    st.write(cab_table)


def __InsertCabData__(cursor):
    # Create an empty list to store booking information
    st.markdown ("<h3 style='text-align: center; '> Enter Cab Data: </h3s", unsafe_allow_html=True)
    cab_info = []
    close = False

    if close == False:
        with st.form(key="cab_form", clear_on_submit = True):
            # Use st.text_input to get user input
            cab_info.append(st.text_input("Enter Cab Id", key="user_Id"))
            cab_info.append(st.text_input("Enter Registration number", key="r_number"))
            cab_info.append(st.text_input("Enter Cab Model", key="cabModel"))
            cab_year = st.text_input("Enter Cab Year", key="cabYear")
            cab_info.append(cab_year)
            cab_info.append(st.text_input("Enter Cab type", key="cabType"))
            cab_info.append(st.text_input("Enter Status", key="status"))
            cab_info.append(st.text_input("Enter Driver id", key="driver_id"))

            # Create a submit button within the form
            addCab = st.form_submit_button("Add Cab", type = "primary")
            if addCab:
                try:
                    data = (int(cab_info[0]), cab_info[1], cab_info[2], cab_info[3], cab_info[4], cab_info[5], int(cab_info[6]))
                    cursor.execute(f'''INSERT INTO CAB (Cab_id, Registration_no, Cab_Model, Cab_Year, Cab_type, Status, Driver_id) VALUES {data}''')
                    db.connection.commit()
                except Exception as err:
                    print("Error:", err)
                    
                st.write("You have entered: ")
                book_table = pd.DataFrame([cab_info], columns=df.cab_column)
                st.write(book_table)
                close = st.form_submit_button("Close")

def __UserView__(cursor):
    st.subheader("Cab User Data:")
    cursor.execute(selectQuery.select_user_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.user_column)
    st.write(user_table)

def __DriverDataView__(cursor):
    st.markdown ("<h2 style='text-align: left; '> Driver Table Data: </h3s", unsafe_allow_html=True)
    cursor.execute(selectQuery.select_driver_data_all)
    results = cursor.fetchall()
    # Print the results
    driver_table = pd.DataFrame(results, columns=df.driver_column)
    st.write(driver_table)


def __InsertDriverData__(cursor):
    # Create an empty list to store booking information
    st.markdown ("<h3 style='text-align: center; '> Enter Driver Data: </h3s", unsafe_allow_html=True)
    driver_info = []
    close = False

    if close == False:
        with st.form(key="driver_form", clear_on_submit = False):
            # Use st.text_input to get user input
            driver_info.append(st.text_input("Enter Driver Id", key="driver_Id"))
            driver_info.append(st.text_input("Enter First Name", key="dFirstName"))
            driver_info.append(st.text_input("Enter Last Name", key="dLastName"))
            driver_info.append(st.text_input("Enter Gender", key="dGender"))
            driver_info.append(st.text_input("Enter Contact Number", key="cNumber"))
            driver_info.append(st.text_input("Enter Rating", key="rating"))
            driver_info.append(st.text_input("Enter Age", key="age"))

            # Create a submit button within the form
            addDriver = st.form_submit_button("Add Driver", type = "primary")
            if addDriver:
                try:
                    data = (int(driver_info[0]), driver_info[1], driver_info[2], driver_info[3], driver_info[4], int(driver_info[5]), int(driver_info[6]))
                    cursor.execute(f'''INSERT INTO DRIVER VALUES {data}''')
                    db.connection.commit()
                except Exception as err:
                    print("Error:", err)
                    
                st.write("You have entered: ")
                driver_table = pd.DataFrame([driver_info], columns=df.driver_column)
                st.write(driver_table)
                close = st.form_submit_button("Close")


def __getCabAndDriverView__(cursor):
    col1, col2 = st.columns([0.5, 0.5])
        # Add content to the first column
    with col1:
        __DriverDataView__(cursor)    
    
    with col2:
        __CabDataView__(cursor)

def __inputCabAndDriverView__(cursor):
    col1, col2 = st.columns([0.5, 0.5])
        # Add content to the first column
    with col1:
        __InsertDriverData__(cursor)    
    
    with col2:
        __InsertCabData__(cursor)

def __PastTripView__(cursor):
    st.subheader("Past Trip Data:")
    cursor.execute(selectQuery.select_trip_data_all)
    results = cursor.fetchall()
    # Print the results
    trips_table = pd.DataFrame(results, columns=df.trip_data_column)
    st.write(trips_table)

def __BillDetailsView__(cursor):
    st.subheader("Bill Detail Data:")
    cursor.execute(selectQuery.select_bill_data_all)
    results = cursor.fetchall()
    # Print the results
    cab_table = pd.DataFrame(results, columns=df.bill_detail_column)
    st.write(cab_table)

def __CustomerServiceView__(cursor):
    st.subheader("Customer Service Data:")
    cursor.execute(selectQuery.select_customer_service_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.customer_service_column)
    st.write(user_table)

def __FeedbackDetailView__(cursor):
    st.subheader("Driver Table Data:")
    cursor.execute(selectQuery.select_feedback_data_all)
    results = cursor.fetchall()
    # Print the results
    driver_table = pd.DataFrame(results, columns=df.feedback_column)
    st.write(driver_table)

def __OwnsDetailView__(cursor):
    st.subheader("Cab and its Owner Data:")
    cursor.execute(selectQuery.select_owns_data_all)
    results = cursor.fetchall()
    # Print the results
    trips_table = pd.DataFrame(results, columns=df.owns_column)
    st.write(trips_table)

def __CabOwnerView__(cursor):
    st.subheader("Cab Owner Data:")
    cursor.execute(selectQuery.select_cab_owner_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.cab_owner_column)
    st.write(user_table)

def __IndividualOwnerView__(cursor):
    st.subheader("Individual Owners Data:")
    cursor.execute(selectQuery.select_individual_owner_data_all)
    results = cursor.fetchall()
    # Print the results
    driver_table = pd.DataFrame(results, columns=df.individual_owner_column)
    st.write(driver_table)

def __CabServiceOwnerView__(cursor):
    st.subheader("Cab Service Owner Data:")
    cursor.execute(selectQuery.select_cab_serice_owner_data_all)
    results = cursor.fetchall()
    # Print the results
    trips_table = pd.DataFrame(results, columns=df.cab_service_owner_column)
    st.write(trips_table)

def __CreateTables__(cursor):
    cursor.execute(createQuery.create_cab_table)
    cursor.execute(createQuery.create_user_table)
    cursor.execute(createQuery.create_driver_table)
    cursor.execute(createQuery.create_trip_detail_table)
    cursor.execute(createQuery.create_bill_detail_table)
    cursor.execute(createQuery.create_customer_service_table)
    cursor.execute(createQuery.create_feedback_table)
    cursor.execute(createQuery.create_owns_table)
    cursor.execute(createQuery.create_cab_owner_table)
    cursor.execute(createQuery.create_individual_table)
    cursor.execute(createQuery.create_cab_service_table)

def __CreateFkConstraint__(cursor):
    cursor.execute(fk.fk_cab_table)
    cursor.execute(fk.fk_user_table)
    cursor.execute(fk.fk_trip_data_driver_id_table)
    cursor.execute(fk.fk_trip_data_user_id_table)
    cursor.execute(fk.fk_trip_data_cab_id_table)
    cursor.execute(fk.fk_bill_data_trip_id_table)
    cursor.execute(fk.fk_bill_data_user_id_table)
    cursor.execute(fk.fk_feedback_data_emp_id_table)
    cursor.execute(fk.fk_feedback_data_trip_id_table)
    cursor.execute(fk.fk_feedback_data_user_id_table)
    cursor.execute(fk.fk_cab_owner_data_cab_id_table)
    cursor.execute(fk.fk_cab_owner_data_owner_id_table)
    cursor.execute(fk.fk_individual_owner_owner_cab_id_table)
    cursor.execute(fk.fk_csc_owner_owner_cab_id_table)

def __ClearTablesData__(cursor):
    cursor.execute(selectQuery.delete_cab_data)
    cursor.execute(selectQuery.delete_user_data)
    cursor.execute(selectQuery.delete_driver_data)
    cursor.execute(selectQuery.delete_trip_data)
    cursor.execute(selectQuery.delete_bill_data)
    cursor.execute(selectQuery.delete_customer_service_data)
    cursor.execute(selectQuery.delete_feedback_data)
    cursor.execute(selectQuery.delete_owns_data)
    cursor.execute(selectQuery.delete_cab_owner_data)
    cursor.execute(selectQuery.delete_individual_owner_data)
    cursor.execute(selectQuery.delete_cab_serice_owner_data)

def __CabDetailViewMain__(cursor):
        __CreateTables__(cursor)
        # __ClearTablesData__(cursor)
        # __CreateFkConstraint__(cursor)    # Already added fk constraint

        __CabDataView__(cursor)
        st.write("---")
        __UserView__(cursor)
        st.write("---")
        __DriverDataView__(cursor)
        st.write("---")
        __PastTripView__(cursor)
        st.write("---")
        __BillDetailsView__(cursor)
        st.write("---")
        __CustomerServiceView__(cursor)
        st.write("---")
        __FeedbackDetailView__(cursor)
        st.write("---")
        __OwnsDetailView__(cursor)
        st.write("---")
        __CabOwnerView__(cursor)
        st.write("---")
        __IndividualOwnerView__(cursor)
        st.write("---")
        __CabServiceOwnerView__(cursor)
