from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Firefox(executable_path=r'C:\projects\seleniumTests\browserDrivers\geckodriver.exe')


myEmail = "x@gmail.com"
myName = "testname"
mySurname = "testSurname"
mySite = "testSite"
myPhone = "1111111111"


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


    def sendFormBeSponsorRu():

        driver.get("https://mhealthcongress.ru/ru/become-sponsor")
        driver.find_element_by_id("becomesponsor-name").send_keys("testName")
        driver.find_element_by_id("becomesponsor-last_name").send_keys("testSurname")
        driver.find_element_by_id("becomesponsor-company").send_keys("testCompany")
        driver.find_element_by_id("becomesponsor-post").send_keys("testPost")
        driver.find_element_by_id("becomesponsor-email").send_keys(myEmail)
        driver.find_element_by_id("becomesponsor-phone").send_keys(myPhone)
        driver.find_element_by_id("becomesponsor-address").send_keys("testAdress")
        driver.find_element_by_id("becomesponsor-city").send_keys("testCity")
        driver.find_element_by_id("becomesponsor-country").send_keys("testCountry")
        driver.find_element_by_id("becomesponsor-site").send_keys("https://test.ru")
        driver.find_element_by_class_name("btn-yellow").submit()
        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form BeSponsor was successful on ru version")
        else:
            print("sending wasn't successful on ru version")


    def sendFormBeSponsorEn():

        driver.get("https://mhealthcongress.ru/en/become-sponsor")
        driver.find_element_by_id("becomesponsor-name").send_keys("testName")
        driver.find_element_by_id("becomesponsor-last_name").send_keys("testSurname")
        driver.find_element_by_id("becomesponsor-company").send_keys("testCompany")
        driver.find_element_by_id("becomesponsor-post").send_keys("testPost")
        driver.find_element_by_id("becomesponsor-email").send_keys(myEmail)
        driver.find_element_by_id("becomesponsor-phone").send_keys(myPhone)
        driver.find_element_by_id("becomesponsor-address").send_keys("testAdress")
        driver.find_element_by_id("becomesponsor-city").send_keys("testCity")
        driver.find_element_by_id("becomesponsor-country").send_keys("testCountry")
        driver.find_element_by_id("becomesponsor-site").send_keys("https://test.ru")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form BeSponsor was successful on en version")
        else:
            print("sending form BeSponsor wasn't successful on en version")


    def sendFormAccreditationRu():

        driver.get("https://mhealthcongress.ru/ru/media-accreditation")
        driver.find_element_by_id("massmediaform-name").send_keys("testName")
        driver.find_element_by_id("massmediaform-fullname").send_keys("testFullname")
        driver.find_element_by_id("massmediaform-post").send_keys("testPost")
        driver.find_element_by_id("massmediaform-email").send_keys(myEmail)
        driver.find_element_by_id("massmediaform-phone").send_keys(myPhone)
        driver.find_element_by_id("massmediaform-site").send_keys("https://test.ru")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form accreditation was successful on ru version")
        else:
            print("sending form accreditation wasn't successful on ru version")


    def sendFormAccreditationEn():

        driver.get("https://mhealthcongress.ru/en/media-accreditation")
        driver.find_element_by_id("massmediaform-name").send_keys("testName")
        driver.find_element_by_id("massmediaform-fullname").send_keys("testFullname")
        driver.find_element_by_id("massmediaform-post").send_keys("testPost")
        driver.find_element_by_id("massmediaform-email").send_keys(myEmail)
        driver.find_element_by_id("massmediaform-phone").send_keys(myPhone)
        driver.find_element_by_id("massmediaform-site").send_keys("https://test.ru")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form accreditation was successful on en version")
        else:
            print("sending form accreditation wasn't successful on en version")


    def sendFormBeSpeakerRu():

        driver.get("https://mhealthcongress.ru/ru/become-speaker")
        driver.find_element_by_id("becomespeaker-name").send_keys("testName")
        driver.find_element_by_id("becomespeaker-last_name").send_keys("testSurname")
        driver.find_element_by_id("becomespeaker-email").send_keys(myEmail)
        driver.find_element_by_id("becomespeaker-phone").send_keys(myPhone)
        driver.find_element_by_id("becomespeaker-country").send_keys("testCountry")
        driver.find_element_by_id("becomespeaker-post").send_keys("testPost")
        driver.find_element_by_id("becomespeaker-company").send_keys("testCompany")
        driver.find_element_by_id("becomespeaker-themename").send_keys("testTheme")
        driver.find_element_by_id("becomespeaker-comments").send_keys("testComments")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form BeSpeaker was successful on ru version")
        else:
            print("sending form BeSpeaker wasn't successful on ru version")


    def sendFormBeSpeakerEn():

        driver.get("https://mhealthcongress.ru/en/become-speaker")
        driver.find_element_by_id("becomespeaker-name").send_keys("testName")
        driver.find_element_by_id("becomespeaker-last_name").send_keys("testSurname")
        driver.find_element_by_id("becomespeaker-email").send_keys(myEmail)
        driver.find_element_by_id("becomespeaker-phone").send_keys(myPhone)
        driver.find_element_by_id("becomespeaker-country").send_keys("testCountry")
        driver.find_element_by_id("becomespeaker-post").send_keys("testPost")
        driver.find_element_by_id("becomespeaker-company").send_keys("testCompany")
        driver.find_element_by_id("becomespeaker-themename").send_keys("testTheme")
        driver.find_element_by_id("becomespeaker-comments").send_keys("testComments")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form BeSpeaker was successful on en version")
        else:
            print("sending form BeSpeaker wasn't successful on en version")


    def sendFormBePartnerRu():

        driver.get("https://mhealthcongress.ru/ru/become-info-partner")
        driver.find_element_by_id("becomeinfopartner-name").send_keys("testFullName")
        driver.find_element_by_id("becomeinfopartner-post").send_keys("testPost")
        driver.find_element_by_id("becomeinfopartner-site").send_keys("https://test.ru")
        driver.find_element_by_id("becomeinfopartner-phone").send_keys(myPhone)
        driver.find_element_by_id("becomeinfopartner-email").send_keys(myEmail)
        driver.find_element_by_id("becomeinfopartner-comments").send_keys("testComments")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form BePartner was successful on ru version")
        else:
            print("sending form BePartner wasn't successful on ru version")


    def sendFormBePartnerEn():

        driver.get("https://mhealthcongress.ru/en/become-info-partner")
        driver.find_element_by_id("becomeinfopartner-name").send_keys("testFullName")
        driver.find_element_by_id("becomeinfopartner-post").send_keys("testPost")
        driver.find_element_by_id("becomeinfopartner-site").send_keys("https://test.ru")
        driver.find_element_by_id("becomeinfopartner-phone").send_keys(myPhone)
        driver.find_element_by_id("becomeinfopartner-email").send_keys(myEmail)
        driver.find_element_by_id("becomeinfopartner-comments").send_keys("testComments")
        driver.find_element_by_class_name("btn-yellow").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form BePartner was successful on en version")
        else:
            print("sending form BePartner wasn't successful on en version")

    def sendFormSubscribeRu():

        driver.get("https://mhealthcongress.ru/ru")
        driver.find_element_by_id("formsubscribe-name").send_keys("testName")
        driver.find_element_by_id("formsubscribe-email").send_keys(myEmail)
        driver.find_element_by_xpath("//*[@id=\"w0\"]/input[2]").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form Subscribe was successful on ru version")
        else:
            print("sending form Subscribe wasn't successful on ru version")


    def sendFormSubscribeEn():

        driver.get("https://mhealthcongress.ru/en")
        driver.find_element_by_id("formsubscribe-name").send_keys("testName")
        driver.find_element_by_id("formsubscribe-email").send_keys(myEmail)
        driver.find_element_by_xpath("//*[@id=\"w0\"]/input[2]").submit()

        if WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "mfp-close"))):
            print("sending form Subscribe was successful on en version")
        else:
            print("sending form Subscribe wasn't successful on en version")


    sendFormBeSponsorRu()
    sendFormBeSponsorEn()
    sendFormAccreditationRu()
    sendFormAccreditationEn()
    sendFormBeSpeakerRu()
    sendFormBeSpeakerEn()
    sendFormBePartnerRu()
    sendFormBePartnerEn()
    sendFormSubscribeRu()
    sendFormSubscribeEn()




