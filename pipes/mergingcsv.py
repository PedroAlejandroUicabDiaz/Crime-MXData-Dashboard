import pandas as pd
import os

# Dir path
dir = "./Crime-MXData-Dashboard/data"

# Get the list of files
list_files = os.listdir(dir)

# reading the first csv
df = pd.read_csv(dir+'/'+'costo_delito_personas_hogares.csv')

# Merging the rest of csv files
for idx in range(1,len(list_files)):
       df = df.merge(pd.read_csv(dir+'/'+list_files[idx]),on='estados')
    

print(df.info())

# Save dataframe
df.to_csv('data/'+'MX_CRIME_DATA_INEGI_P1'+'.csv',index = False)