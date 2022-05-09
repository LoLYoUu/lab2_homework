import requests

s_city = "Moscow,RU"
appid = "ccbcced32f61229d3cd1ae641af0afbc"

res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", s_city)
print(" Скорость ветра:", data['wind']['speed'])
print("Видимость:", data['visibility'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': s_city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})

data = res.json()
print("Скорость вестра и видимость на неделю:")
for i in data['list']:
    print("Дата <", i['dt_txt'], "> \r\nСкорость ветра <",
'{0}'.format(i['wind']['speed']), "> \r\nВидимость <",
i['visibility'], ">")
print("____________________________")