import urllib.request
import datetime
from bs4 import BeautifulSoup

# 引数jdateは2月5日（金）のような形式の文字列
# return 2/5
def date_convert(jdate):
    return jdate[:-3].replace('月', '/').replace('日', '')

class WeatherItem:
  def __init__(self, dt, t):
    self.date_time = dt
    self.temperature = t

  def to_string(self):
    return ' time: ' + self.date_time + '   temp:  ' + self.temperature


def get_year():
  year = '{0:%Y}'.format(datetime.datetime.now())
  return year


def main():
  # 千代田区の天気
  url = 'https://weathernews.jp/onebox/tenki/tokyo/13101/'
  req = urllib.request.Request(url)
  with urllib.request.urlopen(req) as res:
      body = res.read()
      print(res.status)
      soup = BeautifulSoup(body, 'html.parser')
      base_element = soup.find("div", class_="weather-day")
      jdate = base_element.find("div", class_="weather-day__day").p.string
      date = date_convert(jdate)
      year = get_year()
      items = base_element.find_all("div", class_="weather-day__item")
      weatheritems = list()
      for item in items:
        datetime = year + '/' + date + ' ' + item.find("p", class_="weather-day__time").string
        temperature = item.find("p", class_="weather-day__t").string[:-1]
        weatheritem = WeatherItem(datetime,temperature)
        weatheritems.append(weatheritem)

      print_weatheritems(weatheritems)

def print_weatheritems(itemlist):
  for item in itemlist:
    print(item.to_string())

if __name__ == "__main__":
    main()
