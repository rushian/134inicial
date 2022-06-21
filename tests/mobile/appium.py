# This sample code uses the Appium python client v2
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# For W3C actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

caps = {}
caps["platformName"] = "Android"
caps["appium:automationName"] = "uiautomator2"
caps["appium:deviceName"] = "emulator-5554"
caps["appium:appPackage"] = "com.google.android.calculator"
caps["appium:appActivity"] = "com.android.calculator2.Calculator"
caps["appium:ensureWebviewsHavePages"] = True
caps["appium:nativeWebScreenshot"] = True
caps["appium:newCommandTimeout"] = 3600
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="7")
el1.click()
el2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="plus")
el2.click()
el3 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="5")
el3.click()
el4 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="equals")
el4.click()
el5 = driver.find_element(by=AppiumBy.ID, value="com.google.android.calculator:id/result_final")
el5.click()

driver.quit()