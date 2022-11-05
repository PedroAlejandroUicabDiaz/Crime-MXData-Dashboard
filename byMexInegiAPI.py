import json 
import requests
import pandas as pd
import numpy as np

# Get the indicator number and its name
indicator = str(input("Type Indicator: "))
indicator_name = str(input("Type Indicator name: "))


response = requests.get('https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/'+indicator+'/es/0700/false/BISE/2.0/{INEGI_APIKEY}?type=json')
respJson = response.json()

# Getting the time peirod and the value from it
years = [x['TIME_PERIOD'] for x in respJson['Series'][0]['OBSERVATIONS']]
mex_value = [x['OBS_VALUE'] for x in respJson['Series'][0]['OBSERVATIONS']]


# Save them in a dataframe structure
df = pd.DataFrame({'years': years,
                    indicator_name:mex_value})


# Save dataframe
df.to_csv('dataN/'+indicator_name+'.csv',index = False)