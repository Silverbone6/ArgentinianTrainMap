import folium
from lines import *
m = folium.Map(
    location=(-34.6037, -58.3816), zoom_start=11,
    tiles='cartodb positron')
def PlotLine(line):
    folium.PolyLine(
    locations=line[0],
    color=line[1],
    weight=5,
    tooltip=line[2]
    ).add_to(m)
PlotLine(plazac_laplata)
m.save('BuenosAiresTrains.html')