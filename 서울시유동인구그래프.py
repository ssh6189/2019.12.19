###matplotlib 라이브러리를 이용한 시각화###
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


#matplotlib 한글 폰트 오류 문제 해결
#from matplotlib import font_manager, rc
#font_path='./datas/malgun.ttf'      
#font_name= font_manager.FontProperties(fname=font_path).get_name()
#rc('font', fmaily=font_name)

plt.rc('font', family='Malgun Gothic')
#시도별 전출입 인구수.xlsx파일을 결측치는 0으로 대체,  첫번째 행을 header로 데이터 프레임 생서
df = pd.read_excel('C:/Users/student/Desktop/datas/datas/시도별 전출입 인구수.xlsx', fillna=0, header=0)

#데이터 프레임의 데이터중 누락값을 찾아서 앞 행의 동일컬럼의 값으로 채웁니다.
df = df.fillna(method='ffill')

# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시') 
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)

##서울에서 '충청남도', '경상북도', '강원도' , '전라남도' 로 이동한 인구 데이터 값 선택 (1970~2018)
col_years = list(map(str, range(1970, 2018)))
df_4 = df_seoul.loc[['충청남도','경상북도', '강원도', '전라남도'  ], col_years]
df_4 = df_4.transpose()

# 스타일 서식 지정
plt.style.use('ggplot') 

#데이터프레임의 인덱스를 정수형으로 변경 (x축 눈금 라벨로 표시)
df_4.index=df_4.index.map(int)

#df_4.plot(kind='area', stacked=False, alpha=0.2, figsize=(20, 10))
#df_4.plot(kind='area', stacked=True, alpha=0.2, figsize=(20, 10))
df_4.plot(kind='bar', width=0.7, color=['orange', 'green', 'skyblue', 'pink'],  figsize=(20, 10))

# 차트 제목 추가
plt.title('서울 -> 충남, 경북, 강원, 전라 인구 이동', size=30)

# 축이름 추가
plt.xlabel('기간', size=12)
plt.ylabel('이동 인구수', size = 12)
plt.legend(loc='best', fontsize=15)
plt.ylim(50000, 300000)
plt.show()
