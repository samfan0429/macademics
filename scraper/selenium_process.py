from selenium import webdriver
import requests

url = 'https://www.macalester.edu/registrar/schedules/2020fall/class-schedule/'
response = requests.get(url, timeout=5)

browser = webdriver.Chrome('chromedriver')
browser.get(url)

details = browser.find_elements_by_class_name("crs-detail")
print(len(details))
for x in range(0, len(details)):
    if details[x].is_displayed():
        details[x].click()


