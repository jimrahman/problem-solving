
def get_day(day, num):

    days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']

    for i in range(len(days)):
        if days[i] == day:
            if num > 7:
                mod = num % 7 + i
                if mod > 7:
                    get = mod % 7
                    return days[get]
                else:
                    get = 7 - mod
                    return days[get]
            else:
                if (i + num) < 6:
                    get = i + num
                    return days[get]
                else:
                    get = (i + num) - 7
                    return days[get]


print(get_day("Fri", 1))
