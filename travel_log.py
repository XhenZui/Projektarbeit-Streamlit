import folium
import streamlit as st
import random
from streamlit_folium import st_folium
from log import log_entry
import safe_to_file

# read data from file on a new run
if "logs" not in st.session_state:
    st.session_state["logs"] = []
    st.session_state["logs"] = safe_to_file.read_from_file()


def get_pos(lat, lng):
    return lat, lng


# initialize state
if "last_clicked" not in st.session_state:
    st.session_state["last_clicked"] = {}
    st.session_state["last_clicked"]["lat"] = 0.0
    st.session_state["last_clicked"]["lng"] = 0.0
if "create_menu" not in st.session_state:
    st.session_state["create_menu"] = False

st.session_state["center"] = [48, 20]
st.session_state["zoom"] = 4

if "logs" not in st.session_state:
    st.session_state["logs"] = []

# title and layout
st.set_page_config(layout="wide")
st.title("Travel Log")
col1, col2 = st.columns(2)


# edit dialog
@st.dialog("Edit log entry")
def edit(log):
    name = st.text_input("Edit name", value=log.name)
    description = st.text_input("Edit description", value=log.description)
    address = st.text_input("Edit address", value=log.address)
    picture = st.file_uploader("Edit picture", type=["jpg", "png", "jpeg"])
    lat = st.text_input("Edit latitude", value=log.marker.location[0])
    lng = st.text_input("Edit longitude", value=log.marker.location[1])
    if st.button("Submit"):
        log.name = name
        log.description = description
        log.address = address
        log.marker.location[0] = lat
        log.marker.location[1] = lng
        if picture is not None:
            log.picture = picture
        st.rerun()


# buttons
with col2:
    with st.container():
        b1, b2, b3 = st.columns(3)
        with b1:
            if not st.session_state["create_menu"]:
                if st.button("Create log entry"):
                    st.session_state["create_menu"] = True
            else:
                if st.button("Cancel"):
                    st.session_state["create_menu"] = False

            if st.session_state["create_menu"]:
                name = st.text_input("Name", "my new log entry")
                description = st.text_input(
                    "Description", "the description of my new log entry"
                )

                if st.button("Confirm create"):
                    number = len(st.session_state["logs"])

                    new_marker = folium.Marker(
                        location=[
                            st.session_state["last_clicked"]["lat"],
                            st.session_state["last_clicked"]["lng"],
                        ],
                        popup=name,
                        icon=folium.Icon(icon=str(number), prefix="fa", color="red"),
                    )
                    st.session_state["logs"].append(
                        log_entry(
                            new_marker, name, description=description, number=number
                        )
                    )
                    st.session_state["create_menu"] = False
        with b2:
            if st.button("Delete all logs"):
                st.session_state["logs"] = []
        with b3:
            if st.button("Add random log"):
                number = len(st.session_state["logs"])
                random_lat = random.random() * 5 + 48.0
                random_lon = random.random() * 5 + 10.0
                random_marker = folium.Marker(
                    location=[random_lat, random_lon],
                    popup=f"Random marker at {random_lat:.2f}, {random_lon:.2f}",
                    icon=folium.Icon(icon=str(number), prefix="fa", color="blue"),
                )
                st.session_state["logs"].append(
                    log_entry(
                        random_marker,
                        "this is a random marker",
                        description="this is the descripton of a random marker",
                        number=number,
                    )
                )

    # log list
    st.write("-----------------------")
    st.title("Log List")
    for log in st.session_state["logs"]:
        with st.expander(str(log.number) + " - " + log.name):
            st.header(str(log.number) + " - " + log.name)
            if log.description != "":
                st.write(log.description)
            if log.address != "":
                st.write(f"Address: {log.address}")
            if log.marker:
                st.write(
                    f"Coordinates: {log.marker.location[0]} , { log.marker.location[1]}"
                )
            if log.picture:
                st.image(log.picture)
            if st.button(f"edit {log.number} - {log.name}"):
                edit(log)


# create the map
with col1:
    m = folium.Map(location=[45, -122], zoom_start=8)
    fg = folium.FeatureGroup(name="Markers")

    for log in st.session_state["logs"]:
        fg.add_child(log.marker)
    if st.session_state["create_menu"]:
        m.add_child(folium.ClickForMarker())

    out = st_folium(
        m,
        center=st.session_state["center"],
        zoom=st.session_state["zoom"],
        key="new",
        feature_group_to_add=fg,
        height=600,
        width=900,
    )

    # with this you can get which marker was last clicked - need to compare it to list of markers
    # if out.get("last_object_clicked"):
    #     st.write(out.get("last_object_clicked"))

    # write the coordinates of the last clicked point into state
    if out.get("last_clicked"):
        st.session_state["last_clicked"] = out.get("last_clicked")
        # with this you can get the coordinates of the last clicked point
        # data = get_pos(
        #     st.session_state["last_clicked"]["lat"],
        #     st.session_state["last_clicked"]["lng"],
        # )
        # st.write(data)

safe_to_file.save_to_file(st.session_state["logs"])
