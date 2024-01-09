from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
# Add any desired options here, such as headless mode or specific user-agent
chrome_options.headless = True
chrome_options.add_argument("--window-size=1920,1200")

chrome_service = ChromeService('/Users/gracezhou/Documents/Code-2023/WebScraping/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
driver.get("https://www.theweathernetwork.com/ca/weather/alberta/calgary")

labels = driver.find_elements(By.XPATH, '//span[@class="label"]')
values = driver.find_elements(By.XPATH, '//span[@class="value"]')

weather = []

for label in labels:
    for value in values:
        
        weather.append(
            {
                'label': label,
                'value': value,
            }
        )

print(weather)

driver.quit()

