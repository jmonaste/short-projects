import csv
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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
header = jsonObject['header']

iframe_xpath = jsonObject['iframe_xpath']

output_SuitNo_xpath = jsonObject['output_SuitNo_xpath']
output_ParcelNo_xpath = jsonObject['output_ParcelNo_xpath']
output_Owner_xpath = jsonObject['output_Owner_xpath']
CoOwner_xpath = jsonObject['CoOwner_xpath']
LegalDesc_xpath = jsonObject['LegalDesc_xpath']
PropertyAddress_xpath = jsonObject['PropertyAddress_xpath']
PropertyCity_xpath = jsonObject['PropertyCity_xpath']
PropertyState_xpath = jsonObject['PropertyState_xpath']
DateSold_xpath = jsonObject['DateSold_xpath']
PurchasePrice_xpath = jsonObject['PurchasePrice_xpath']
Judgment_xpath = jsonObject['Judgment_xpath']
Excess_xpath = jsonObject['Excess_xpath']
Purchaser_xpath = jsonObject['Purchaser_xpath']
PurchaserAddress_xpath = jsonObject['PurchaserAddress_xpath']
PurchaserCity_xpath = jsonObject['PurchaserCity_xpath']
PurchaserState_xpath = jsonObject['PurchaserState_xpath']
PurchaserZip_xpath = jsonObject['PurchaserZip_xpath']
HearingDate_xpath = jsonObject['HearingDate_xpath']
HearingTime_xpath = jsonObject['HearingTime_xpath']
ContinuedDate_xpath = jsonObject['ContinuedDate_xpath']
ContinuedTime_xpath = jsonObject['ContinuedTime_xpath']
Confirmed_xpath = jsonObject['Confirmed_xpath']
SetAside_xpath = jsonObject['SetAside_xpath']
Appealed_xpath = jsonObject['Appealed_xpath']
CountyPaid_xpath = jsonObject['CountyPaid_xpath']
StatePaid_xpath = jsonObject['StatePaid_xpath']
ExcessAppFiled_xpath = jsonObject['ExcessAppFiled_xpath']
ExcessDenied_xpath = jsonObject['ExcessDenied_xpath']
ExcessAppealed_xpath = jsonObject['ExcessAppealed_xpath']
ExcessPaid_xpath = jsonObject['ExcessPaid_xpath']




# Chrome driver configuration
options = Options()
options.add_argument(selenium_webdriver_useragent)
driver = webdriver.Chrome(options=options)

# Access the URL and wait for the page to load. Consideramos que se ha cargado cuando se muestra al final de la página la sección de paginación
driver.get(url)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]/div[10]")))


# Create a CSV file and write the headers
with open(csv_file, "w", newline="", encoding=csv_encoding) as csv_file:
    writer = csv.writer(csv_file, delimiter="\t")

    writer.writerow(header)

    # Find the iframe
    #iframe = driver.find_elements(By.XPATH, iframe_xpath)

    # Change Selenium context to point to iframe
    #driver.switch_to.frame(iframe[0])

    # Now you can search and manipulate the elements inside the iframe
    # To know if we have reached the end, detect if there is a 'Next' button.
    #botones_siguiente = driver.find_elements(By.XPATH, "//input[@name='Next']")
    #more_cases = True
    #if len(botones_siguiente) == 0:
          #more_cases = False
          #print('No more records')

    # Find all records on the current page and write them to the CSV file
    divs = driver.find_elements(By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div[3]/div[1]/div[1]")

    print("Cantidad de elementos en divs:", len(divs))

    divs_content = "\n\n\n\n\n".join([div.get_attribute("outerHTML") for div in divs])
    print(divs_content)


    for div in divs:
        inner_divs = div.find_elements(By.CLASS_NAME, "col-md-12.product-result-element.pro-element")


        for inner_div in inner_divs:
            # Realiza las operaciones deseadas con el div que tiene la clase especificada
            # por ejemplo, extraer información o interactuar con los elementos dentro del div
            # div.find_element(...) o div.text

            # Encuentra el elemento del título dentro del div
            title_element = inner_div.find_element(By.CLASS_NAME, "title")
            title = title_element.text
        
            # Encuentra el elemento de la descripción dentro del inner_div
            description_element = inner_div.find_element(By.CLASS_NAME, "p-desc-txt")
            description = description_element.text
            
            # Imprime el título y la descripción
            print("Título:", title)
            print("Descripción:", description)
            print("---")



# Close the browser
driver.quit()
