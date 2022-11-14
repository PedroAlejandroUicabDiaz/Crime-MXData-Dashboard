
import pandas as pd
import numpy as np
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim 

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
