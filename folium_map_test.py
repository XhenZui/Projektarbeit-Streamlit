import folium
import streamlit as st
from streamlit_folium import st_folium

st.title("hello world - da map")

# Define Liberty Bell coordinates
liberty_bell_coords = [39.949610, -75.150282]

# Create the map and add the Liberty Bell marker
m = folium.Map(location=liberty_bell_coords, zoom_start=16)
liberty_bell_marker = folium.Marker(
    liberty_bell_coords,
    popup="Liberty Bell",
    tooltip="Click me!",
    icon=folium.Icon(color="green"),
)

# Add JavaScript to detect marker click
click_js = """
function(marker) {
    marker.on('click', function() {
        fetch('/_stcore/post_message', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ type: 'click', marker: 'Liberty Bell' })
        });
    });
}
"""

# Add marker with JS event
liberty_bell_marker.add_to(m).add_child(folium.Element(f"<script>{click_js}</script>"))


# Render the map in Streamlit
st_data = st_folium(m, width=725)

st.write("da end of da map")

# Check if the user clicked the marker
if (
    st_data
    and "last_clicked" in st_data
    and st_data["last_clicked"] == liberty_bell_coords
):
    st.write("You clicked on the Liberty Bell marker!")
