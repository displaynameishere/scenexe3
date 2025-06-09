# scenexe3 bot
# made by displaynameis here
import undetected_chromedriver as uc
from time import sleep

HEADLESS = True
PAGE_LOAD_WAIT = 5
TEMP_SCREENSHOTS_DIR = "~/.scenexe3/temp_frames"

driver = uc.Chrome(headless=HEADLESS)
driver.get("https://scenexe2.io")
sleep(PAGE_LOAD_WAIT)
driver.save_screenshot("test.png")
driver.quit()
