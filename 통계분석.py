범주형 척도(변수) : 예) 성별, 혈액형 - 빈도수 비율 분석이 의미가 있음

서열척도(변수) : 순서가 있는 데이터 예) 학년 -  빈도수 비율 분석이 의미가 있음

등간척도(변수) : 구간으로 나눠진 데이터 예) 만족도(매우만족, 만족, 보통, 불만족, 매우 불만족) - 절대원점(0)은 없고, 덧셈뺄셈 연산 가능

비율 척도(연속형변수) : 절대원점(0)이 존재하고, 산술연산이 가능함

Dummy 변수변환 - 어떤 특성이 있는지 없는지 여부만 표시하는 데이터 변환

여기서 변수는 그 데이터값

get_dummies() : one hot encoding - 0아니면, 1에 해당하는 벡터로 만들어 준다.



merge() : 하나 이상의 키를 기준으로 dataframe 객체 병합, 기본 병합 방식은 교집합(inner)

merge(df1, df2)

merge(df1, df2, on='병합기준으로 사용될 명 변수', right_on='병합할 키열', left_on='병합할 키열', how='left, right, outer', left_index = True, right_index=True)

join() - 두 데이터 프레임에서 행 인덱스로 데이터 병합, (기본 left join 방식)



####Review####

