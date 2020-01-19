import folium
import pandas as pd

df = pd.read_excel('C:/Users/student/Desktop/datas/datas/서울지역 대학교 위치.xlsx')
df.columns=['대학', '위도', '경도']

print(df)

seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup = name).add_to(seoul_map)
    
seoul_map.save('C:/Users/student/Desktop/datas/datas/seoul_colleges.html')
