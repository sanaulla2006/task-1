import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

API_KEY = "94aef6c3023bdcad555021b615a5162d"
CITY = "Hyderabad"
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# === Fetch data from API ===
response = requests.get(URL)
data = response.json()

# === Parse the weather forecast data ===
dates = []
temperatures = []

for forecast in data["list"]:
    dt = datetime.datetime.fromtimestamp(forecast["dt"])
    temp = forecast["main"]["temp"]
    dates.append(dt)
    temperatures.append(temp)

# === Plot using seaborn ===
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o', color='blue')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# === Save & show the chart ===
plt.savefig("weather_dashboard.png")
plt.show()

