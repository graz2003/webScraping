import requests
from bs4 import BeautifulSoup
import csv

def scrape_page(soup, weather):
    # retrieving all the quote <div> HTML element on the page
    weather_elements = soup.find_all('div', class_='detailed-metrics')
    # iterating over the list of quote elements
    # to extract the data of interest and store it
    # in quotes
    for weather_element in weather_elements:
        # extracting each individual part of the element
        label = weather_element.find('span', class_='label').text
        value = weather_element.find('span', class_= 'value').text

        # appending a dictionary containing the quote data
        # in a new format in the quote list
        weather.append(
            {
                'label': label,
                'value': value,
            }
        )
    
    print(weather)

# the url of the home page of the target website
base_url = 'https://www.theweathernetwork.com/ca/weather/alberta/calgary'

# defining the User-Agent header to use in the GET request below
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# retrieving the target web page
page = requests.get(base_url, headers=headers)

# parsing the target web page with Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')

# initializing the variable that will contain data 
weather = []

# scraping the home page
scrape_page(soup, weather)

# reading  the "quotes.csv" file and creating it
# if not present
csv_file = open('items.csv', 'w', encoding='utf-8', newline='')

# initializing the writer object to insert data
# in the CSV file
writer = csv.writer(csv_file)

# writing the header of the CSV file
writer.writerow(['Label', 'Value'])

# writing each row of the CSV
for item in weather:
    writer.writerow(item.values())

# terminating the operation and releasing the resources
csv_file.close()


