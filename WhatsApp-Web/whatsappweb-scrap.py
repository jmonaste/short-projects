from selenium import webdriver
from selenium.webdriver.common.by import By

# Inicializar el controlador del navegador
driver = webdriver.Chrome()

# Abrir WhatsApp Web
driver.get("https://web.whatsapp.com")

# Esperar a que el usuario escanee el código QR y realice la autenticación

# Esperar hasta que se cargue la lista de chats
driver.implicitly_wait(10)  # Esperar hasta 10 segundos

# Buscar y obtener elementos en la página
# Obtener la lista de chats
chat_list = driver.find_elements(By.XPATH, "//div[@id='pane-side']//div[contains(@data-testid, 'list-item-')]")

# Iterar sobre los chats
for chat in chat_list:
    # Obtener información del chat
    chat_name = chat.find_element(By.XPATH, ".//div[@data-testid='cell-frame-title']//span").text

    # Realizar acciones deseadas con la información del chat
    print("Chat:", chat_name)
    print("---")

    # Verificar si el chat_name es igual a 'David' y hacer clic en el chat correspondiente
    if chat_name == 'Monasterio Solar':
        chat.click()


        break  # Romper el bucle una vez se encuentra el chat deseado

# Esperar hasta que se cargue el panel de conversación
driver.implicitly_wait(10)  # Esperar hasta 10 segundos

# Buscar el contenido del div 'conversation-panel-body' en toda la página
conversation_body = driver.find_element(By.XPATH, "//div[@data-testid='conversation-panel-body']")

# Obtener el texto del contenido del div
conversation_text = conversation_body.text

# Imprimir el contenido del div
print("Contenido del div 'conversation-panel-body':")
print(conversation_text)




# Cerrar el navegador
driver.quit()
