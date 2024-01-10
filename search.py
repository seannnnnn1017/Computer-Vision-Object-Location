import sys
sys.path.insert(0, "C:/Users/fishd/Desktop/Github/Computer-Vision-Object-Location/chromedriver-win64/chromedriver.exe")
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import urllib.request
import os
import time

# Create DataFrame with XPaths
f = pd.DataFrame(index=range(1200), columns=['xpath', 'src'])
for w in range(1200):
    f.xpath[w] = '//*[@id="islrg"]/div[1]/div[' + str(w) + ']/a[1]/div[1]/img'

f1 = f.drop(f.index[:1])


# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')


# Initialize ChromeDriver
chrome_path = 'C:/Users/fishd/Desktop/Github/Computer-Vision-Object-Location/chromedriver-win64/chromedriver.exe'
chrome_service = ChromeService(chrome_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
with webdriver.Chrome() as driver:
    # Get user input for the search term
    word = input("What are you looking for? ")
    url = "http://images.google.com/search?q=" + word + "&tbm=isch&sout=1"
    driver.get(url)

        


    # Define lambda function to get image src
    def lambd(a):
        try:
            image_element = driver.find_element("xpath", a)
            if image_element.get_attribute("data-src"):
                return image_element.get_attribute("data-src")
            elif image_element.get_attribute("src"):
                return image_element.get_attribute("src")
            else:
                return None
        except NoSuchElementException:
            return None

    # Apply lambda function to get src values
    f1['src'] = f1['xpath'].apply(lambda x: (lambd(x)))

    f2 = f1.dropna()

    # Create 'pics' directory
    os.makedirs('pics', exist_ok=True)

    # Download images
    for i in range(len(f2)):
        urllib.request.urlretrieve(f2.src.iloc[i], 'pics/image' + str(i) + ".jpg")

    # Close the driver

    driver.close()
print('over')