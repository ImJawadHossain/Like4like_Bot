import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pathlib

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


print(input("login instagram and like4like:"))
driver.get("https://www.like4like.org/free-instagram-followers-likes-and-comments-exchange.php")
def instagramFollow():
    driver.implicitly_wait(10)
    time.sleep(3.5)
    if driver.find_elements_by_xpath(liFollowXpath):
        print("like4like follow button found")
        driver.find_element_by_xpath(liFollowXpath).click()
    else:
        print("like4like follow xpath not found")
        driver.refresh()
        return

    driver.switch_to.window(driver.window_handles[1])

    driver.implicitly_wait(7)
    if driver.find_elements_by_xpath(inFollowXpath):
        print("instagram follow button found")
        time.sleep(2)
        driver.find_element_by_xpath(inFollowXpath).click()

    elif driver.find_elements_by_xpath(inUnfollowXpath):
        print("instagram unfollow button found")
        driver.find_element_by_xpath(inUnfollowXpath).click()
        time.sleep(1)
        driver.find_element_by_xpath("//button[normalize-space()='Unfollow']").click()

    else:
        print("Instagram follow/unfollow button not found")
    time.sleep(2)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.implicitly_wait(7)
    time.sleep(2)
    driver.find_element_by_css_selector(confirm).click()
    time.sleep(1)

while True:
    try:
        instagramFollow()
    except:
        pass
