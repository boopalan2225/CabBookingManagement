import streamlit as st
import DbConnection as db
from streamlit_option_menu import option_menu
import CabBookingMain as booking


st.markdown("<h1 style='text-align: center;'>Cab Booking Management 🚗", unsafe_allow_html=True)
st.title("")


# horizontal menu
selectedScreen = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

cursor = db.getDbConnectionCursor()

if selectedScreen == "Home":
    booking.__CreateButton__(cursor)
elif selectedScreen == "Upload":
    booking.__CabDetailViewMain__(cursor)
elif selectedScreen == "Tasks":
    st.write("Contact us at example@example.com")
elif selectedScreen == "Settings":
    st.write("Contact us at example@example.com")