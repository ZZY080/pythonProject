import datetime

destTime ="2023-11-29 15:11:00"
now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# while True:
#     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     if(now>destTime):
#         print(12)
#         break
now=datetime.datetime.now()

# 添加一分钟
one_minute_later = now+datetime.timedelta(minutes=2)
print(one_minute_later)
# 增加一个小时
one_hour_later = now+datetime.timedelta(hours=2)
print(one_hour_later)
