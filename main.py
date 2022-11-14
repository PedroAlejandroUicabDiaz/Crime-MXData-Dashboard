import streamlit as st
from streamlit_folium import folium_static
from libs.st_utils import map_crime_zoom
from libs.fdf_articles import FdfArticles


articles = FdfArticles()

if 'data' not in st.session_state:
    st.session_state['data']:'FdfArticles' | None = None

with st.sidebar:
    st.markdown('#### Choose a dataset:')

    selection_df:str = st.selectbox(label='',options=articles.names)
    if selection_df:
        st.session_state['data'] = articles.articles[selection_df]
    
    st.markdown('#### Choose a target:')
    selection_target:str = st.selectbox(label='', options=st.session_state['data'].features)
    if selection_target:
        st.session_state['data'].feature = selection_target

content = st.empty()

with content.container():
    try:
        folium_static(st.session_state['data'].show_map(zoom=True))
    except:
        st.write('Maybe the data selected is not able to show')

