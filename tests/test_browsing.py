from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.saucedemo import login

driver = webdriver.Chrome()

def test_browsing():
  try:
    login(driver,'standard_user','secret_sauce')
    
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
    
    
    
  finally:
    driver.quit()