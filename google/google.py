from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def busca():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/search?q=xiaomi+14+pro&sca_esv=e51918ddf39b0c56&tbm=shop&source=lnms&biw=982&bih=695&dpr=1.25")
    driver.maximize_window()
    
    #class i0X6df - fazer um loop com range de 10 para coletar nome, preço e link de cada class
    
    
    
    
    
    
    
    
    
    
    
    
    time.sleep(1800)

busca()