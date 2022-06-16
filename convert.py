import pandas as pd
import geopandas as gp
import json
# df = pd.DataFrame({"lon":[10.8494,10.8494, 10.85422,], "lat":[50.90028,50.90028,50.90116],"names":["address 1","address 2","address 3"]})


df = pd.read_json("points.index.json",orient="index")


gdf = gp.GeoDataFrame(df,geometry=gp.points_from_xy(df.lon, df.lat))
gdf.to_file('markers.geojson', driver="GeoJSON") 


