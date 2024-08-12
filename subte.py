import folium
import pandas as pd
from folium import features
from lines import *

m = folium.Map(
    location=(-34.6037, -58.3816), zoom_start=11,
    tiles='cartodb positron')

stations = pd.read_csv('main_stations.csv', sep=',', encoding='latin-1')

features.LatLngPopup().add_to(m)

def PlotLine(line):
    folium.PolyLine(
    locations=line[0],
    color=line[1],
    weight=2.5,
    tooltip=line[2]
    ).add_to(m)
def PlotDashedLine(line):
    folium.PolyLine(
    locations=line[0],
    color=line[1],
    weight=2.5,
    tooltip=line[2],
    dash_array=10
    ).add_to(m)

PlotLine(linea_a)
PlotLine(linea_b)
PlotLine(linea_c)
PlotLine(linea_d)
PlotLine(linea_e)
PlotLine(linea_h)
PlotLine(linea_p)
PlotLine(linea_p_centrocivico)

m.save('subte.html')