from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()


myEmail = "qatestich@gmail.com"
myName = "testname"
mySurname = "testSurname"
mySite = "testSite"
myPhone = "999852858"


class innotechForm():

    def subscribe(self):
        driver.get("https://innotech.ua/ru")

        emailInput = driver.find_element_by_id("newssubscribe-email")
        emailInput.send_keys(myEmail)
        nameInput = driver.find_element_by_id("newssubscribe-name")
        nameInput.send_keys(myName)
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div/form/div/div[4]/input").submit()

    def checkMail(login, password):
        driver.get("https://mail.ru/")
        if EC.element_located_to_be_selected("mailbox:login"):
            driver.find_element_by_id("mailbox:login").send_keys(login)
            driver.find_element_by_id("mailbox:password").send_keys(password)
            driver.find_element_by_class_name("o-control").submit()
            driver.get("https://e.mail.ru/messages/inbox/")
        else:
            driver.get("https://e.mail.ru/messages/inbox/")
        screen = driver.save_screenshot("screen.png")















