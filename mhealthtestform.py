from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox()


myEmail = "qatestich@gmail.com"
myName = "testname"
mySurname = "testSurname"
mySite = "testSite"
myPhone = "999852858"


class testForms():

    def checkMail(login, password):

        numberMes = 1
        curMail = 0
        driver.maximize_window()

        driver.get("https://mail.ru/")

        if EC.element_located_to_be_selected("mailbox:login"):
            driver.find_element_by_id("mailbox:login").send_keys(login)
            driver.find_element_by_id("mailbox:password").send_keys(password)
            driver.find_element_by_class_name("o-control").submit()
            driver.get("https://e.mail.ru/messages/inbox/")
        else:
            driver.get("https://e.mail.ru/messages/inbox/")

        driver.save_screenshot("inbox.png")

        if EC.element_located_to_be_selected("b-datalist__body"):
            print(driver.find_element_by_class_name("b-datalist__body"))
            mailLists = driver.find_elements_by_xpath("//*[@class='b-datalist__body']/div/div/a")
            print(mailLists)

            for i in range(len(mailLists)):
                mailLists = driver.find_elements_by_xpath("//*[@class='b-datalist__body']/div/div/a")
                EC.visibility_of_all_elements_located
                mailLists[curMail].click()
                time.sleep(2)
                driver.save_screenshot("message" + str(numberMes) + ".png")
                numberMes += 1
                curMail += 1
                driver.back()
        else:
            print("no letters")
            driver.quit()

        driver.quit()



