import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def get_forecast(birthdate, birthzodiac):
    # Get today's date in mm/dd/yyyy format
    today = datetime.now().strftime('%m/%d/%Y')
    # Get tomorrow's date in mm/dd/yyyy format
    tomorrow = (datetime.now() + timedelta(days=1)).strftime('%m/%d/%Y')

    # Determine the forecast type based on the birthdate input
    if birthdate.lower() == 'today':
        forecast_type = 'daily'
        birthdate = today
    elif birthdate.lower() == 'tomorrow':
        forecast_type = 'tomorrow'
        birthdate = tomorrow
    else:
        print("Invalid date. Please enter either 'today' or 'tomorrow'.")
        return

    # Construct the URL
    url = f"https://astrologyk.com/horoscope/{forecast_type}"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # This is a placeholder for the forecast. Replace it with the actual logic to extract the forecast from the website.
    forecast = soup.find('div', {'class': 'forecast'})

    print(f"Date: {birthdate}")
    print(f"Chinese Zodiac: {birthzodiac}")
    print(f"Forecast: {forecast}")

print("Please enter 'today' or 'tomorrow' for the birthdate.")
birthdate = input("Enter the birthdate: ")
birthzodiac = input("Enter your Chinese Zodiac animal: ")
get_forecast(birthdate, birthzodiac)