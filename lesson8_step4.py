from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    from selenium.webdriver.common.by import By

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла