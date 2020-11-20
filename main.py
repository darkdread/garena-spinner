import os
import time
from appium import webdriver

desired_caps = dict(
    platformName="Android",
    platformVersion="10",
    automationName="uiautomator2",
    deviceName="Android Emulator",
    app=os.path.dirname("Garena_base.apk"),
    appActivity="com.garena.gxx.splash.GGSplashActivity",
    appPackage="com.garena.gaslite"
)


class GarenaAutomator():

    def __init__(self):
        self.driver: WebDriver = webdriver.Remote(
            'http://localhost:4723/wd/hub', desired_caps)
        time.sleep(5)
        pass

    def login(self, login, pw):
        el1 = self.driver.find_element_by_id(
            "com.garena.gaslite:id/et_identity")
        el1.click()
        el1.send_keys(login)
        el2 = self.driver.find_element_by_id(
            "com.garena.gaslite:id/et_password")
        el2.click()
        el2.send_keys(pw)
        el3 = self.driver.find_element_by_id(
            "com.garena.gaslite:id/tv_btn_login")
        el3.click()

    def spin(self):
        el6 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout[2]/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.c[2]/android.widget.LinearLayout/android.widget.TextView")
        el6.click()
        el7 = self.driver.find_element_by_id(
            "com.garena.gaslite:id/layout_wheelview")
        el7.click()
        el8 = self.driver.find_element_by_id("com.garena.gaslite:id/btn_ok")
        el8.click()


automator = GarenaAutomator()
automator.login("", "")
automator.spin()
