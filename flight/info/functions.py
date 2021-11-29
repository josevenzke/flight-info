from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def scrap_data(name: str) -> dict:
    """Coleta informações de aerodromos através do
    site da AISWEB e as retorna em um dict"""

    options = Options()
    options.headless = True
    options.add_argument("--window-size=1920,1080")

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=options, service=s)
    driver.get(f"https://aisweb.decea.mil.br/?i=aerodromos&codigo={name}")

    try:
        error = driver.find_element(
            By.XPATH, "/html/body/div/div/section/div/div[1]/div/div"
        )
        return False
    except:
        pass

    try:
        sunrise = driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div[1]/h4/sunrise"
        ).text
        sunset = driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/div[2]/div[1]/div[2]/h4/sunset"
        ).text
    except:
        sunrise = ""
        sunset = ""

    try:
        metar = driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/div[2]/p[2]"
        ).text
        tarf = driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[2]/div[2]/p[3]"
        ).text
    except:
        metar = ""
        tarf = ""

    try:
        div = driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[2]")
        listas = div.find_elements(By.TAG_NAME, "li a")
    except:
        listas = []

    links_info = []
    for i in range(len(listas)):
        date = listas[i]

        links_info.append({"text": date.text, "link": date.get_attribute("href")})

    context = {
        "sunrise": sunrise,
        "sunset": sunset,
        "metar": metar,
        "tarf": tarf,
        "links": links_info,
    }

    return context
