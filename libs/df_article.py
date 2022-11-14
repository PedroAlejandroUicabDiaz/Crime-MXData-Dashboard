from dataclasses import dataclass
import folium
from folium.plugins import HeatMap
import pandas as pd
from utils.filters import unwanted


@dataclass
class Article:
    def __init__(self, df:'pd.DataFrame', feature:str='LATITUDE'):
        self.df:'pd.DataFrame' = df
        self.feature:str = feature
        self.features:list[str] = [n for n in list(df.columns) if n not in unwanted]
    
    def show_map(self, zoom:bool=False) -> 'folium.Map':
        df_crime= self.df[['LATITUDE', 'LONGITUDE', self.feature]].copy()

        hm = folium.Map(location=[19.42847, -99.12766], tiles='stamentoner', zoom_start=10.2 if zoom else 5.2)

        HeatMap(df_crime, min_opacity=0.4, blur = 18).add_to(folium.FeatureGroup(name='Heat Map').add_to(hm))

        folium.LayerControl().add_to(hm)

        return hm

