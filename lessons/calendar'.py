date, month, year = map(int, input().split('/'))

year2 = int(str(year)[-3] + str(year)[-2] + str(year)[-1])

base_date, base_month, base_year = 15, 10, 1582
days = ['суббота', 'воскреснье', 'понедельник', 'вторник', 'среда',
        'четверг', 'пятница']
count_days = 0
days_in_year = 0
base_days = 0
form = 0

base_days = 365 - 4 * month + date

if (year % 4 == 0 or year2 % 400 == 0) and year2 % 100 != 0:
    days_in_year = count_days = 366 - 4 * month + date
else:
    days_in_year = count_days = 365 - 4 * month + date


for i in range(year + 1):
    if (year % 4 == 0 or year2 % 400 == 0) and year2 % 100 != 0:
        count_days += 366
    else:
        count_days += 365

form = ((base_days - 1)
        + 0.25 * (base_days - 1)
        + (days_in_year - 1)) / 7

res = days[int(str(form)[-1])]
print(res)
