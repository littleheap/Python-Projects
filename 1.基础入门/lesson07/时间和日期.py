import time

print(time.time())
print(time.localtime())
for i in range(3):
    time.sleep(0.5)
    print("Tick!")

print("--------------------")

import datetime

print("today is: ", datetime.date.today())
print("now is: ", datetime.datetime.now())
print(datetime.date(2016, 6, 4))
print(datetime.time(14, 00))

print("--------------------")

# 计算昨天和明天的日期
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print(yesterday, today, tomorrow)
