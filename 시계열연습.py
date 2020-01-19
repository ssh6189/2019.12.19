import pandas as pd

ts_ms = pd.date_range(start='2019-01-01',
                   end=None,
                   periods=6,
                   freq='MS' ,   #월의 시작일 시간 간격
                   tz = 'Asia/Seoul')
print(ts_ms)

ts_me = pd.date_range(start='2019-01-01',
                   end=None,
                   periods=6,
                   freq='M' ,   #월의 마지막날 시간 간격
                   tz = 'Asia/Seoul')
print(ts_me)

ts_3m = pd.date_range(start='2019-01-01',
                   end=None,
                   periods=6,
                   freq='3M' ,   #3개월 시간 간격
                   tz = 'Asia/Seoul')
print(ts_3m)

pr_h = pd.period_range(start='2019-01-01',
                   end=None,
                   periods=3,
                   freq='M')   #기간의 길이는 (M:월)
print(pr_h)


pr_5h = pd.period_range(start='2019-01-01',
                   end=None,
                   periods=3,
                   freq='5H')   #기간의 길이는 (H:시간)
print(pr_5h)


