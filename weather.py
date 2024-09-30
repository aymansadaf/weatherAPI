import requests


def get_weather(city):
    api_key = "ba68bbfff3a2c0157dcc26f55ebe54e0"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # Parameters for the API call
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Fetch temperature in Celsius
    }

    # Making a GET request to fetch the weather data
    response = requests.get(base_url, params=params)

    # Checking if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extracting relevant data from the response
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Displaying the weather data
        print(f"Weather in {city.capitalize()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found, please check the city name and try again.")


# Get city from user
city = input("Enter a city name: ")
get_weather(city)
