from selenium import webdriver 
from selenium.webdriver.common.by import By
from time import sleep

# List situs yang ingin dibuka 
situs = ["https://www.tiket.com", "https://www.tokopedia.com", "https://www.orangsiber.com","https://demoqa.com","https://automatetheboringstuff.com"] 
 
# Inisialisasi browser Chrome 
driver = webdriver.Chrome() 
driver.minimize_window()
 
# Looping untuk membuka setiap situs 
for url in situs: 
    driver.get(url) 
    sleep(2)  
    title=driver.title
    print(f"Title dari {url}: {title}")
 
# Menutup browser 
driver.quit()