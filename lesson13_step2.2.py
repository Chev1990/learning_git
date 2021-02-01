# coding=utf-8
from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select



browser = webdriver.Chrome()
try:
    link = "http://suninjuly.github.io/selects2.html"#"http://suninjuly.github.io/selects1.html"
    browser.get(link)

    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    print (int(x))
    y_element = browser.find_element_by_id("num2")
    y = y_element.text

    y = int(x) + int(y)

    print (y)

    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(str(y)) # ищем элемент с текстом из списка

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
  #  browser.quit()
