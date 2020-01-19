import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import csv
import re

plt.rc('font', family='Malgun Gothic')

df1 = pd.read_csv('C:/Users/student/Desktop/game_ws1_datas/install.csv', header = None, encoding='cp949')
df2 = pd.read_csv('C:/Users/student/Desktop/game_ws1_datas/dau.csv', header = None, encoding='cp949')
df3 = pd.read_csv('C:/Users/student/Desktop/game_ws1_datas/dpu.csv', header = None, encoding='cp949')

s6 = 0
s7 = 0


sd6 = []
sd7 = []

i = 1
j = 1

#유저데이터에 이용시작 데이터 결합

res = pd.merge(df1, df2, how = 'outer')

#1단계에서 결합한 데이터에 과금 데이터 결합

rst = pd.merge(df3, res, how = 'outer')

#월 컬럼추가
result = rst.append({"월":""}, ignore_index=True)

#신규 유저 및 기존 유저 구분  컬럼추가
final = result.append({"유저타입":""}, ignore_index=True)

#비과금 유저의 과금액에 NaN을 0으로 대체
final = final.fillna(0)

#신규/기존 유저 구분


#월별 과금액 집계
for final.iloc[i][0] in pd.date_range("2013-06-01", "2013-06-30"):
    s6 = s6 + int(final.iloc[i, [3]])

    sd6.append(s6)
    i = i +1

print("6월 과금액 총합 : ", s6)

for result.iloc[j][0] in pd.date_range("2013-07-01", "2013-07-31"):

    s7 = s7 + int(final.iloc[j, [3]])

    sd7.append(s7)
    j = j + 1

print("7월 과금액 총합 : ", s7)

#유저타입 과금액 집계

x1 = pd.date_range("2013-06-01", "2013-06-30")
y1 = sd6

x2 = pd.date_range("2013-07-01", "2013-07-31")
y2 = sd7


        

plt.plot(x1, y1, 'r--', x2, y2, 'b--')
plt.title('월별 유저과금 누적합')
plt.legend(labels = ['6월 과금집계', '7월 과금집계'])

plt.show()
