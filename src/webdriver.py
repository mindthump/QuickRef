__author__ = 'ed'

"""This does not (yet) work in my basic docker"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("http://demo.magentocommerce.com/")

assert 'Madison Island' in browser.title

query_input = browser.find_element_by_id("search")
query_input.send_keys("earbuds" + Keys.RETURN)
browser.find_element("title", "Madison Earbuds")

browser.quit()