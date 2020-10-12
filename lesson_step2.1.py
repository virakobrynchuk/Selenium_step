from selenium import webdriver
import math, time

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/math.html")
#
#
# def calc(x):
#   return str(math.log(abs(12 * math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id('input_value')
# x = x_element.text
#
# y = calc(x)
#
# input1 = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
# input2 = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
# input3 = browser.find_element_by_xpath("//input[@id ='robotsRule']").click()
# button = browser.find_element_by_xpath("//*[@class='btn btn-default']").click()
#
# time.sleep(6)
# browser.quit()

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")


def calc(x):
  return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element_by_id("treasure")
x = x_element.get_attribute("valuex")

y = calc(x)

input1 = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
input2 = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
input3 = browser.find_element_by_xpath("//input[@id ='robotsRule']").click()
button = browser.find_element_by_xpath("//*[@class='btn btn-default']").click()

time.sleep(15)
browser.quit()
