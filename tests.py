from selenium import webdriver

link = 'https://stackoverflow.com/nocaptcha?s=a9ba45d1-f8f6-42f6-a537-eda44b3c5aa0'

browser = webdriver.Chrome()
browser.get(link)
