# Live weather-tracking application created on 10/16/2021 by Andrew P. Jones

import requests
from bs4 import BeautifulSoup

# standard headers for html parsing
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 " \
          "(KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}


def get_weather(search_city):
    search_city = search_city.replace(" ", "+")
    # search for the desired URL using the input city
    res = requests.get(f'https://www.google.com/search?q={search_city}&oq={search_city}'
                       f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching for weather..... \n")
    # create the "soup" to allow for parsing
    soup = BeautifulSoup(res.text, 'html.parser')
    # find relevant information regarding weather using their respective class names
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    precipitation = soup.select('#wob_pp')[0].getText().strip()
    humidity = soup.select('#wob_hm')[0].getText().strip()
    wind = soup.select('#wob_ws')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    # print the data
    print(location)
    print(time)
    print(info)
    print(f'Precipitation: {precipitation}, Humidity: {humidity}, Wind: {wind}')
    print(f'{weather}°F\n')


if __name__ == '__main__':
    # infinite menu loop
    while True:
        # get user input and do the requested job
        city = input("Enter the name of any city or 'Exit' to end: ")
        if city.lstrip() == "exit":
            break
        city = city + " weather"
        get_weather(city)

