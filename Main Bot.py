from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


# Path to your WebDriver
#driver_path = 'C:/Users/dsfel/OneDrive - University of Waterloo/DAVID/Personal/Projects/2023/Facebook Bot/chromedriver_win32/chromedriver.exe'

#driver = webdriver.Chrome()

# Rest of the code...

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome()

driver.get("https://sslproxies.org/")
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered']//th[contains(., 'IP Address')]"))))
print("Part 1")
#test = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr/td[1]")))
#print(test.get_attribute("innerHTML"))  
for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr/td[1]"))):
    print(my_elem.get_attribute("innerHTML"))
    print("my name jeff")
#ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr[@role='row']/td[position() = 1]")))]
print("Part 2")
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr[@role='row']/td[position() = 2]")))]
print("Part 3")
driver.quit()

proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)
for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        options.add_argument('--proxy-server={}'.format(proxies[i]))
        driver = webdriver.Chrome()
        driver.get("https://www.whatismyip.com/proxy-check/?iref=home")
        if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
            break
    except Exception:
        driver.quit()

print("Proxy Invoked")

try:
    # Open the website
    driver.get('https://whatismyipaddress.com/')  # Replace with the actual URL

    # Wait for the page to load
    time.sleep(5000)

    # Find the search box (adjust the selector as needed)
    #element = driver.find_element_by_id('Work')  # Example selector

    element = driver.find_element(By.ID, "Work")
    
    # Type in the search query
    #search_box.send_keys('Nintendo')
    #search_box.send_keys(Keys.RETURN)  # Press Enter

    # Wait for results to load
    time.sleep(5)

    # Extract data (adjust according to the webpage's structure)
    # ...

finally:
    # Close the browser
    driver.quit()
