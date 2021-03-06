re 모듈 - 정규 표현식을 지원 
정규 표현식 패턴에 일치하는 문자열을 검색 - findall, match, search
pandas의 Series객체에는 문자열에 대한 간결하게 처리 메소드 지원 - Series객체.str속성의 메서드
MultiIndex - 2개이상의 level을 가지는 인덱스 
2개이상의 level을 가지는 Series객체의 Index를 이용하여 데이터를 재배열해주는 메소드 - unstack
재배열된 데이터 구조를 2개이상의 level을 가지는 Series객체로 변환 - stack
2개이상의 level을 가지는 Series객체 - swaplevel()

info() - 데이터프레임의 기본 정보 (클래스 유형, 행 인덱스 구성, 열 이름의 종류와 개수, 각 열의 자료형과 개수, 메모리 할당량) 제공
decribe() - 기본 기술 통계 요약 (데이터프레임의 열에 대한 평균, 표준편차, 최소값, 최대값, 중앙값, 1/4분위값, 3/4분위값 등) 요약 반환
빈도수 - value_counts(), freq(), top()

pandas 기본 내장 시각화 도구 - 데이터프레임 객체.plot(kind=)

matplotlib 라이브러리 - 2D 평면 그래프에 관한 다양한 포맷과 기능 지원 
matplotlib.pyplot.plot()  - line chart가 기본 ,  점으로 그래프 표현  두번째 인수로 'o' 
제목 - title()
축이름 - xlabel(), ylabel()
그래프 틀 객체 (그래프의 size 지정 또는 그래프 분할 지정) - figure()
figure()로 생성된 그래프 객체에 분할영역을 생성(지정, 추가) - add_subplot() 
눈금 - xticks()
축 범위 - xlim(), ylim()
annotate() -그래프에 여러 형태의 설명을 추가하기 위해 사용
범례 - legend()
sub plot 객체 = add_subplot() 
sub plot 객체.set_title()
sub plot 객체.set_xlim()
그래프 꾸미기 옵션 - markerfacecolor , color, linewidth , label

데이터를 일정 구간으로 나눠서 분석하기 위해 
cut(data객체,  bins=경계값객체|구간개수 , label=, include_lower=) - 데이터를 일정 구간으로 나누기 위해 사용하는 함수 

숫자 데이터의 상대적인 크기에 대한 차이를 제거할 경우 - 열에 속하는 데이터값을 동일한 크기 기준으로 나눈 비율로 변환 => 정규화
비율로 변환하는 정규화 결과 데이터 범위 : 0~1 또는 -1~1 범위의 값이 됩니다.
비율로 변환하는 방법 - 열의 최대값으로 나눈 방법, 최대값-최소값으로 나누는 방법

범주형 척도(변수) :  예)  성별, 혈액형 - 빈도수 비율 분석이 의미가 있음
서열척도(변수) :  순서가 있는 데이터, 예) 학년  - 빈도수 비율 분석이 의미가 있음
등간척도(변수) :  구간으로 나눠진 데이터 예) 만족도  - 절대원점(0)은 없고, 덧셈 뺄셈 연산 가능
비율 척도(연속형변수) :  절대원점(0)이 존재하고 , 산술연산 가능

Dummy 변수변환 - 어떤 특성이 있는지 없는지 여부만 표시하는 데이터 변환
get_dummies()  : one hot encoding - 0 과 1 값의 벡터 변환
