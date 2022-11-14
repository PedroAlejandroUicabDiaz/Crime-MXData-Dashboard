import folium
from folium.plugins import HeatMap



def map_crime(df,feature):
    df_crime= df[['LATITUDE', 'LONGITUDE', feature]].copy()
    hm = folium.Map(location=[23.634501, -102.552784], tiles='stamentoner', zoom_start=5.2)
    HeatMap(df_crime, min_opacity=0.4, blur = 18).add_to(folium.FeatureGroup(name='Heat Map').add_to(hm))
    folium.LayerControl().add_to(hm)
    return hm


def map_crime_zoom(df,feature):
    df_crime= df[['LATITUDE', 'LONGITUDE', feature]].copy()
    hm = folium.Map(location=[19.42847, -99.12766], tiles='stamentoner', zoom_start=10.2)
    HeatMap(df_crime, min_opacity=0.4, blur = 18).add_to(folium.FeatureGroup(name='Heat Map').add_to(hm))
    folium.LayerControl().add_to(hm)
    return hm
