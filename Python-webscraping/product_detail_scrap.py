import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from selenium import webdriver
import mysql.connector

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



driver = uc.Chrome()
driver.get("https://www.doordash.com/store/1912-coffee-and-bites-marlin-23684201/")
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="cassie_accept_all_pre_banner"]').click()
time.sleep(3)
address= driver.find_element(By.XPATH, '//*[@id="FieldWrapper-3"]')
address.send_keys('835 53rd St Pullman, Michigan(MI), 49450')
time.sleep(2)
time.sleep(5)
address.send_keys(Keys.ENTER)
time.sleep(8)
driver.find_element(By.XPATH, '//*[@id="prism-modal-footer"]/button').click()
product_xpath= "(//button[@class='styles__StyledButtonRoot-sc-1ldytso-0 gnVsrc'])[7]"
wait(product_xpath)
element = driver.find_element(By.XPATH,product_xpath)
element.click()
time.sleep(5)
flag= True
i=1
detail_list=[]


while flag== True:
    try:
        detail_xpath = "(//div[@class='styles__ModalContent-sc-89otqx-4 eZQuEH']//div[@class='Inline__StyledInline-sc-1x9qr46-0 iDYccX'])[" + str(
            i) + "]/span"
        single_detail = driver.find_element(By.XPATH,detail_xpath)
        text=single_detail.text
        detail_list.append(text)
        i+=1

    except:
        flag=False
print(detail_list)

conn = mysql.connector.connect(
    user='root', password='maazali786', host='127.0.0.1', database='scrapping_database')
cursor = conn.cursor()
query_0 = "CREATE TABLE IF NOT EXISTS saadscrap (Id INT AUTO_INCREMENT PRIMARY KEY, Add_on VARCHAR(1000))"
cursor.execute(query_0)
query1 = "INSERT INTO saadscrap (Add_on) VALUES (%s)"
for item in detail_list:
    print(item)
    row = [item]
    cursor.execute(query1, row)
conn.commit()
conn.close()
driver.quit()

