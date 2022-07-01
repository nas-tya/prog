from yaweather import Bangladesh, Russia, UnitedStates, YaWeather #Yandex Weather API wrapper


api_key = ''

def get_weather_data(place, api_key):

    if api_key=='':
        return None

    y = YaWeather(api_key)
    res = y.forecast(place)

    print(f'Forecast on web: {res.info.url}')
    print(f'Location (coords): {str(place)}')
    print(f'Timezone: {res.info.tzinfo.abbr}')
    print(f'Now: {res.fact.temp} °C, feels like {res.fact.feels_like} °C')
    print(f'Condition: {res.fact.condition} \n')


if __name__ == "__main__":
    get_weather_data(Russia.SaintPetersburg, api_key)
    get_weather_data(Bangladesh.Dhaka, api_key)
    get_weather_data(UnitedStates.Chicago, api_key)