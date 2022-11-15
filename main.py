import streamlit as st
from streamlit_folium import folium_static
from libs.st_utils import map_crime_zoom
from libs.fdf_articles import FdfArticles
from libs.df_article import Article
from components.st_crime_states import crime_bullets


articles = FdfArticles()
state = ''

if 'data' not in st.session_state:
    st.session_state['data']:'Article' | None = None

if 'bullets' not in st.session_state:
    st.session_state['bullets'] = {'hello', 'hello'}

with st.sidebar:

    selection_df:str = st.selectbox(label='Choose a dataset:',options=articles.names)
    if selection_df:
        st.session_state['data'] = articles.articles[selection_df]
    
    selection_target:str = st.selectbox(label='Choose a target:', options=st.session_state['data'].features)
    if selection_target:
        st.session_state['data'].feature = selection_target
    
    if st.session_state['data'].model != None:
        art:'Article' = st.session_state['data']
        group = art.model.group
        df = art.model.df
        state = st.selectbox(label='Choose the location', options=df[group])
        data = df[df[group] == state]
        data_to_predict = data[art.model.feature_cols]
        blt_1 = data[art.model.evaluator].values[0]
        state_data = art.df[art.df[group] == state]
        blt_2 = len(state_data.groupby('SECTOR').sum())
        st.write()
        if state:
            st.session_state['bullets'] = {'warn':art.model.predict_data(data_to_predict), 'blt_1':blt_1, 'blt_2':blt_2}

content = st.empty()

with content.container():
    if st.session_state['data'].model != None:
        st.markdown(f'## {state}')
        crime_bullets(**st.session_state['bullets'])
    try:
        folium_static(st.session_state['data'].show_map(zoom=True))
    except:
        st.write('Maybe the data selected is not able to show')

