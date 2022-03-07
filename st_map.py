import streamlit as st
import xyzservices.providers as xyz
import leafmap.foliumap as leafmap
import folium

MEAN_LAT, MEAN_LON = (54.42672787640451, 36.76480275056178)


def st_map(cities=None, zoom_start=6, mean_lat=MEAN_LAT, mean_lon=MEAN_LON):
    m = leafmap.Map(location=(mean_lat, mean_lon), zoom_start=zoom_start)
    map_name = m.get_name()
    tiles = ["xyz.OpenRailwayMap"]

    if tiles is not None:
        for tile in tiles:
            m.add_xyz_service(tile)

    if cities is not None:
        for index, location_info in cities.iterrows():
            folium.Marker([location_info["lat"], location_info["lon"]],
                          popup=location_info["Полное наименование"]).add_to(m)

    m.to_html(outfile="map.html")
    return map_name
