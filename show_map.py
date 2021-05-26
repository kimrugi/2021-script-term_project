import folium
import webbrowser

def show_map(data_list, index):

    map_osm = folium.Map(location=[data_list[index]["LAT"], data_list[index]["LONGI"]], zoom_start=30)
    for data in data_list:
        folium.Marker([data["LAT"],data["LONGI"]], popup=data["LIBRRY_NM"]).add_to(map_osm)
    map_osm.save('osm.html')
    webbrowser.open_new('osm.html')

