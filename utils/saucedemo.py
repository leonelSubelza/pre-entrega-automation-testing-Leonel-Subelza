from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
import pytest
import time                             #Para hacer pausas visibles (solo demo)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# driver = webdriver.Chrome()

def login(driver,username,password):
  driver.get('https://www.saucedemo.com')
      
  #Automatización de Login:
  driver.find_element(By.ID, "user-name").send_keys(username)
  driver.find_element(By.ID, "password").send_keys(password)
  driver.find_element(By.ID, "login-button").click()
  
  # Espera a que la nueva página cargue
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'app_logo')))
  
  
  #Navegación y Verificación del Catálogo: (Clases 6 a 8)
  assert '/inventory.html' in driver.current_url, f"URL inesperada: {driver.current_url}"
  assert driver.title == 'Swag Labs'