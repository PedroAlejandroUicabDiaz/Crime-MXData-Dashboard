import folium
import pandas as pd
import numpy as np
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
from folium.plugins import HeatMap

def findGeocode(city):
 
    try:

        geolocator = Nominatim(user_agent="your_app_name")
        
        return geolocator.geocode(city)
      
    except GeocoderTimedOut:
          
        return findGeocode(city)


def redifine_locations(df:'pd.DataFrame'):
    longitude = []
    latitude = []
    for i in (df["estados"]):

        if findGeocode(i) != None:

            loc = findGeocode(i)

            latitude.append(loc.latitude)
            longitude.append(loc.longitude)

        # missing value 
        else:
            latitude.append(np.nan)
            longitude.append(np.nan)
    df["LATITUDE"] = latitude
    df["LONGITUDE"] = longitude

    df.to_csv('./data/featured.csv')
    
    return df


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
