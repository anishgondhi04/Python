import requests
from bs4 import BeautifulSoup

# Enter the DoorDash store URL to scrape
store_url = "https://www.doordash.com/en-CA/store/taco-bell-ogdensburg-23109443/?pickup=false"

# Send a GET request to the DoorDash store page
response = requests.get(store_url)

# Parse the HTML content with BeautifulSoup
#soup = BeautifulSoup(response, 'lxml')
print(response)
# Extract the menu items and their add-ons
#menu_items = soup.find_all('div', {'data-anchor-id': 'MenuItem'})
#for item in menu_items:
    # Extract the name and price of the menu item
  #  name = item.find('h3', {'data-telemetry-id': 'StoreMenuItem.title'}).text.strip()
 #   price = item.find('div', {'data-anchor-id': 'StoreMenuItemPrice'}).text.strip()
#    print(name, price)
# Extract the add-ons for the menu item
#add_ons = soup.find_all('div', {'data-anchor-id': 'ItemModal'})
#add_ons = soup.find_all('div', {'data-anchor-id': 'ItemModal'})
#for add_on in add_ons:
# add_on_name = add_on.find_next('div', {'class': 'Inline__StyledInline-sc-1x9qr46-0 iDYccX'}).text.strip()
