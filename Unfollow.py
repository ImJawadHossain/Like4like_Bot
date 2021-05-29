import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pathlib
from selenium.webdriver.common.keys import Keys

liFollowXpath = "//tbody//div[1]//span[1]//a[1]"
inFollowXpath = "//button[normalize-space()='Follow']"
inUnfollowXpath = "//span[@aria-label='Following']"
confirm = "img[title='Click On The Button To Confirm Interaction!']"

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


print(input(""))
def unfollow():
    #driver.get("https://instagram.com/tishaktermim")
    driver.get("https://instagram.com/priyaakterpayel")
    #driver.find_element_by_xpath("//a[@href='/tishaktermim/following/']").click()
    driver.find_element_by_xpath("//a[@href='/priyaakterpayel/following/']").click()
    time.sleep(2)
    a = 1
    while True:

        driver.find_element_by_xpath("//li["+str(a)+"]//div[1]//div[3]//button[1]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath("//div[@class='piCib']//button[1]").click()
        time.sleep(2)
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.END)
        a += 1

while True:
    try:
        unfollow()
    except:
        pass
