# 🧪 Proyecto de Automatización - SauceDemo Tests

Este proyecto forma parte del curso **Automation Testing** del programa **Talento Tech**.  
Su objetivo es automatizar pruebas funcionales sobre el sitio [saucedemo.com](https://www.saucedemo.com) utilizando **Selenium** y **Pytest**.

---

## 🎯 Propósito del Proyecto

El propósito del proyecto es **validar el correcto funcionamiento de la página web SauceDemo** a través de tres pruebas automatizadas que simulan acciones reales de un usuario:

1. **Test de Login Correcto:**  
   Verifica que el usuario pueda iniciar sesión correctamente con credenciales válidas.

2. **Test de Navegación e Inventario:**  
   Comprueba que, una vez dentro del sitio (`inventory.html`), se muestren todos los elementos esperados:  
   - El botón de menú lateral  
   - El filtro de productos  
   - El título "Products"  
   - Y la lista de productos visibles en pantalla

3. **Test de Carrito de Compras:**  
   Agrega un producto al carrito y valida que el producto efectivamente aparezca dentro del carrito.

Además se cuenta con un reporte de todas las pruebas hechas en la carpeta reports/report.html

---

## ⚙️ Tecnologías Utilizadas

- **Python 3.10+**
- **Selenium** (para la automatización del navegador)
- **Pytest** (para la ejecución y reporte de tests)
- **ChromeDriver** (para controlar Google Chrome)
---

## 🚀 Instalación y Configuración

### Clonar el repositorio

```bash
git clone https://github.com/leonelSubelza/pre-entrega-automation-testing-Leonel-Subelza.git
cd pre-entrega-automation-testing-Leonel-Subelza
```

### 🧪 Cómo Ejecutar las Pruebas
Para ejecutar todas las pruebas abrir una terminal sobre el proyecto y ejecutar

```bash
py -m pytest -v
```

<!--
### 🧰 Ejemplo de Ejecución
```bash
============================================================================== test session starts ==============================================================================
platform win32 -- Python 3.13.7, pytest-8.4.1, pluggy-1.6.0 -- C:\Users\TuUsuario\AppData\Local\Programs\Python\Python313\python.exe
cachedir: .pytest_cache
metadata: {'Python': '3.13.7', 'Platform': 'Windows-10-10.0.19045-SP0', 'Packages': {'pytest': '8.4.1', 'pluggy': '1.6.0'}, 'Plugins': {'html': '4.1.1', 'metadata': '3.1.1', 'mocplugins: html-4.1.1, metadata-3.1.1, mock-3.15.0
collected 3 items                                                                                                                                                                 

tests/test_browsing.py::test_browsing PASSED                                                                                                                               [ 33%] 
tests/test_login.py::test_valid_login PASSED                                                                                                                               [ 66%] 
tests/test_product_interaction.py::test_add_product_to_cart PASSED                                                                                                         [100%] 

============================================================================== 3 passed in 13.81s ===============================================================================
```
-->