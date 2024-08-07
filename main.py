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
PlotLine(chardai_santasylvina)
PlotLine(vera_lastoscas)
PlotLine(tucuman_alberdi)
PlotLine(tucuman_riohondo)
PlotLine(corrientes_goya)
PlotLine(nogoya_victoria)
PlotLine(gualeguay_ecarbo)
PlotLine(gualeguaychu_parera)
PlotLine(cba_cruzdeleje)
PlotLine(cba_altagracia)
PlotLine(patquia_chilecito)
PlotLine(palmira_rivadavia)
PlotLine(realico_alvear)
PlotLine(bragado_castex)
PlotLine(bragado_realico)
PlotLine(plazac_carhue)
PlotLine(carhue_rivera)
PlotLine(miramar_otamendi)
PlotLine(guido_pinamar)
PlotLine(plazac_olavarria)
PlotLine(bb_palta)
PlotLine(jacobacci_esquel)
PlotLine(rosario_pergamino)
PlotLine(rosnor_melincue)
PlotLine(villac_rufino)

for index, row in stations.iterrows():
    if row['category']=='first':
        size=(10,10)
    if row['category']=='second':
        size=(8,8)
    if row['category']=='third':
        size=(6,6)
    if row['ffcc']=='gu':
        ffcc='urquizastation.png'
    if row['ffcc']=='roca':
        ffcc='rocastation.png'
    if row['ffcc']=='sm':
        ffcc='sanmartinstation.png'
    if row['ffcc']=='b':
        ffcc='belgranostation.png'
    if row['ffcc']=='mitre':
        ffcc='mitrestation.png'
    if row['ffcc']=='pat':
        ffcc='patagoniastation.png'
    if row['ffcc']=='dfs':
        ffcc='sarmientostation.png'
    if row['ffcc']=='andino':
        ffcc='andinostation.png'
    pushpin = folium.features.CustomIcon(ffcc, icon_size=size)
    folium.Marker([row['lat'], row['lon']], 
        icon=pushpin,
        popup=row['station']
    ).add_to(m)

m.save('map.html')
exec