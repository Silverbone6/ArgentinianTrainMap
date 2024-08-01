import folium
import pandas as pd
from folium import features
from lines import *

m = folium.Map(
    location=(-34.6037, -58.3816), zoom_start=11,
    tiles='cartodb positron')

main_stations = pd.read_csv('main_stations.csv', sep=',', encoding='latin-1')

features.LatLngPopup().add_to(m)

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
PlotLine(salta_chile)
PlotLine(jujuy_villazon)
PlotLine(perico_formosa)
PlotLine(santafe_tucuman)
PlotLine(resistencia_metan)
PlotLine(lacroze_posadas)
PlotLine(parana_concepcion)
PlotLine(corrientes_montecaseros)
PlotLine(pichanal_oran)
PlotLine(pichanal_yacuiba)
PlotLine(saenzpena_anatuya)
PlotLine(saenzpena_tostado)

for index, row in main_stations.iterrows():
    pushpin = folium.features.CustomIcon('stationico.png', icon_size=(8,8))
    folium.Marker([row['lat'], row['lon']], 
        icon=pushpin,
        popup=row['station']
    ).add_to(m)

m.save('map.html')
