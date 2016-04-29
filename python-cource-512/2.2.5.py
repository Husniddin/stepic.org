import datetime

year, month, day = input().split(" ")
days = int(input())

n_date = datetime.date.today()

c_date = n_date.replace(int(year), int(month), int(day))

delta = datetime.timedelta(days=days)

new_date = c_date + delta

print(new_date.year, new_date.month, new_date.day)
print(new_date.strftime("%Y %m %d"))