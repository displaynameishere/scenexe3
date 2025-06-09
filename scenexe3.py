# scenexe3 bot
# made by displaynameis here
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

HEADLESS = False
FIRST_LOAD_WAIT = 6
PAGE_LOAD_WAIT = 5
PLAYER_NAME = "displaynameisbot"

def send_chat(msg):
    chat = driver.find_element(By.ID, "chat")
    chat.click()
    chat.send_keys(msg)
    chat.send_keys(Keys.RETURN)

driver = uc.Chrome(headless=HEADLESS)

driver.execute_cdp_cmd("Network.enable", {})
driver.execute_cdp_cmd("Network.setBlockedURLs", {
    "urls": ["*://*.doubleclick.net/*", "*://*.googlesyndication.com/*", "*://*.adsafeprotected.com/*", "*://*.adinplay.com/*"]
})
driver.execute_cdp_cmd("Network.enable", {})

driver.get("https://scenexe2.io")

sleep(FIRST_LOAD_WAIT)

adContinue = driver.find_element(By.ID, "adblockContinue")
adContinue.click()

sleep(1)

nameInput = driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div[10]/input")
nameInput.click()
nameInput.send_keys(PLAYER_NAME)

playButton = driver.find_element(By.ID, "playButton")
playButton.click()

sleep(PAGE_LOAD_WAIT)

send_chat("hello world")
sleep(1)

driver.save_screenshot(f"test.png")
driver.quit()