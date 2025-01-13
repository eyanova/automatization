from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)


    firstbutton = browser.find_element(By.CSS_SELECTOR, ".trollface")
    firstbutton.click()
    time.sleep(1)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)


    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))


    n = browser.find_element(By.ID, "input_value")
    num = n.text
    y = calc(num)

    inp = browser.find_element(By.ID, "answer")
    inp.send_keys(y)


    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert.text)

    browser.quit()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()




