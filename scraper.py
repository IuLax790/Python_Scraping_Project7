import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver")
driver.get("https://www.cia.gov/the-world-factbook/countries/argentina/#people-and-society")
data = driver.find_element(By.TAG_NAME, 'div').text
print(data)
driver.implicitly_wait(3)
data = driver.find_element(By.TAG_NAME, 'div').screenshot('Argentina.jpeg')
print(data)
facts = driver.find_element(By.TAG_NAME,'a').screenshot('Argentina.png')

