import csv
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
import sys
from selenium.webdriver.common.keys import Keys
import random
import time




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



# Configurar undetected_chromedriver
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Iniciar el navegador utilizando undetected_chromedriver
driver = uc.Chrome(options=options)

# Access the URL and wait for the page to load.
driver.get(url)
driver.maximize_window()



# Encontrar el elemento del botón por la clase CSS
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button.button--full.button--midnight")))
boton = driver.find_element(By.CLASS_NAME, "button.button--full.button--midnight")
boton.click() 


# Esperar hasta que aparezca el elemento "Log in"
boton_login = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Log in')]"))
)

# Hacer clic en el botón "Log in"
boton_login.click()


# Esperar hasta que aparezca el campo de entrada de correo electrónico
campo_email = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="login[email]"]'))
)

# Limpiar el campo de entrada (opcional, dependiendo de tus necesidades)
campo_email.clear()

# Escribir tu nombre de usuario en el campo de entrada
campo_email.send_keys("javiermonasterio@gmail.com")



# Esperar hasta que aparezca el campo de entrada de contraseña
campo_contraseña = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="login[password]"]'))
)

# Limpiar el campo de entrada (opcional, dependiendo de tus necesidades)
campo_contraseña.clear()

# Escribir tu contraseña en el campo de entrada
campo_contraseña.send_keys("96eH6896e4e5gqH@e")

# Presionar la tecla Enter (si es necesario para enviar el formulario)
campo_contraseña.send_keys(Keys.ENTER)



# Esperar hasta que aparezca el iframe de Cloudflare
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[src^='https://challenges.cloudflare.com']"))
)

# Cambiar al iframe de Cloudflare
driver.switch_to.frame(iframe)

# Esperar hasta que aparezca el checkbox de Cloudflare
checkbox = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='checkbox'].rc-anchor-checkbox"))
)

# Mover el ratón sobre el checkbox
action = ActionChains(driver)
action.move_to_element(checkbox).perform()

# Hacer clic en el checkbox de Cloudflare
checkbox.click()

# Cambiar de nuevo al contexto principal
driver.switch_to.default_content()

# Continuar con el resto de tus acciones
print("Acceso conseguido!")




# Close the browser
driver.quit()
