import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:/Program Files/Google/Chrome/chromedriver")
driver.get("https://www.cia.gov/the-world-factbook/countries/argentina/#people-and-society")
country1 = driver.find_element(By.TAG_NAME, 'div').text
print(country1)
driver.implicitly_wait(3)
country1 = driver.find_element(By.TAG_NAME, 'div').screenshot('Argentina.jpeg')
print(data)
facts = driver.find_element(By.TAG_NAME,'a').screenshot('Argentina.png')

driver.implicitly_wait(3)
country2 = driver .get("https://www.cia.gov/the-world-factbook/countries/brazil/#people-and-society")
print(country2)
driver.implicitly_wait(3)
country2 = driver.find_element(By.TAG_NAME, 'div').text
print(country2)
facts2 = driver.find_element(By.TAG_NAME,'a')

