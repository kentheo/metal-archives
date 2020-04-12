import time
from selenium import webdriver

url = "www.google.com"
driver = webdriver.Chrome('/home/kendeas93/Downloads/chromedriver_linux64/chromedriver')

driver.get('http://www.google.com/')
time.sleep(5)  # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5)  # Let the user actually see something!
driver.quit()

