import streamlit as st
from streamlit_option_menu import option_menu
from home import Home
from planty import Planty
from shop import Shop
from contact import Contact

# Set up page configuration
st.set_page_config(page_title="Tomato System", page_icon="🍅", layout="wide")

# Navigation Menu
select = option_menu(
    menu_title='',
    options=['Home', 'Planty AI', 'Shop', 'Contact'],
    icons=['house', 'robot', 'shop', 'envelope'],
    menu_icon='cast',
    default_index=0,
    orientation='horizontal',
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "20px"},
        "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

# Home Page
if select == 'Home':
    Home()

# Planty AI Page
elif select == 'Planty AI':
    Planty()

# Shop Page
elif select == 'Shop':
    Shop()

# Contact Page
elif select == 'Contact':
    Contact()

else:
    exit()




