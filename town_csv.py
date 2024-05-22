import requests
from bs4 import BeautifulSoup
import csv

# URL of the page containing the town names
url_1 = "https://meteo.go.ke/forecast/todays-weather/"

# Function to fetch the webpage content
def fetch_page_content(url_1):
    response = requests.get(url_1)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to extract town names from the HTML content
def extract_town_names(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    town_names = []
    for town_div in soup.find_all('div', class_='views-field views-field-field-town'):
        town_name = town_div.find('div', class_='field-content').get_text().strip()
        town_names.append(town_name)  # Append each town name to the list
    return town_names

# Function to extract temperatures from the HTML content
def extract_temperatures(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    min_temperatures = []
    max_temperatures = []
    for temp_detail in soup.find_all('div', class_='temp-detail'):
        min_temp_tag = temp_detail.find('span', text='Min: ')
        max_temp_tag = temp_detail.find('span', text='Max: ')
        if min_temp_tag:
            min_temp = min_temp_tag.find_next_sibling(text=True).strip()
            min_temperatures.append(min_temp)
        if max_temp_tag:
            max_temp = max_temp_tag.find_next_sibling(text=True).strip()
            max_temperatures.append(max_temp)
    return min_temperatures, max_temperatures
# Fetch the content of the webpage
html_content = fetch_page_content(url_1)

if html_content:
    # Extract the town names
    towns = extract_town_names(html_content)
    # Extract the minimum and maximum temperatures
    min_temperatures, max_temperatures = extract_temperatures(html_content)

    # Combine the extracted data into a single list
    weather_data = zip(towns, min_temperatures, max_temperatures)
    # convert the weather data from zipped object to a dictionary
    
    weather_data = list(weather_data)
    print(weather_data)
       
    # Write the data into a CSV file
    with open('weather_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Town', 'Min Temp', 'Max Temp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for town, min_temp, max_temp in weather_data:
            writer.writerow({'Town': town,'Min Temp':min_temp, 'Max Temp':max_temp})

    print("Weather data has been written to 'weather_data.csv' successfully.")
else:
    print("Failed to fetch the webpage content.")
