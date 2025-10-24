from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_browsing(login_in_driver):
  try:
    driver = login_in_driver
    
    # Espera explícita para garantizar que los productos existen
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item"]')))
    
    # validar titulo
    products_txt = driver.find_element(By.CSS_SELECTOR, '[data-test="title"]')
    assert "Products" in products_txt.text
    
    # Validar presencia de productos 
    assert driver.find_element(By.CSS_SELECTOR,'[data-test="add-to-cart-sauce-labs-backpack"]'), "Primer producto no encontrado"
    # Nombre y precio del primero
    assert driver.find_elements(By.CSS_SELECTOR,'[data-test="inventory-item-name"]')[0].text == 'Sauce Labs Backpack' , "Titulo de Primer producto incorrecto"
    assert driver.find_elements(By.CSS_SELECTOR,'[data-test="inventory-item-price"]')[0].text == '$29.99' , "Precio de Primer producto incorrecto"
    
    # validar presencia de elementos importantes
    assert driver.find_element(By.ID,'react-burger-menu-btn'), "Botón menú no encontrado"
    assert driver.find_element(By.CSS_SELECTOR, '[data-test="product-sort-container"]'), "Filtro no encontrado"
    assert driver.find_element(By.CSS_SELECTOR, '[data-test="shopping-cart-link"]'), "Carrito no encontrado"
  except Exception as e:
    print(f"Error en test_browsing: {e}")
    raise