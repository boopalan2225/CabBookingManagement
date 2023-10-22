import streamlit as st
import pandas as pd
import DbConnection as db
import Queries.CreateTables as createQuery
import Queries.InsertQuery as insertQuery
import Queries.SelectQuery as selectQuery
import Utils.DataFrameColumns as df


def __CabDataView__(cursor):
    st.subheader("Cab Table Data:")
    cursor.execute(createQuery.create_cab_table)
    cursor.execute(selectQuery.delete_cab_data)
    cursor.execute(insertQuery.insert_cab)
    cursor.execute(selectQuery.select_cab_data_all)
    results = cursor.fetchall()
    # Print the results
    cab_table = pd.DataFrame(results, columns=df.cab_column)
    st.write(cab_table)

def __UserView__(cursor):
    st.subheader("Cab User Data:")
    # cursor.execute("DROP TABLE CabBookingManagement.USER_TBL;")
    cursor.execute(createQuery.create_user_table)
    cursor.execute(selectQuery.delete_user_data)
    cursor.execute(insertQuery.insert_user)
    cursor.execute(selectQuery.select_user_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.user_column)
    st.write(user_table)

def __DriverDataView__(cursor):
    st.subheader("Driver Table Data:")
    cursor.execute(createQuery.create_driver_table)
    cursor.execute(selectQuery.delete_driver_data)
    cursor.execute(insertQuery.insert_driver)
    cursor.execute(selectQuery.select_driver_data_all)
    results = cursor.fetchall()
    # Print the results
    driver_table = pd.DataFrame(results, columns=df.driver_column)
    st.write(driver_table)

def __PastTripView__(cursor):
    st.subheader("Past Trip Data:")
    cursor.execute(createQuery.create_trip_detail_table)
    cursor.execute(selectQuery.delete_trip_data)
    cursor.execute(insertQuery.insert_trip_detail)
    cursor.execute(selectQuery.select_trip_data_all)
    results = cursor.fetchall()
    # Print the results
    trips_table = pd.DataFrame(results, columns=df.trip_data_column)
    st.write(trips_table)

def __BillDetailsView__(cursor):
    st.subheader("Bill Detail Data:")
    cursor.execute(createQuery.create_bill_detail_table)
    cursor.execute(selectQuery.delete_bill_data)
    cursor.execute(insertQuery.insert_bill_detail)
    cursor.execute(selectQuery.select_bill_data_all)
    results = cursor.fetchall()
    # Print the results
    cab_table = pd.DataFrame(results, columns=df.bill_detail_column)
    st.write(cab_table)

def __CustomerServiceView__(cursor):
    st.subheader("Customer Service Data:")
    # cursor.execute("DROP TABLE CabBookingManagement.USER_TBL;")
    cursor.execute(createQuery.create_customer_service_table)
    cursor.execute(selectQuery.delete_customer_service_data)
    cursor.execute(insertQuery.insert_customer_service)
    cursor.execute(selectQuery.select_customer_service_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.customer_service_column)
    st.write(user_table)

def __FeedbackDetailView__(cursor):
    st.subheader("Driver Table Data:")
    cursor.execute(createQuery.create_feedback_table)
    cursor.execute(selectQuery.delete_feedback_data)
    cursor.execute(insertQuery.insert_feedback)
    cursor.execute(selectQuery.select_feedback_data_all)
    results = cursor.fetchall()
    # Print the results
    driver_table = pd.DataFrame(results, columns=df.feedback_column)
    st.write(driver_table)

def __OwnsDetailView__(cursor):
    st.subheader("Past Trip Data:")
    cursor.execute(createQuery.create_owns_table)
    cursor.execute(selectQuery.delete_owns_data)
    cursor.execute(insertQuery.insert_owns)
    cursor.execute(selectQuery.select_owns_data_all)
    results = cursor.fetchall()
    # Print the results
    trips_table = pd.DataFrame(results, columns=df.owns_column)
    st.write(trips_table)

def __CabOwnerView__(cursor):
    st.subheader("Cab Owner Data:")
    # cursor.execute("DROP TABLE CabBookingManagement.USER_TBL;")
    cursor.execute(createQuery.create_cab_owner_table)
    cursor.execute(selectQuery.delete_cab_owner_data)
    cursor.execute(insertQuery.insert_owner_cab)
    cursor.execute(selectQuery.select_cab_owner_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.cab_owner_column)
    st.write(user_table)

def __IndividualOwnerView__(cursor):
    st.subheader("Individual Owners Data:")
    cursor.execute(createQuery.create_individual_table)
    cursor.execute(selectQuery.delete_individual_owner_data)
    cursor.execute(insertQuery.insert_individual)
    cursor.execute(selectQuery.select_individual_owner_data_all)
    results = cursor.fetchall()
    # Print the results
    driver_table = pd.DataFrame(results, columns=df.individual_owner_column)
    st.write(driver_table)

def __CabServiceOwnerView__(cursor):
    st.subheader("Cab Service Owner Data:")
    cursor.execute(createQuery.create_cab_service_table)
    cursor.execute(selectQuery.delete_cab_serice_owner_data)
    cursor.execute(insertQuery.insert_car_service_company)
    cursor.execute(selectQuery.select_cab_serice_owner_data_all)
    results = cursor.fetchall()
    # Print the results
    trips_table = pd.DataFrame(results, columns=df.cab_service_owner_column)
    st.write(trips_table)


def main():
    if db.connection.is_connected():
        print("Connected to MySQL")
        cursor = db.connection.cursor()    # Create a cursor object
        st.title("Cab Booking Management :car:")

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

        cursor.close()  # Close the cursor
        db.connection.close()
    else:
        st.write("Connection to MySQL failed")

if __name__ == "__main__":
    main()