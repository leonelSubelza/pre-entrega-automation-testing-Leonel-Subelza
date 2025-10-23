import pytest
from selenium import webdriver
from utils.saucedemo import login

@pytest.fixture
def driver():
  driver = webdriver.Chrome()
  yield driver
  driver.quit()
  
@pytest.fixture
def login_in_driver(driver):
  login(driver,"standard_user","secret_sauce")  
  return driver
  