import requests

def main():

    print_header()
    code = input("What zipcode would you like the results for? ")
    html = get_html(code)
    # parse html
    # display forecast


def print_header():
    print("--------------------------------")
    print("       WEATHER REPORT")
    print("--------------------------------")
    print()


def get_html(zipcode):
    url = "http://www.wunderground.com/weather/{}".format(zipcode)
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    main()