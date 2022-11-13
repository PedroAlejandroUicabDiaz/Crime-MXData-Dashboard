import streamlit as st
from streamlit_folium import folium_static
from libs.st_utils import map_crime_zoom


with st.sidebar:
    st.title('Hello')

import pandas as pd

df1 = pd.read_csv('./data/MX-DATA-UPDATED.csv')
df2 = pd.read_csv('./data/MX_CRIME_DATA_INEGI_P1.csv')




# df_loc_fet = redifine_locations(df2)

df_loc_fet = pd.read_csv('./data/featured.csv')


m = map_crime_zoom(df1, 'ROBO A NEGOCIO C.V.')


st_data = folium_static(m, width=725)

