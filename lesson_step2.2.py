from selenium import webdriver
import time, math, os
from selenium.webdriver.support.ui import Select

# browser = webdriver.Chrome()
# # browser.get("http://suninjuly.github.io/selects1.html")
# browser.get("http://suninjuly.github.io/selects2.html")
#
# x = browser.find_element_by_xpath('//*[@id="num1"]').text
# y = browser.find_element_by_xpath('//*[@id="num2"]').text
# z = str(int(x) + int(y))
#
# select = Select(browser.find_element_by_tag_name("select"))
# select.select_by_value(z)
#
# button = browser.find_element_by_class_name('btn')
# button.click()
#
# time.sleep(6)
# browser.quit()

# ================================================================

# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/execute_script.html")
#
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
#
# x_element = browser.find_element_by_id('input_value')
# x = x_element.text
# y = calc(x)
#
# input1 = browser.find_element_by_xpath("//input[@id='answer']").send_keys(y)
# input2 = browser.find_element_by_xpath("//input[@id='robotCheckbox']").click()
#
# input3 = browser.find_element_by_xpath("//input[@id ='robotsRule']")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# input3.click()
#
# button = browser.find_element_by_xpath("//*[@class='btn btn-primary']")
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# button.click()
#
# time.sleep(12)

# browser.quit()

# ===========================================================================

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

browser.find_element_by_name("firstname").send_keys("Vira")
browser.find_element_by_name("lastname").send_keys("Kobrynchuk")
browser.find_element_by_name("email").send_keys("virakobrynchuk@gmail.com")

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
browser.find_element_by_id("file").send_keys(file_path)


button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(12)

browser.quit()





