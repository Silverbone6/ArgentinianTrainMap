import folium
from lines import *
m = folium.Map(
    location=(-34.6037, -58.3816), zoom_start=11,
    tiles='cartodb positron')
def PlotLine(line):
    folium.PolyLine(
    locations=line[0],
    color=line[1],
    weight=2.5,
    tooltip=line[2]
    ).add_to(m)
PlotLine(plazac_mdp)
PlotLine(bb_santarosa)
PlotLine(bb_villamercedes)
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
PlotLine(villamercedes_riocuarto)
PlotLine(cba_riocuarto)
PlotLine(sanmartin_sanrafael)
PlotLine(sanmartin_gralalvear)
PlotLine(mendoza_losandes)
PlotLine(cba_labanda_tucuman)
PlotLine(cba_santafe_mitre)
PlotLine(tandil_lasflores)
PlotLine(tandil_necochea)
PlotLine(olavarria_pringles_bb)
PlotLine(tandil_bb)
PlotLine(tandil_maipu)
PlotLine(mdp_ayacucho)
PlotLine(retiro_riocuarto)
PlotLine(retiro_cba_belgrano)
PlotLine(santafe_sanfrancisco)
PlotLine(cba_jujuy)
PlotLine(cba_sanjuan)
PlotLine(cba_catamarca)
PlotLine(rosoeste_santafe)
PlotLine(santafe_resistencia)

m.save('map.html')
