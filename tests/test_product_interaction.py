from selenium import webdriver          #Importamos la librería que permite controlar el navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_add_product_to_cart(login_in_driver):
  try:
    driver = login_in_driver
    
    # Espera explícita para garantizar que los productos existen
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="inventory-item"]')))
    
    cart_btn = driver.find_element(By.CSS_SELECTOR,'[data-test="shopping-cart-link"]')
    
    btn_primer_elem = driver.find_element(By.CSS_SELECTOR, '[data-test="add-to-cart-sauce-labs-backpack"]')
    btn_primer_elem.click()
    
    #esperar a que aparezca el badge de carrito
    cart_badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
    #confirmar que dice 1
    assert cart_badge.text == '1'
    
    # verificar que hay un elemento en el carrito
    cart_btn.click()
    assert driver.find_element(By.CSS_SELECTOR, '[data-test="inventory-item"]'), "No hay elemento en carrito"
  except Exception as e:
    print(f"Error en test_product_interaction: {e}")
    raise