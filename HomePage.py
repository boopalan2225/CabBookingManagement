import streamlit as st
import DbConnection as db
from streamlit_option_menu import option_menu
import CabBookingMain as booking

st.set_page_config(layout="wide")
st.markdown("<h1 style='text-align: center;'>Cab Booking Management 🚗", unsafe_allow_html=True)
st.title("")


# horizontal menu
selectedScreen = option_menu(None, ["Home", "User Info", "Driver & Cab Info", "Owner Info", "Trip History", "Bill Details", "Feedback", "Customer Service"], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

cursor = db.getDbConnectionCursor()

if selectedScreen == "Home":
    booking.__CreateButton__(cursor)

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