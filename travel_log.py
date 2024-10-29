import folium
import streamlit as st
from folium.features import Marker, Popup
import random
from streamlit_folium import st_folium
from log import log_entry
import safe_to_file


if "logs" not in st.session_state:
    st.session_state["logs"] = []
    st.session_state["logs"] = safe_to_file.read_from_file()


def get_pos(lat, lng):
    return lat, lng


st.set_page_config(layout="wide")

# initialize state
if "last_clicked" not in st.session_state:
    st.session_state["last_clicked"] = {}
    st.session_state["last_clicked"]["lat"] = 0.0
    st.session_state["last_clicked"]["lng"] = 0.0
if "create_menu" not in st.session_state:
    st.session_state["create_menu"] = False

st.session_state["center"] = [45, -122]
st.session_state["zoom"] = 4

if "logs" not in st.session_state:
    st.session_state["logs"] = []

st.title("Travel Log")

col1, col2 = st.columns(2)


# buttons
with col2:
    # create menu
    if not st.session_state["create_menu"]:
        if st.button("Create log entry"):
            st.session_state["create_menu"] = True
    else:
        if st.button("cancel"):
            st.session_state["create_menu"] = False
            if st.session_state["temp"] is not None:
                st.session_state["temp"] = None

    if st.session_state["create_menu"]:
        # text inputs
        name = st.text_input("Name", "my new log entry")
        description = st.text_input(
            "Description", "the description of my new log entry"
        )

        if st.button("confirm create"):
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
            st.session_state["create_menu"] = False
            if st.session_state["temp"] is not None:
                st.session_state["temp"] = None
        st.write("-----------------------")

    if st.button("remove logs"):
        st.session_state["logs"] = []

    if st.button("Add random log"):
        random_lat = random.random() * 0.5 + 39.8
        random_lon = random.random() * 0.5 - 75.2
        random_marker = folium.Marker(
            location=[random_lat, random_lon],
            popup=f"Random marker at {random_lat:.2f}, {random_lon:.2f}",
        )
        st.session_state["logs"].append(
            log_entry(random_marker, "this is a random marker")
        )

    # log list
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
    if st.session_state["temp"] is not None:
        fg.add_child(st.session_state["temp"])
    if st.session_state["create_menu"]:
        m.add_child(folium.ClickForMarker())
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
        # data = get_pos(
        #     st.session_state["last_clicked"]["lat"],
        #     st.session_state["last_clicked"]["lng"],
        # )
        # st.write(data)

safe_to_file.save_to_file(st.session_state["logs"])
