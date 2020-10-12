from selenium import webdriver
import time, math


# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/alert_accept.html")
#
# browser.find_element_by_tag_name("button").click()
#
# confirm = browser.switch_to.alert
# confirm.accept()
#
#
# def calc(x):
#     return str(math.log(abs(12 * math.sin(int(x)))))
#
# x_element = browser.find_element_by_id("input_value")
# x = x_element.text
# y = calc(x)
#
# browser.find_element_by_id("answer").send_keys(str(y))
# browser.find_element_by_tag_name("button").click()
#
#
# time.sleep(12)
#
# browser.quit()

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

browser.find_element_by_tag_name("button").click()

browser.switch_to.window(browser.window_handles[1])


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

browser.find_element_by_id("answer").send_keys(str(y))
browser.find_element_by_tag_name("button").click()


time.sleep(12)

browser.quit()


