import json 
import requests
import pandas as pd
import numpy as np

# Get the indicator number and its name
indicator = str(input("Type Indicator: "))
indicator_name = str(input("Type Indicator name: "))

# List of states of Mexico
mex_states_names = ['Aguascalientes', 'Baja California','Baja California Sur','Campeche','Coahuila','Colima','Chiapas','Chihuahua','Ciudad de Mexico','Durango','Guanajuato','Guerrero','Hidalgo','Jalisco','Mexico','Michoacan','Morelos','Nayarit','Nuevo Leon','Oaxaca','Puebla','Queretaro','Quintana Roo','San Luis Potosi','Sinaloa','Sonora','Tabasco','Tamaulipas','Tlaxcala','Veracruz','Yucatan','Zacatecas']
mex_states_value = []

# Iterate over each state and get the value throught INEGI API
for state in range(len(mex_states_names)):

    if state < 10:
        response = requests.get('https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/'+indicator+'/es/0700000'+str(state+1)+'/true/BISE/2.0/{INEGI_APIKEY}?type=json')
        respJson = response.json()
    else:
        response = requests.get('https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/'+indicator+'/es/070000'+str(state+1)+'/true/BISE/2.0/{INEGI_APIKEY}?type=json')
        respJson = response.json()
    
    try:
        mex_states_value.append(round(float(respJson['Series'][0]['OBSERVATIONS'][0]['OBS_VALUE']),2))
    except:
        mex_states_value.append(round(np.mean(mex_states_value),4))


# Save them in a dataframe structure
df = pd.DataFrame({'estados': mex_states_names,
                    indicator_name:mex_states_value})


# Save dataframe
df.to_csv('dataE/'+indicator_name+'.csv',index = False)

