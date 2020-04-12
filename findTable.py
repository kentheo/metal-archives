import time
from selenium import webdriver
import pandas as pd

df = pd.DataFrame(columns=['Band', 'Country', 'Genre', 'Status'])

url = "www.google.com"
driver = webdriver.Chrome('/home/kendeas93/Downloads/chromedriver_linux64/chromedriver')

driver.get('https://www.metal-archives.com/lists/A')
time.sleep(5)  # Let the user actually see something!

elements = driver.find_element_by_xpath('//*[@id="bandListAlpha"]/tbody')

rows = elements.find_elements_by_xpath('//*[@id="bandListAlpha"]/tbody/tr')

pos = 0
for row in rows:
    rowData = []
    cols = row.find_elements_by_tag_name('td')
    for col in cols:
        x = col.text
        rowData.append(x)
        print(x)
    print('-------------------------------')
    df.loc[pos] = rowData
    pos += 1

print('Number of rows from site: ', len(rows))

driver.quit()

print(df.head(10))

#############
# Achieved getting the first table (on A in page 1)
#############
