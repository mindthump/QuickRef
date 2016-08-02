__author__ = 'ed'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import ddt

browser = webdriver.Firefox()

browser.get("http://demo.magentocommerce.com/")

assert 'Madison Island' in browser.title

query_input = browser.find_element_by_id("search")
query_input.send_keys("earbuds" + Keys.RETURN)
browser.find_element("title", "Madison Earbuds")

browser.quit()