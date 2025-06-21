
from api_fetch.fetch_weather import fetch_weather_data
from spark_process.spark_weather import process_weather_data
from sql.load_to_mysql import load_to_mysql_data

def main():
    print("\n Step 1: Fetching weather data from API...")
    fetch_weather_data("Chennai", "4092d92f7eabc9964f3f4c2c4d41e0bc", "data/weather.csv")

    print("\n Step 2: Processing weather data with PySpark...")
    process_weather_data()

    print("\n Step 3: Loading data into MySQL...")
    load_to_mysql_data()

    print("\n Pipeline execution completed successfully!\n")

if __name__ == "__main__":
    main()


