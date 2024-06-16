class weather_data:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
datas = []
for i in range(n):
    date, day, weather = input().split()
    datas.append(weather_data(date, day, weather))


for data in datas:
    if data.weather == "Rain":
        print(data.date, data.day, data. weather)
        break