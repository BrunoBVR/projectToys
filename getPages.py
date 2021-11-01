import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Function to get next page
def getNextPage(url, slp = 10):
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url)

    driver.implicitly_wait(slp)
    nxt = driver.find_element_by_xpath(
        "//*[@id='page-navigation-bottom']/div/a[2]")
    driver.execute_script("arguments[0].click();", nxt)
    next_url = driver.current_url
    driver.quit()
    if next_url != url:
        return next_url
    else:
        return

girls_url = 'https://www.kohls.com/catalog/girls-toys.jsp?CN=Gender:Girls+Department:Toys'
boys_url = 'https://www.kohls.com/catalog/boys-toys.jsp?CN=Gender:Boys+Department:Toys'

# print(getNextPage(girls_url,10))

# Writting initial page
# with open('girls_pages.txt', 'a') as f:
with open('boys_pages.txt', 'a') as f:
    # f.write(girls_url)
    f.write(boys_url)
    f.write('\n')

current_page = 1
while True:
    print(40 * '=')
    print(f'On page {current_page}')

    # with open('girls_pages.txt', 'a') as f:
    with open('boys_pages.txt', 'a') as f:
        # f.write(getNextPage(girls_url))
        f.write(getNextPage(boys_url))
        f.write('\n')

    # girls_url = getNextPage(girls_url, slp = 5)
    boys_url = getNextPage(boys_url, slp = 5)
    current_page += 1

    # if not girls_url:
    if not boys_url:
        break
