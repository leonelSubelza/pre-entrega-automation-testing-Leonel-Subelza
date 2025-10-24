from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_valid_login(driver):
  try:
    driver.get('https://www.saucedemo.com')
    
    #Automatización de Login:
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Espera explicita a que la nueva página cargue
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))    
    
    #Navegación y Verificación del Catálogo: (Clases 6 a 8)
    assert '/inventory.html' in driver.current_url, f"URL inesperada: {driver.current_url}"
    assert driver.find_element(By.CLASS_NAME, 'title').text == 'Products', f"Título inesperado: {driver.title}"
  except Exception as e:
    print(f"Error en test_login: {e}")
    raise