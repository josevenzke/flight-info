from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def scrap_data(name):
    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    s=Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options,service=s)
    driver.get(f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={name}")

    sunrise = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h4/sunrise')
    sunset = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/div[1]/div[2]/h4/sunset')
    metar = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/p[2]')
    tarf = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/p[3]')
    
    div = driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]')
    listas = div.find_elements(By.TAG_NAME, "li a")

    rows_list = []
    for i in range(len(listas)):
        date = listas[i]

        rows_list.append([date.text,date.get_attribute('href')])

    return rows_list