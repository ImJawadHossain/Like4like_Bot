from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import os
import pyautogui

uss = 'priyaakterpayel'
ine = os.environ.get('ine')
pw = os.environ.get('password')

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")


driver.get('https://www.like4like.org/login/')
driver.find_element_by_id('username').send_keys(uss)
driver.find_element_by_id('password').send_keys(pw)
input('w :')
driver.find_element_by_xpath("//a[text()='Submit']").click()
driver.set_page_load_timeout(10)
time.sleep(3)
driver.get('https://www.like4like.org/free-instagram-followers-likes-and-comments-exchange.php')
window_before = driver.window_handles[0]




def first_follow(tr,td):
        xpath = ('/html/body/div[6]/div[2]/div[2]/div[1]/div/div/table/tbody/tr['+str(tr)+']/td['+str(td)+']/div/div[2]/div/span/a')   #1st click
        driver.find_element_by_xpath(xpath).click()



def insta_follow():
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    try:
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
    except:
        pass

    try:
        driver.find_element_by_xpath(
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button')).click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
    except:
        pass

    try:
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[1]').click() #un follow
    except:
        pass


def confirm(tr,td):
    pyautogui.hotkey('Ctrl', 'w')
    time.sleep(1.5)
    driver.switch_to.window(window_before)
    driver.find_element_by_xpath('/html/body/div[6]/div[2]/div[2]/div[1]/div/div/table/tbody/tr['+str(tr)+']/td['+str(td)+']/div/a/img').click()

class RunProject:
    while True:
            try:

                cond = 1
                while cond < 7:
                    time.sleep(5)
                    first_follow(3,cond)

                    time.sleep(6)
                    insta_follow()

                    time.sleep(1)
                    confirm(3,cond)
                    time.sleep(2)
                    cond +=1
            except:
                pyautogui.hotkey('Ctrl', 'r')

            try:
                cond = 1
                while cond < 7:
                    time.sleep(5)
                    first_follow(3, cond)
                    driver.set_page_load_timeout(10)
                    time.sleep(1)
                    insta_follow()

                    time.sleep(1)
                    confirm(3, cond)
                    cond += 1
            except:
                pass

            try:
                time.sleep(5)
                first_follow(4,5)
                time.sleep(6)
                insta_follow()
                time.sleep(1)
                confirm(4,5)
            except:
                pyautogui.hotkey('Ctrl', 'r')

            try:
                time.sleep(5)
                first_follow(4,5)
                time.sleep(6)
                insta_follow()
                time.sleep(1)
                confirm(4,5)
            except:
                pass

            try:
                cond = 6
                while cond > 0:
                    time.sleep(5)
                    first_follow(5,cond)
                    driver.set_page_load_timeout(10)
                    time.sleep(1)
                    insta_follow()
                    time.sleep(2)
                    confirm(5,cond)
                    time.sleep(2)
                    cond -=1

            except:
                pass

            pyautogui.hotkey('ctrl','r')
while True:
    try:
        RunProject()

    except:
        pass

    RunProject()


