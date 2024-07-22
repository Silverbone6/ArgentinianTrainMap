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
PlotLine(plazac_mdp)
PlotLine(plazac_laplata)
PlotLine(plazac_bb)
PlotLine(bb_neuquen)
PlotLine(bb_patagones)
PlotLine(patagones_saoeste)
PlotLine(saoeste_bariloche)
PlotLine(neuquen_zapala)
PlotLine(retiro_mendoza)
PlotLine(jd_sanluis_lapaz)
PlotLine(mendoza_sanjuan)
PlotLine(retiro_rosnor)
PlotLine(rosnor_santafe)
PlotLine(rosnor_cba)
PlotLine(rosnor_tucuman)
PlotLine(once_santarosa)
PlotLine(bb_villamercedes)
PlotLine(villamercedes_riocuarto)
PlotLine(cba_riocuarto)

m.save('index.html')
