import folium
import streamlit as st
from folium.features import Marker, Popup
import random
from streamlit_folium import st_folium


class log_entry:
    marker = None
    name = ""
    description = ""
    address = ""

    def __init__(self, marker, name, description="", address=""):
        self.marker = marker
        self.name = name
        self.description = description
        self.address = address
