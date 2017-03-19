import sys
import pandas as pd
df = pd.read_csv("train.csv")
print(df.columns)
sys.exit(0)
rows = len(df)
for idx in range(0, rows):
    date = df.ix[idx]['dt']
    country  = df.ix[idx]['Country']
    averagetemperature = df.ix[idx]['AverageTemperature']
    city = df.ix[idx]['City']
    latitude = df.ix[idx]['Latitude']
    longitude = df.ix[idx]['Longitude']
    averagetemperatureuncertainty = df.ix[idx]['AverageTemperatureUncertainty']
    query ="""INSERT INTO GlobalLandTemperaturesByCity_10000 (dt,AverageTemperature,AverageTemperatureUncertainty,City, Country, Longitude, Latitude)
    VALUES ("{dt}",{averagetemperature},{averagetemperatureuncertainty},"{country}","{city}","{longitude}","{latitude}");""".format(dt=date, country=country,averagetemperature=averagetemperature, longitude=longitude, latitude=latitude, city=city,averagetemperatureuncertainty=averagetemperatureuncertainty) 
    print(query)


