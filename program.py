import requests
import bs4
import collections

WeatherReport = collections.namedtuple("weatherReport",
                                       "cond, temp, scale, loc")

def main():

    print_header()
    code = input("What zipcode would you like the results for? ")
    html = get_html(code)
    report = get_weather(html)
    print("The temperature in {} is {} {} and {}".format(
        report.loc,
        report.temp,
        report.scale,
        report.cond,
    ))



def print_header():
    print("--------------------------------")
    print("       WEATHER REPORT")
    print("--------------------------------")
    print()


def get_html(zipcode):
    url = "http://www.wunderground.com/weather/{}".format(zipcode)
    response = requests.get(url)
    return response.text


def get_weather(html):
    #cityCss = "region-content-header h1"
    #weatherScaleScc = ".wu-unit-temperature.wu-label"
    #weatherTempCss = ".wu-unit-temperature.wu-value"
    #weatherConditionCss = ".condition-icon"

    soup = bs4.BeautifulSoup(html, "html.parser")
    loc = soup.find(class_="region-content-header").find("h1").get_text()
    condition = soup.find(class_="condition-icon").get_text()
    temp = soup.find(class_="wu-unit-temperature").find(class_="wu-value").get_text()
    scale = soup.find(class_="wu-unit-temperature").find(class_="wu-label").get_text()

    loc = cleanup_text(loc)
    loc = find_city_and_state(loc)
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)

    # return(condition, temp, scale, loc)
    report = WeatherReport(cond = condition, temp = temp, scale = scale, loc = loc)
    return report

def find_city_and_state(loc: str):
    parts = loc.split("\n")
    return parts[0].strip()


def cleanup_text(text : str):
    if not text:
        return text

    text = text.strip()
    return text


if __name__ == "__main__":
    main()