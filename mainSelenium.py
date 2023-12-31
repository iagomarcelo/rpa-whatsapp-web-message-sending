from selenium import webdriver
import time

# Caminho para o seu driver do navegador (por exemplo, ChromeDriver)
# Certifique-se de baixar a versão adequada para o seu navegador
driver_path = '/chromedriver'

# URL do WhatsApp Web
whatsapp_web_url = 'https://web.whatsapp.com/'

# Inicializa o navegador (nesse exemplo, Chrome)
driver = webdriver.Chrome() #executable_path=driver_path

# Abre o WhatsApp Web
driver.get(whatsapp_web_url)

# Aguarde um tempo para que o usuário possa fazer login manualmente
time.sleep(15)  # Ajuste conforme necessário

# Encerre o navegador após algum tempo
time.sleep(60)  # Ajuste conforme necessário
driver.quit()
