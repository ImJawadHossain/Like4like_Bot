import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pathlib

liSubscribeXpath = "//tbody//div[1]//span[1]//a[1]"
subscribeXpath = "//yt-formatted-string[@class='style-scope ytd-subscribe-button-renderer']"


unSubscribeXpath = "//yt-formatted-string[normalize-space()='Subscribed']"


chrome_options = Options()
scriptDirectory = pathlib.Path().absolute()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--user-data-dir=chrome-data")
chrome_options.add_argument('--profile-directory=Default')
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument('disable-infobars')
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_argument("user-data-dir=chrome-data")
chrome_options.add_argument(f"user-data-dir={scriptDirectory}\\userdata")
driver = webdriver.Chrome("./chromedriver.exe", chrome_options=chrome_options)

driver.get("https://www.like4like.org/login/")
print(input("login instagram and like4like:"))
driver.get("https://www.like4like.org/user/earn-youtube-subscribe.php")
def youtubeSubscribe():
    driver.implicitly_wait(10)
    time.sleep(3.5)
    if driver.find_elements_by_xpath(liSubscribeXpath):
        print("like4like Subscribe button found")
        driver.find_element_by_xpath(liSubscribeXpath).click()
    else:
        print("like4like Subscribe xpath not found")
        driver.refresh()
        return

    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(7)
    if driver.find_elements_by_xpath(subscribeXpath):
        print("Youtube subscribe button found")
        time.sleep(2)
        driver.find_element_by_xpath(subscribeXpath).click()

    elif driver.find_elements_by_xpath(unSubscribeXpath):
        print("Youtube un subscribe button found")
        driver.find_element_by_xpath(unSubscribeXpath).click()
        time.sleep(1)
        driver.find_element_by_xpath("//yt-button-renderer[@id='confirm-button']//yt-formatted-string[@id='text']").click()





    else:
        print("YouTube Subscribe UnSubscribe button not found")
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(7)
    time.sleep(2)


coun = 1
while True:
    try:
        youtubeSubscribe()
        print("times run ============================= ", coun)
        coun += 1
    except:
        pass
