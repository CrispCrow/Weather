from dotenv import load_dotenv
load_dotenv()

from src.weather_api_service import get_weather_info


def main() -> None:
    data = get_weather_info()

    print(
        f'Sunrise: {data.sunrise}\n'
        f'Sunset: {data.sunset}\n'
        f'Temperature: {data.temperature}° Celsius\n'
        f'Wind Speed: {data.wind_speed}m/s\n'
        f'Weather: {data.weather}'
    )


if __name__ == '__main__':
    main()
