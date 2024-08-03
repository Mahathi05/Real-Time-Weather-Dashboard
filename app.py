import requests
import streamlit as st

# Define API key and base URL
API_KEY = '72058a1e94124ebbdac89d9e559629c2'  # Replace with your actual API key
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

# Function to get weather data
def get_weather(city):
    try:
        complete_url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(complete_url)
        data = response.json()
        
        # Debugging: Print the raw JSON response
        print(data)

        if response.status_code == 200 and "main" in data:
            main = data["main"]
            wind = data["wind"]
            weather_desc = data["weather"][0]["description"]
            weather_data = {
                "City": city,
                "Temperature (°C)": main["temp"],
                "Pressure (hPa)": main["pressure"],
                "Humidity (%)": main["humidity"],
                "Wind Speed (m/s)": wind["speed"],
                "Description": weather_desc
            }
            return weather_data
        else:
            return None
    except Exception as e:
        # Debugging: Print the exception
        print(e)
        return None

# Streamlit app
st.title("Real-Time Weather Dashboard")

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    if city:
        weather = get_weather(city)
        if weather:
            st.write(f"**City**: {weather['City']}")
            st.write(f"**Temperature (°C)**: {weather['Temperature (°C)']}")
            st.write(f"**Pressure (hPa)**: {weather['Pressure (hPa)']}")
            st.write(f"**Humidity (%)**: {weather['Humidity (%)']}")
            st.write(f"**Wind Speed (m/s)**: {weather['Wind Speed (m/s)']}")
            st.write(f"**Description**: {weather['Description']}")
        else:
            st.error("City not found or API request failed")
    else:
        st.error("Please enter a city name")
