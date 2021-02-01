from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration2.html")

    first = browser.find_element_by_css_selector(".first_block .first")
    first.send_keys("Text")
    last = browser.find_element_by_css_selector(".first_block .second")
    last.send_keys("Text")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("Text")

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    time.sleep(2)

    welcome = browser.find_element_by_tag_name("h1")
    welcome_text = welcome.text
    assert "Congratulations! You have successfully registered!" == welcome_text


finally:
    time.sleep(10)
    browser.quit()