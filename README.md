# Realtime Weather Data Pipeline 🌦️

This project implements a complete ETL (Extract, Transform, Load) pipeline to fetch real-time weather data from an API, process it using PySpark, and store the results in a MySQL database for further analysis.

 ## 🔧 Technologies Used

- **Python**: Core scripting
- **PySpark**: Data processing and transformation
- **MySQL**: Data storage
- **Pandas**: Data handling
- **API**: For real-time weather data fetching
- **CSV**: For storing interim results

## 📁 Project Structure

├── fetch_weather.py # Fetches real-time weather data from API
├── load_to_mysql.py # Loads processed data into MySQL database
├── main.py # Orchestrates the entire ETL workflow
├── spark_weather.py # Applies transformations using PySpark
├── weather.csv # Sample output/intermediate data


📊 Output

Weather data stored in weather.csv

Processed results stored in MySQL under a specified schema/table

📌 Use Cases

Real-time weather monitoring

Data analysis and visualization

Feeding analytics dashboards
