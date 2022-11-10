import streamlit as st

st.title('Hello world')


import pandas as pd 

df = pd.read_csv(r'./state_market_tracker.tsv000.gz', sep='\t')
df=df[['period_begin','state','state_code','property_type','median_sale_price']]
df=df[(df['period_begin']=='2022-01-01') & (df['property_type']=='Single Family Residential')] 
df.rename({'median_sale_price':'Median Sales Price ($)'},axis=1, inplace=True)

import plotly.express as px
fig = px.choropleth(df,
                    locations='state_code', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Median Sales Price ($)',
                    color_continuous_scale="Viridis_r", 
                    
                    )
fig.update_layout(
      title_text = 'Jan 2022 Median Housing Price by State',
      title_font_family="Times New Roman",
      title_font_size = 22,
      title_font_color="black", 
      title_x=0.45, 
         )


st.plotly_chart(fig, use_container_width=True)
