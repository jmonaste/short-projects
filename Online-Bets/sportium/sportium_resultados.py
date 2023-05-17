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

# Maximizar la ventana del navegador
driver.maximize_window()

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



# Hacer clic en el botón "DEPORTES"
boton_deportes = driver.find_element(By.XPATH, '//li[a[contains(text(), "DEPORTES")]]')
boton_deportes.click()

# Hacer clic en el enlace "Resultados"
enlace_resultados = driver.find_element(By.XPATH, '//li[a[contains(text(), "Resultados")]]')
enlace_resultados.click()




# Obtener las ventanas abiertas
ventanas = driver.window_handles

# Cambiar el enfoque a la nueva ventana
driver.switch_to.window(ventanas[-1])

# Realizar operaciones en la nueva ventana
# Aquí puedes agregar tus operaciones adicionales en la nueva ventana



# Hacer clic en el elemento "En directo"
elemento_en_directo = driver.find_element(By.CLASS_NAME, 'sr-dropdown-container')
elemento_en_directo.click()
# Esperar 10 segundos
time.sleep(10)











# Cerrar la nueva ventana
driver.close()

# Cambiar el enfoque de vuelta a la ventana original
driver.switch_to.window(ventanas[0])


# Close the browser
driver.quit()
