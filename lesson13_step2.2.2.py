import document as document
from selenium import webdriver
import time
import math
#from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element_by_css_selector("#input_value")
x = int(x_element.text)

print (x)
y=str(math.log((abs(12*math.sin(x)))))
print (y)

z_element = browser.find_element_by_id("answer")
z_element.send_keys(y)

option1= browser.find_element_by_id("robotCheckbox")
option1.click()

browser.execute_script("window.scrollBy(0, 100);")

option2= browser.find_element_by_id("robotsRule")
option2.click()

button = browser.find_element_by_class_name("btn.btn-primary")
button.click()
