
import requests
from bs4 import BeautifulSoup
import csv
# URL of the page containing the town names
url = "https://meteo.go.ke/forecast/todays-weather/"

# Function to fetch the webpage content
def fetch_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# Function to extract minimum and maximum temperatures from the HTML content
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
html_content = fetch_page_content(url)

# second program #################
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
        min_temp_tag = temp_detail.find('span', string='Min: ')
        max_temp_tag = temp_detail.find('span', string='Max: ')
        if min_temp_tag:
            min_temp = min_temp_tag.find_next_sibling(string=True).strip()
            min_temperatures.append(min_temp)
        else:
            min_temperatures.append("N/A")  # Handle missing min temperature
        if max_temp_tag:
            max_temp = max_temp_tag.find_next_sibling(string=True).strip()
            max_temperatures.append(max_temp)
        else:
            max_temperatures.append("N/A")  # Handle missing max temperature
    return min_temperatures, max_temperatures

# Fetch the content of the webpage
new_html_content = fetch_page_content(url_1)

if new_html_content:
    # Extract the town names
    towns = extract_town_names(html_content)
    # Extract the minimum and maximum temperatures
    min_temperatures, max_temperatures = extract_temperatures(html_content)

    # Combine the extracted data into a single list
    weather_data = zip(towns, min_temperatures, max_temperatures)





##########################################
if html_content:
    # Extract the minimum and maximum temperatures
    min_temperatures, max_temperatures = extract_temperatures(html_content)
    # Print the list of minimum temperatures
    print("List of Minimum Temperatures:")
    print(min_temperatures)
    print("\nList of Maximum Temperatures:")
    print(max_temperatures)
    weather_data = zip(min_temperatures, max_temperatures)
    
    with open('TEMP DATA_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Min ', 'Max']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for min_temp, max_temp in weather_data:
            writer.writerow({'Min ':min_temp, 'Max':max_temp})
    print("TEMP CSV CREATED")

else:
    print("Failed to fetch the webpage content.")
