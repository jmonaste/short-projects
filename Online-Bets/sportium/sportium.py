import csv
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import sys



# First we check if the code is executed from Python or from the .exe, because the way to get the 
# path from where the code is executed is different in both cases.
if getattr(sys, 'frozen', False):
    # Runs from the .exe
    application_path = os.path.dirname(sys.executable)
else:
    # Runs from Python
    application_path = os.path.dirname(os.path.abspath(__file__))

# Once we have the path, we read the configuration file and obtain the parameters
with open(os.path.join(application_path, "config.json")) as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

# Parameter reading
url = jsonObject['url']
csv_file = os.path.join(application_path, jsonObject['csv_filename'])
csv_encoding = jsonObject['csv_encoding']
selenium_webdriver_useragent = jsonObject['selenium_webdriver_useragent']

# Chrome driver configuration
options = Options()
options.add_argument(selenium_webdriver_useragent)
driver = webdriver.Chrome(options=options)

# Access the URL and wait for the page to load. Consideramos que se ha cargado cuando se muestra al final de la página la sección de paginación
driver.get(url)


# Encontrar el botón "Aceptar"
boton_aceptar = driver.find_element(By.CLASS_NAME, "btn.acceptCookies")
# Hacer clic en el botón "Aceptar"
boton_aceptar.click()

# Encontrar el enlace del menú de apuestas
enlace_apuestas = driver.find_element(By.XPATH, '//a[@href="https://sports.sportium.es/es"]')
# Hacer clic en el enlace del menú de apuestas
enlace_apuestas.click()



try:
    # Encontrar el botón "Aceptar"
    boton_aceptar = driver.find_element(By.CLASS_NAME, "acceptCookies")
    
    # Hacer clic en el botón "Aceptar"
    boton_aceptar.click()
    
except NoSuchElementException:
    # Si no se encuentra el botón "Aceptar", continuar sin hacer nada
    pass


category_live_xpath = "/html/body/div[1]/div/div[2]/div/div/div[2]/div[3]/h4"
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, category_live_xpath)))

# Obtener todos los divs con la clase "expander-button"
divs = driver.find_elements(By.CLASS_NAME, "expander-button")

# Recorrer los divs y mostrar el contenido del span
for div in divs:
    print("Div impresol...")
    #span = div.find_element(By.TAG_NAME, "span")
    #contenido_span = span.text
    #print(contenido_span)


# Close the browser
driver.quit()
