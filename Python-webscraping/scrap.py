import sys
import time
import urllib
import selenium
import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def wait(xpath):
    y=200
    flag=False
    while flag==False:
        try:
            driver.find_element(By.XPATH, xpath)
            flag = True
        except:
            driver.execute_script("window.scrollTo(0, " + str(y) + ")")
            y += 200
            time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, 0)")

#url = sys.argv[1]
url = "https://www.doordash.com/store/mcdonald's-ogdensburg-1657725/?cursor=eyJzdG9yZV92ZXJ0aWNhbF9pZCI6bnVsbCwic2VhcmNoX2l0ZW1fY2Fyb3VzZWxfY3Vyc29yIjp7InF1ZXJ5IjoiIiwiaXRlbV9pZHMiOltdLCJzZWFyY2hfdGVybSI6IiIsInZlcnRpY2FsX2lkIjpudWxsLCJ2ZXJ0aWNhbF9uYW1lIjoiIn0sImlzX3NpYmxpbmciOmZhbHNlLCJmb3JjZV9zdG9yZV9hdmFpbGFiaWxpdHlfdjIiOmZhbHNlfQ==&pickup=false" 
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")

options.headless = True

driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

driver.get(url)
print(driver.title)
time.sleep(3)
Menuitems = driver.find_elements_by_xpath('//div[@data-anchor-id="MenuItem"]')
Itemimgs = driver.find_elements_by_xpath('//div[@data-anchor-id="MenuItem"]//child::img')
global Item_IDs
global Item_imgs

Item_IDs = []
Item_imgs = []
for i in Menuitems:
    Item_ID = i.get_attribute("data-item-id")
    Item_IDs.append(Item_ID)
for j in Itemimgs:
    Item_img = j.get_attribute("src")
    Item_imgs.append(Item_img)
driver.quit()

db = mysql.connector.connect(
        host='cloud.worksaar.com',
        user='catersnow_test',
        password='XvsJoXVf5W',
        database='catersnow_tes'
    )
cursor = db.cursor()
query_0 = "CREATE TABLE IF NOT EXISTS" + " " + Table_name + " " + "( Id INT AUTO_INCREMENT PRIMARY KEY, Item_ID VARCHAR(1000),Image_URL VARCHAR(255))"
cursor.execute(query_0)
table_content = []
for (i, j) in zip(Item_IDs, Item_imgs):
    row = (i, j)
    table_content.append(row)
query_1 = "INSERT INTO saadscrap (Item_ID,Image_URL) VALUES (%s,%s)"
cursor.executemany(query_1, table_content)
db.commit()
db.close()