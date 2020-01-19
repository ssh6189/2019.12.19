import folium
seoul_map = folium.Map(location=[37.55, 126.98], zoom_start=12)

seoul_map.save('C:/Users/student/Desktop/datas/output/seoul.html')


####################################################################

seoul_map1 = folium.Map(location=[37.55, 126.98], tiles = 'Stamen Terrain' , zoom_start=12)
seoul_map2 = folium.Map(location=[37.55, 126.98], tiles = 'Stamen Toner' , zoom_start=12)

seoul_map2.save('C:/Users/student/Desktop/datas/output/seoul2.html')
seoul_map1.save('C:/Users/student/Desktop/datas/output/seoul1.html')
