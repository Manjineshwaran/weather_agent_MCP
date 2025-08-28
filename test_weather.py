from weather_agent import get_weather_data

# Test the weather function directly
def test_weather():
    while True:
        city = input("Enter city name (or 'q' to quit): ")
        if city.lower() == 'q':
            break
        try:
            result = get_weather_data(city)
            print("\nWeather Information:")
            print("-" * 40)
            print(result)
            print("-" * 40 + "\n")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_weather()
