import folium
import streamlit as st
from folium.features import Marker, Popup
import random
from streamlit_folium import st_folium


def get_pos(lat, lng):
    return lat, lng


# initialize state
if "last_clicked" not in st.session_state:
    st.session_state["last_clicked"] = {}
    st.session_state["last_clicked"]["lat"] = 45.0
    st.session_state["last_clicked"]["lng"] = -122.0

st.session_state["center"] = [45, -122]
st.session_state["zoom"] = 4

if "markers" not in st.session_state:
    st.session_state["markers"] = []

# buttons
if st.button("Create marker"):
    random_marker = folium.Marker(
        location=[
            st.session_state["last_clicked"]["lat"],
            st.session_state["last_clicked"]["lng"],
        ],
        popup="my new marker",
    )
    st.session_state["markers"].append(random_marker)

if st.button("remove marker"):
    st.session_state["markers"] = []


if st.button("Add random marker"):
    random_lat = random.random() * 0.5 + 39.8
    random_lon = random.random() * 0.5 - 75.2
    random_marker = folium.Marker(
        location=[random_lat, random_lon],
        popup=f"Random marker at {random_lat:.2f}, {random_lon:.2f}",
    )
    st.session_state["markers"].append(random_marker)


# create the map
m = folium.Map(location=[45, -122], zoom_start=8)
fg = folium.FeatureGroup(name="Markers")
for marker in st.session_state["markers"]:
    fg.add_child(marker)

out = st_folium(
    m,
    center=st.session_state["center"],
    zoom=st.session_state["zoom"],
    key="new",
    feature_group_to_add=fg,
    height=400,
    width=700,
)

# with this you can get which marker was last clicked
if out.get("last_object_clicked"):
    st.write(out.get("last_object_clicked"))


# write the coordinates of the last clicked point into state
if out.get("last_clicked"):
    st.session_state["last_clicked"] = out.get("last_clicked")
    data = get_pos(
        st.session_state["last_clicked"]["lat"], st.session_state["last_clicked"]["lng"]
    )
    st.write(data)
    st.write(st.session_state["last_clicked"])


st.write(st.session_state["markers"])
