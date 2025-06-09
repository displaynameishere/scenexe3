import undetected_chromedriver as uc

driver = uc.Chrome()
driver.get("https://scenexe2.io")
driver.save_screenshot("test.png")
driver.quit()
