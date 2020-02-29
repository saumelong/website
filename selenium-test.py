# Script for test the website deployed in node tester.
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path='/home/saumelong/chromedriver', chrome_options=chrome_options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
driver.get('http://13.88.216.239:82/') 

print(driver.title)
