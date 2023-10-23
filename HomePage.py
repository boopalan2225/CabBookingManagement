import streamlit as st
import mysql.connector
import pandas as pd
import DbConnection as db
import Utils.DataFrameColumns as df
from streamlit_option_menu import option_menu
import CabBookingMain as booking

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Cab Booking Management 🚗</h1>", unsafe_allow_html=True)
st.title("")


# horizontal menu
selectedScreen = option_menu(None, ["Home", "User Info", "Driver & Cab Info", "Owner Info", "Trip History", "Bill Details", "Feedback", "Customer Service"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

cursor = db.getDbConnectionCursor()

def __CreateButton__(cursor):
    st.subheader("")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""
        
    col1, col2 = st.columns([0.5, 0.5])
    # Add content to the first column
    with col1:
        st.markdown("<h3 style='text-align: right;'>Book your cab and resume you trip: </h3>", unsafe_allow_html=True)
    # Add content to the second column
    with col2:
        book_cab = st.button("Book your cab", type="primary", help="Click to book your cab")

    # Create an empty list to store booking information
    booking_info = []
    close = False

    if close == False:
        with st.form(key="booking_form", clear_on_submit = False):
            # Use st.text_input to get user input
            booking_info.append(st.text_input("Enter Customer Name", key="name"))
            booking_info.append(st.text_input("Enter Customer Address", key="address"))
            booking_info.append(st.text_input("Enter Customer Contact Number", key="contact"))
            booking_info.append(st.text_input("Enter Cab Id", key="cab_id"))
            booking_info.append(st.text_input("Enter Customer Gender", key="gender"))
            booking_info.append(st.text_input("Customer Advance Amount", key="advance"))

            # Create a submit button within the form
            submit = st.form_submit_button("Submit")
            if submit:
                try:
                    advanceFloat = format(float(booking_info[5]), '.2f')
                    data = (booking_info[0], booking_info[1], booking_info[2], booking_info[3], booking_info[4], advanceFloat)
                    cursor.callproc("BOOK_CAB", data)
                    db.connection.commit()
                except Exception as err:
                    print("Error:", err)
                    
                st.write("You have entered: ")
                book_table = pd.DataFrame([booking_info], columns=df.homepage_book_column)
                st.write(book_table)
                close = st.form_submit_button("Close")

if selectedScreen == "Home":
    __CreateButton__(cursor)

elif selectedScreen == "User Info":
    booking.__UserView__(cursor)

elif selectedScreen == "Driver & Cab Info":
    # Create two columns
    col1, col2 = st.columns(2)
    # Add content to the first column
    with col1:
        booking.__DriverDataView__(cursor)
    # Add content to the second column
    with col2:
        booking.__CabDataView__(cursor)

elif selectedScreen == "Owner Info":
    # Create two columns
    col1, col2, col3, col4  = st.columns(4)
    # Add content to the first column
    with col1:
        booking.__OwnsDetailView__(cursor)
    # Add content to the second column
    with col2:
        booking.__CabOwnerView__(cursor)
    # Add content to the first column
    with col3:
        booking.__IndividualOwnerView__(cursor)
    # Add content to the second column
    with col4:
        booking.__CabServiceOwnerView__(cursor)

elif selectedScreen == "Trip History":
    booking.__PastTripView__(cursor)

elif selectedScreen == "Bill Details":
    booking.__BillDetailsView__(cursor)

elif selectedScreen == "Feedback":
    booking.__FeedbackDetailView__(cursor)

elif selectedScreen == "Customer Service":
    booking.__CustomerServiceView__(cursor)

else:
    st.write("Contact us at example@example.com")