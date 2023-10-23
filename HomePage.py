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
selectedScreen = option_menu(None, ["Home", "User Info", "Driver & Cab Info", "Owner Info", "Trip History", "Bill Details", "Feedback"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

cursor = db.getDbConnectionCursor()

def __BookingInput__(cursor):
    # Create an empty list to store booking information
    st.markdown ("<h3 style='text-align: center; '>Book your cab and resume you trip: </h3s", unsafe_allow_html=True)
    booking_info = []
    close = False

    if close == False:
        with st.form(key="booking_form", clear_on_submit = True):
            # Use st.text_input to get user input
            booking_info.append(st.text_input("Enter Customer Name", key="name"))
            booking_info.append(st.text_input("Enter Customer Address", key="address"))
            booking_info.append(st.text_input("Enter Customer Contact Number", key="contact"))
            booking_info.append(st.text_input("Enter Cab Id", key="cab_id"))
            booking_info.append(st.text_input("Enter Customer Gender", key="gender"))
            booking_info.append(st.text_input("Customer Advance Amount", key="advance"))

            # Create a submit button within the form
            submit = st.form_submit_button("Confirm & Book", type = "primary")
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


def __EndTripInput__(cursor):
    # Create an empty list to store booking information
    st.markdown ("<h3 style='text-align: center;'>End Your Trip with Memories: </h3>", unsafe_allow_html=True)
    end_trip = []
    close1 = False

    if close1 == False:
        with st.form(key="booking_form1", clear_on_submit = True):
            # Use st.text_input to get user input
            end_trip.append(st.text_input("Enter Booking Id", key="booking_id"))
            end_trip.append(st.text_input("Enter Total Discount", key="discount"))

            # Create a submit button within the form
            end_trip_submit = st.form_submit_button("End Trip", type = "primary")
            if end_trip_submit:
                try:
                    bookingId = int(end_trip[0])
                    discountFloat1 = format(float(end_trip[1]), '.2f')
                    cursor.callproc("TRIP_END", (bookingId, discountFloat1))
                    db.connection.commit()
                except Exception as err:
                    print("Error:", err)
                    
                st.write("You have entered: ")
                end_trip_table = pd.DataFrame([end_trip], columns=df.homepage_end_trip_column)
                st.write(end_trip_table)
                close1 = st.form_submit_button("Close")


def __CreateButton__(cursor):
    st.subheader("")

    if "my_input" not in st.session_state:
        st.session_state["my_input"] = ""
        
    col1, col2 = st.columns([0.5, 0.5])
    # Add content to the first column
    with col1:
        __BookingInput__(cursor)    
    
    with col2:
        __EndTripInput__(cursor)

if selectedScreen == "Home":
    __CreateButton__(cursor)

elif selectedScreen == "User Info":
    booking.__UserView__(cursor)

elif selectedScreen == "Driver & Cab Info":
    # Create two columns
    # col1, col2 = st.columns(2)
    # # Add content to the first column
    # with col1:
        booking.__getCabAndDriverView__(cursor)
        st.write("---")
    # Add content to the second column
    # with col2:
        booking.__inputCabAndDriverView__(cursor)

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

else:
    st.write("Contact us at example@example.com")