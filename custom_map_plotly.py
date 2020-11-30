import pandas as pd    # to work with our dataframe
import plotly.express as px    # to plot the choropleth
import json    # to read your location's geojson from local directory
import requests    # to read your location's geojson from online resource
import random    # to create random data

with open('italy.json') as response:
    region_geo = json.loads(response.read())
    
province= []
for i in region_geo['features']:
    province.append(i['properties']['NOME_REG'])

df= pd.DataFrame(province, columns= ['province'])
df['total'] = [random.randint(1000,2000) for i in df['province']]

fig = px.choropleth(data_frame = df, 
                    geojson = region_geo, 
                    locations = 'province', # name of dataframe column
                    featureidkey = 'properties.NOME_REG',  # path to field in GeoJSON feature object with which to match the values passed in to locations
                    color='total',
                    color_continuous_scale="blues",
                    scope="europe",
                   )
# to only show italy map
fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(title= 'Italy choropleth map')
fig.show()