import folium
import pandas as pd
import json

df = pd.read_excel('C:/Users/student/Desktop/datas/datas/경기도인구데이터.xlsx',  index_col='구분')
df.columns = df.columns.map(str)

print(df)

seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)

geo_data = json.load(open('C:/Users/student/Desktop/datas/datas/경기도행정구역경계.json', encoding='utf-8'))
print(geo_data)

g_map = folium.Map(location=[37.5502, 126.982], tiles = 'Stamen Terrain', zoom_start=9)

year = '2017'

folium.Choropleth(geo_data=geo_data,
                  data = df[year],
                  columns = [df.index, df[year]],
                  fill_color = 'YlOrRd', fill_opacity=0.7, line_opacity = 0.3,
                  threshold_scale = [10000, 100000, 300000, 500000, 700000],
                  key_on = 'feature.properties.name').add_to(g_map)

g_map.save('C:/Users/student/Desktop/datas/output/gyounggi_pop_2017.html')
