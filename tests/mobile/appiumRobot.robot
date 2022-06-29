# This sample code uses the Appium robot client
# pip install robotframework-appiumlibrary
# Then you can paste this into a file and simply run with robot
#
#  more keywords on: http://serhatbolsu.github.io/robotframework-appiumlibrary/AppiumLibrary.html

*** Settings ***
Library           AppiumLibrary
Test Teardown     Quit Application

*** Variables ***
${REMOTE_URL}   http://127.0.0.1:4723/wd/hub
${platformName}    Android
${appium:automationName}    uiautomator2
${appium:deviceName}    emulator-5554
${appium:appPackage}    com.google.android.calculator
${appium:appActivity}    com.android.calculator2.Calculator
${appium:ensureWebviewsHavePages}    false
${appium:nativeWebScreenshot}    false
${appium:newCommandTimeout}    3600
${appium:connectHardwareKeyboard}    true

*** Test Cases ***
qq coisa
    Open Application    ${REMOTE_URL}   platformName=${platformName}  appium:automationName=${appium:automationName}  appium:deviceName=${appium:deviceName}  appium:appPackage=${appium:appPackage}  appium:appActivity=${appium:appActivity}  appium:ensureWebviewsHavePages=${appium:ensureWebviewsHavePages}  appium:nativeWebScreenshot=${appium:nativeWebScreenshot}  appium:newCommandTimeout=${appium:newCommandTimeout}  appium:connectHardwareKeyboard=${appium:connectHardwareKeyboard}
    # accessibility id=7
    ###
    Click Element    accessibility_id=7
    # accessibility id=multiply
    Click Element    id=com.google.android.calculator:id/op_mul
    # accessibility id=9
    Click Element    id=com.google.android.calculator:id/digit_9
    Click Element    id=com.google.android.calculator:id/digit_9
    '''
    # accessibility id=equals
    Click Element    id=com.google.android.calculator:id/eq
    # id=com.google.android.calculator:id/result_final
    element should contain text    id=com.google.android.calculator:id/result_final    693
