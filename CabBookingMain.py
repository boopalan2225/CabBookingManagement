import streamlit as st
import pandas as pd
import DbConnection as db
import Queries.CreateTables as createQuery
import Queries.InsertQuery as insertQuery
import Queries.SelectQuery as selectQuery
import Utils.DataFrameColumns as df


def __FirstView__(cursor):
    st.subheader("Cab Table Date:")
    cursor.execute(selectQuery.delete_cab_data)
    cursor.execute(createQuery.create_cab_table)
    cursor.execute(insertQuery.insert_cab)
    cursor.execute(selectQuery.select_cab_data_all)
    results = cursor.fetchall()
    # Print the results
    cab_table = pd.DataFrame(results, columns=df.cab_column)
    st.write(cab_table)

def __SecondView__(cursor):
    st.subheader("Cab User Date:")
    cursor.execute(selectQuery.delete_user_data)
    # cursor.execute("DROP TABLE CabBookingManagement.USER_TBL;")
    cursor.execute(createQuery.create_user_table)
    cursor.execute(insertQuery.insert_user)
    cursor.execute(selectQuery.select_user_data_all)
    results = cursor.fetchall()
    # Print the results
    user_table = pd.DataFrame(results, columns=df.user_column)
    st.write(user_table)

def main():
    if db.connection.is_connected():
        print("Connected to MySQL")
        cursor = db.connection.cursor()    # Create a cursor object
        st.title("Cab Booking Management :car:")

        __FirstView__(cursor)
        st.write("---")
        __SecondView__(cursor)

        cursor.close()  # Close the cursor
        db.connection.close()
    else:
        st.write("Connection to MySQL failed")

if __name__ == "__main__":
    main()