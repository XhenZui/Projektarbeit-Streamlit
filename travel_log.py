import folium
import streamlit as st
from folium.features import Marker, Popup
import random
from streamlit_folium import st_folium
from log import log_entry


def get_pos(lat, lng):
    return lat, lng


st.set_page_config(layout="wide")

# initialize state
if "last_clicked" not in st.session_state:
    st.session_state["last_clicked"] = {}
    st.session_state["last_clicked"]["lat"] = 45.0
    st.session_state["last_clicked"]["lng"] = -122.0

st.session_state["center"] = [45, -122]
st.session_state["zoom"] = 4

if "logs" not in st.session_state:
    st.session_state["logs"] = []

st.title("Travel Log")

col1, col2 = st.columns(2)


# buttons
name = col2.text_input("Name", "my new log entry")
description = col2.text_input("Description", "the description of my new log entry")
if col2.button("Create log entry"):
    new_marker = folium.Marker(
        location=[
            st.session_state["last_clicked"]["lat"],
            st.session_state["last_clicked"]["lng"],
        ],
        popup=name,
    )
    st.session_state["logs"].append(
        log_entry(new_marker, name, description=description)
    )

if col2.button("remove logs"):
    st.session_state["logs"] = []


if col2.button("Add random log"):
    random_lat = random.random() * 0.5 + 39.8
    random_lon = random.random() * 0.5 - 75.2
    random_marker = folium.Marker(
        location=[random_lat, random_lon],
        popup=f"Random marker at {random_lat:.2f}, {random_lon:.2f}",
    )
    st.session_state["logs"].append(log_entry(random_marker, "this is a random marker"))

with col2:
    for log in st.session_state["logs"]:
        st.write("-----------------------")
        st.header(log.name)
        if log.description != "":
            st.write(log.description)
        if log.address != "":
            st.write(log.address)
        if log.marker:
            st.write(log.marker.location)


# create the map
with col1:
    m = folium.Map(location=[45, -122], zoom_start=8)
    fg = folium.FeatureGroup(name="Markers")
    for log in st.session_state["logs"]:
        fg.add_child(log.marker)

    out = st_folium(
        m,
        center=st.session_state["center"],
        zoom=st.session_state["zoom"],
        key="new",
        feature_group_to_add=fg,
        height=400,
        width=700,
    )

    # with this you can get which marker was last clicked - need to compare it to list of markers
    if out.get("last_object_clicked"):
        st.write(out.get("last_object_clicked"))

    # write the coordinates of the last clicked point into state
    if out.get("last_clicked"):
        st.session_state["last_clicked"] = out.get("last_clicked")
        data = get_pos(
            st.session_state["last_clicked"]["lat"],
            st.session_state["last_clicked"]["lng"],
        )
