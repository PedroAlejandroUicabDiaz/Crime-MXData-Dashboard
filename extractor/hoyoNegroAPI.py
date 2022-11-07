import requests
import json
import pandas as pd

crimes_types = requests.get('https://hoyodecrimen.com/api/v1/crimes')
crimes_types = crimes_types.json()


cuadrantes_list = requests.get('https://hoyodecrimen.com/api/v1/cuadrantes')
cuadrantes_list = cuadrantes_list.json()


sectores_list = requests.get('https://hoyodecrimen.com/api/v1/sectores')
sectores_list = sectores_list.json()


crimes = [x['crime'] for x in crimes_types['rows']]

sectores = [x['sector'] for x in cuadrantes_list['rows']]

municipios = [x['municipio'] for x in cuadrantes_list['rows']]

cuadrantes = [x['cuadrante'] for x in cuadrantes_list['rows']]


homi = []
arma = []
robo_metro_cv = []
robo_metro_sv = []
robo_micro_cv = []
robo_micro_sv = []
robo_taxi_cv = []
robo_hab = []
robo_cuentahab = []
robo_negocio = []
robo_repartidor_cv = []
robo_repartidor_sv = []
robo_trans_cv = []
robo_trans_sv = []
robo_transpor_cv = []
robo_transpor_sv = []
robo_vehi_cv =[]
robo_vehi_sv = []
secuestro = []
violacion = []

for cuadrante in cuadrantes:
    for crime in crimes:
        response = requests.get('https://hoyodecrimen.com/api/v1/cuadrantes/'+cuadrante+'/crimes/'+crime+'/period')
        response = response.json()

        count = response['rows'][0]['count']

        if crime == 'HOMICIDIO DOLOSO':
            homi.append(count)
        elif crime == 'LESIONES POR ARMA DE FUEGO':
            arma.append(count)
        elif crime == 'ROBO A BORDO DE METRO C.V.':
            robo_metro_cv.append(count)
        elif crime == 'ROBO A BORDO DE METRO S.V.':
            robo_metro_sv.append(count)
        elif crime == 'ROBO A BORDO DE MICROBUS C.V.':
            robo_micro_cv.append(count)
        elif crime == 'ROBO A BORDO DE MICROBUS S.V.':
            robo_micro_sv.append(count)
        elif crime == 'ROBO A BORDO DE TAXI C.V.':
            robo_taxi_cv.append(count)
        elif crime == 'ROBO A CASA HABITACION C.V.':
            robo_hab.append(count)
        elif crime == 'ROBO A CUENTAHABIENTE C.V.':
            robo_cuentahab.append(count)
        elif crime == 'ROBO A NEGOCIO C.V.':
            robo_negocio.append(count)
        elif crime == 'ROBO A REPARTIDOR C.V.':
            robo_repartidor_cv.append(count)
        elif crime == 'ROBO A REPARTIDOR S.V.':
            robo_repartidor_sv.append(count)
        elif crime == 'ROBO A TRANSEUNTE C.V.':
            robo_trans_cv.append(count)
        elif crime == 'ROBO A TRANSEUNTE S.V.':
            robo_trans_sv.append(count)
        elif crime == 'ROBO A TRANSPORTISTA C.V.':
            robo_transpor_cv.append(count)
        elif crime == 'ROBO A TRANSPORTISTA S.V.':
            robo_transpor_sv.append(count)
        elif crime == 'ROBO DE VEHICULO AUTOMOTOR C.V.':
            robo_vehi_cv.append(count)
        elif crime == 'ROBO DE VEHICULO AUTOMOTOR S.V.':
            robo_vehi_sv.append(count)
        elif crime == 'SECUESTRO':
            secuestro.append(count)
        elif crime == 'VIOLACION':
            violacion.append(count)


# Save them in a dataframe structure
df = pd.DataFrame({'CUADRANTE': cuadrante,
                    'MUNICIPIO':municipios,
                    'SECTOR':sectores,
                    'HOMICIDIO DOLOSO':homi,
                    'LESIONES POR ARMA DE FUEGO':arma,
                    'ROBO A BORDO DE METRO C.V.':robo_metro_cv,
                    'ROBO A BORDO DE METRO S.V.':robo_metro_sv,
                    'ROBO A BORDO DE MICROBUS C.V.':robo_micro_cv,
                    'ROBO A BORDO DE MICROBUS S.V.':robo_micro_sv,
                    'ROBO A BORDO DE TAXI C.V.':robo_taxi_cv,
                    'ROBO A CASA HABITACION C.V.':robo_hab,
                    'ROBO A CUENTAHABIENTE C.V.':robo_cuentahab,
                    'ROBO A NEGOCIO C.V.':robo_negocio,
                    'ROBO A REPARTIDOR C.V.':robo_repartidor_cv,
                    'ROBO A REPARTIDOR S.V.':robo_repartidor_sv,
                    'ROBO A TRANSEUNTE C.V.':robo_trans_cv,
                    'ROBO A TRANSEUNTE S.V.':robo_trans_sv,
                    'ROBO A TRANSPORTISTA C.V.':robo_trans_cv,
                    'ROBO A TRANSPORTISTA S.V.':robo_trans_sv,
                    'ROBO DE VEHICULO AUTOMOTOR C.V.':robo_vehi_cv,
                    'ROBO DE VEHICULO AUTOMOTOR S.V.':robo_vehi_sv,
                    'SECUESTRO':secuestro,
                    'VIOLACION':violacion})


# Save dataframe
df.to_csv('MX-DATA.csv',index = False)

"""for crime in crimes:
    crime_total = requests.get('https://hoyodecrimen.com/api/v1/df/crimes/'+crime+'/series')
    crime_total = crime_total.json()

    dates = [x['date'] for x in crime_total['rows']]
    counts = [x['count'] for x in crime_total['rows']]

    print(crime,'\n',dates,'\n',counts)"""