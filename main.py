from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
SIMILAR_ACCOUNT = "liverpoolfc"
USERNAME = "USERNAME"
PASSWORD = "PASSWORD"


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        sleep(2)
        username = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(PASSWORD)
        login_button = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_button.click()

        sleep(5)
        # If the save login info pop up appears
        save_login_info = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        save_login_info.click()

        sleep(1)
        # If the turn on notifications popup appears
        no_notifications = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Not Now')]")
        no_notifications.click()

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")

        sleep(2)
        # Check the page's followers
        followers_button = self.driver.find_element(By.XPATH, value="//a[contains(@href, '/followers/')]")
        followers_button.click()

        sleep(5)
        # Find the scrollable div within the popup
        # scrollable_div_xpath = ("//div[@class='xyi19xy x1ccrb07 xtf3nb5 x1pc53ja x1lliihq x1iyjqo2 xs83m0k xz65tgg "
        #                         "x1rife3k x1n2onr6']")
        # scrollable_div = self.driver.find_element(By.XPATH, value=scrollable_div_xpath)
        #
        # # Scroll down in the popup
        # for i in range(5):  # Adjust the range for more or less scrolling
        #     self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_div)
        #     sleep(2)  # Adjust sleep time as needed to let new followers load

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="button._acan._acap._acas._aj1-._ap30")
        # if not follow_buttons:
        #     print("No follow buttons found.")
        #     return
        #
        # print(f"Found {len(follow_buttons)} follow buttons.")
        for follow_button in follow_buttons:
            follow_button.click()
            sleep(1.1)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
