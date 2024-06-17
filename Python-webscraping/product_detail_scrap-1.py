import urllib
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import undetected_chromedriver as uc
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

options = uc.ChromeOptions()
options.headless = True
driver = uc.Chrome(options=options)
#url = sys.argv[1]
driver.get("https://www.doordash.com/store/taco-bell-ogdensburg-23109443/?pickup=false")
time.sleep(10)
address_field = WebDriverWait(driver, 10) .until(
    EC.presence_of_element_located((By.ID, "FieldWrapper-1"))
)
address_field.clear()
address_field.send_keys("22 Madison Ave,Ogdensburg NY")
time.sleep(5)
address_field.send_keys(Keys.ENTER)
time.sleep(5)
#driver.find_element(By.XPATH, '//*[@id="cassie_accept_all_pre_banner"]')
#driver.find_element(By.XPATH, '//*[@id="prism-modal-footer"]/button')
product_xpath = "(//button[@class='styles__StyledButtonRoot-sc-11ldytso-0 gbrzHn'])[7]"
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
print (detail_list)

conn = mysql.connector.connect(user='catersnow_test', password='XvsJoXVf5W', host='cloud.worksaar.com', database='catersnow_tes')
cursor = conn.cursor()
query_0 = "CREATE TABLE IF NOT EXISTS saadscrap (Id INT AUTO_INCREMENT PRIMARY KEY, Add_on VARCHAR(1000))"
cursor.execute(query_0)
query1 = "INSERT INTO saadscrap (Add_on) VALUES (%s)"
for item in detail_list:
    print (item)
    row = [item]
    cursor.execute(query1, row)
conn.commit()
conn.close()
driver.quit()