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

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

# NEW CODE ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TO DO: Add proxy support

# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException, WebDriverException
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support. ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common. proxy import Proxy, ProxyType

# from random_user_agent.user_agent import UserAgent
# from random_user_agent.params import SoftwareName, OperatingSystem

# from time import sleep

# class Request:
#     selenium_retries = 0
#     def __init__(self,url):
#         self.url = url
#     def get_selenium_res(self,class_name):
#         software_names = [SoftwareName.CHROME.value]
#         operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem. LINUX. value]
#         user_agent_rotator = UserAgent(software_names=software_names, operating_system=operating_systems,limit=100)
#         user_agent =user_agent_rotator.get_random_user_agent()
        
#         chrome_options = Options()
#         chrome_options.add_argument('--headless')
#         chrome_options.add_argument('--no-sandbox')
#         chrome_options.add_argument('--window-s ize=1420, 1080')
#         chrome_options.add_argument('--disable-gpu')
#         chrome_options.add_argument(f'user-agent={user_agent}')
#         PROXY = "http: //gate. smartproxy. com.7000"
#         prox = Proxy()
#         prox.proxy_type = ProxyType.MANUAL
#         prox.autodetect = False
#         capabilities = webdriver.DesiredCapabilities.CHROME
#         prox.http_proxy = PROXY
#         prox.ssl_proxy = PROXY
#         prox.add_to_capabilities(capabilities)
#         browser = webdriver.Chrome(chrome_options)
#         #browser = webdriver.Chrome(chrome_options=chrome_options, desired_capabilities=capabilities)
#         browser.get(self.url)
#         # when testing proxies
#         # browser. get( i http://lumtest.com/myip.json' )
#         time_to_wait = 90
#         try:
#             WebDriverWait(browser, time_to_wait).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
#         except (TimeoutException, WebDriverException):
#             sleep(6)
#             self.selenium_retries += 1
#             return self.get_selenium_res(class_name)
#         finally:
#             browser.maximize_window()
#             page_html = browser.page_source
#             browser.close()
#             return page_html
        
# NEW CODE ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OLD PROXY CODE  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

driver = webdriver.Chrome()

driver.get("https://sslproxies.org/")
driver.execute_script("return arguments[0].scrollIntoView(true);", WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//table[@class='table table-striped table-bordered']//th[contains(., 'IP Address')]"))))
ips = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr/td[1]")))]
ports = [my_elem.get_attribute("innerHTML") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, "//table[@class='table table-striped table-bordered']//tbody//tr/td[2]")))]
driver.quit()

proxies = []
for i in range(0, len(ips)):
    proxies.append(ips[i]+':'+ports[i])
print(proxies)
for i in range(0, len(proxies)):
    try:
        print("Proxy selected: {}".format(proxies[i]))
        options = webdriver.ChromeOptions()
        #New Code 
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
        print("Init software_names", software_names)
        user_agent_rotator = UserAgent(software_names=software_names, operating_system=operating_systems,limit=100)
        print("Init user_agent_rotator", user_agent_rotator)
        user_agent =user_agent_rotator.get_random_user_agent()
        print("Init user_agent", user_agent)    
        #options.add_argument('--headless')
        #options.add_argument('--no-sandbox')
        #options.add_argument('--window-s ize=1420, 1080')
        #options.add_argument('--disable-gpu')
        #options.add_argument(f'user-agent={user_agent}')
        # Old stuff
        options.add_argument('--proxy-server=%s' % proxies[i])
        driver = webdriver.Chrome(options)
        driver.get('https://www.whatismyip.com')
        print("My IP", proxies[i])
        time.sleep(5000)
        time_to_wait = 90
        try:
            WebDriverWait(driver, time_to_wait).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))
        finally:
            driver.maximize_window()
            page_html = driver.page_source
            driver.close()
            print(page_html)
        

        # driver.get("https://www.whatismyip.com/proxy-check/?iref=home")
        # if "Proxy Type" in WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "p.card-text"))):
        #     break
    except Exception as e:
        print("Exception: ", str(e))
        driver.quit()
# OLD PROXY CODE  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SIMPLE CODE ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# try:
#     # Open the website
#     driver.get('https://whatismyipaddress.com/')  # Replace with the actual URL

#     # Wait for the page to load
#     time.sleep(5000)

#     # Find the search box (adjust the selector as needed)
#     #element = driver.find_element_by_id('Work')  # Example selector

#     element = driver.find_element(By.ID, "Work")
    
#     # Type in the search query
#     #search_box.send_keys('Nintendo')
#     #search_box.send_keys(Keys.RETURN)  # Press Enter

#     # Wait for results to load
#     time.sleep(5)

#     # Extract data (adjust according to the webpage's structure)
#     # ...

# finally:
#     # Close the browser
#     driver.quit()
# SIMPLE CODE ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
