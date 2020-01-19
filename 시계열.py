#######################TimeStamp 객체 생성과 인덱스 지정 ##############
import pandas as pd

df = pd.read_csv("C:/Users/student/Desktop/datas/datas/stock-data.csv")
print(df.head())
print(df.info())

#문자열 데이터를 pandas의  Timestamp로 변환해서 새로운 열로 추가 
df['new_Date'] = pd.to_datetime(df['Date'])  
print(df.head())
print(df.info())
#print(df.type(df['new_Date']))
#print(df.type(df['new_Date'][0])) 

df.set_index('new_Date', inplace = True)
df.drop('Date', axis = 1, inplace = True)
print(df.head())
print(df.info())

####Timestamp를 Peroid로 변환####


import pandas as pd

df = pd.read_csv("C:/Users/student/Desktop/datas/datas/stock-data.csv")
print(df.head())
print(df.info())

#문자열 데이터를 pandas의  Timestamp로 변환해서 새로운 열로 추가 
df['new_Date'] = pd.to_datetime(df['Date'])  
print(df.head())
print(df.info())
 
#년, 월, 일  값 속성으로 접근
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df.head())

df['Date_yr'] = df['new_Date'].dt.to_period(freq='A')
df['Date_m'] = df['new_Date'].dt.to_period(freq='M')
print(df.head())

df.set_index( 'Date_m' , inplace=True)
print(df.head())


#행 인덱스에 접근
#iloc[]
#loc[]


########################################
import pandas as pd

df = pd.read_csv("C:/Users/student/Desktop/datas/datas/stock-data.csv")

print(df.head())
print(df.info())

#문자열 데이터를 pandas의  Timestamp로 변환해서 새로운 열로 추가 
df['new_Date'] = pd.to_datetime(df['Date'])  
df.set_index('new_Date', inplace = True)

print(df.head())
print(df.info())

df_y = df['2018']
print(df_y)
df_ym = df.loc['2018-07']
print(df_ym)

df_ym_cols = df.loc['2018-07', 'Start':'High']
print(df_ym_cols)

df_ymd_range = df.loc['2018-06-25':'2018-06-20']
print(df_ymd_range)
