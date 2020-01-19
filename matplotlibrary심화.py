면적(area plot) 그래프

히스토그램

변수가 하나인 단변수 데이터의 빈도수를 그래프로 표현한다.
X축을 같은 크기의 여러 구간으로 나누고 각 구간에 속하는 뎅터의 값의 개수(빈도)를  y축에
표시한다.

산점도
서로 다른 두 변수 사이의 관계를 나타낸다.
각 변수는 연속되는 값을 갖는다.
plot(kind = 'scatter', x=, y=, c=, s=, figsize=, alpha=)

파이차트
원을 파이 조각으로 나누어서 표현한다.
조각의 크기는 해당 변수에 속하는 데이터 값의 크기에 비례한다.

plot(kind = 'pie', figsize, autopct= , startangle=, colors=)

박스플롯
범주형 데이터의 분포를 파악하는데 적합하다.
5개의 통계지표(최소값, 1분위값, 중간값, 3분위값, 최대값)을 제공한다.
boxplot(x=, labels=, vert = False) #vert=False 옵션으로 수평박스 플롯을 그린다.(True : 수직)



Seaborn

regplot(서로 다른 2개의 연속 변수 사이의 산점도를 그리고, 선형 회귀 분석에 의한 회구선을 함께 나타낸다. Fit_reg=False 옵션을 설정하면
        회귀선을 안 보이게 할 수 있다.
        
displot 하나의 변수 데이터의 히스토그램/커널 밀도 그래프
        hist = False 옵션을 추가하면 히스토그램이 표시되지 않고
        kde = False옵션을 추가하면, 커널 밀도 그래프를 표시하지 않는다.
        
heatmap 2개의 범주형 변수를 각각 x,y축에 놓고 데이터를 매트릭스 형태로 분류한다.
        aggfunc옵션은 집계할 데이터 값을 설정ㅎ나다.
        bar옵션은 컬러바 표시설정
        
stripplot 범주형 데이터의 산점도 - 범주별 데이터의 분포를 확인
        
sarmplot 데이터의 분산까지 고려하여 그린다.
barplot
countplot

boxplot
violinplot
joinplot
FacetGrid
pairplot()

##################sea born regplot()###################
