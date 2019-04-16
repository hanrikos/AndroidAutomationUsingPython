import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from random import randint


class AndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'emulator-5554'
        # Returns abs path relative to this file and not cwd
        #desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'D:\Programs\myapp\Chess Free.apk'))
        desired_caps['appPackage'] = 'proxima.makemoney.android'
        desired_caps['appActivity'] = '.MainActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_single_player_mode(self):
        n = 0
        while n < 20:
            sleep(randint(3, 40))
            try:
                element = self.driver.find_element_by_id("proxima.makemoney.android:id/button1")
                element.click()
            except:
                pass
            sleep(randint(3, 10))
            try:
                element = self.driver.find_element_by_id("proxima.makemoney.android:id/okbutton")
                element.click()
            except:
                pass
            sleep(randint(3, 10))

            TouchAction(self.driver).tap(None, 450, 320, 1).perform()
            sleep(randint(3, 10))
            element = self.driver.find_element_by_id("proxima.makemoney.android:id/okbutton")
            element.click()
            if self.driver.find_element_by_id("android:id/button2"):
                sleep(randint(3, 5))
                element = self.driver.find_element_by_id("android:id/button2")
                element.click()
            else:
                sleep(randint(30, 45))
                self.driver.back()

            n += 1

        #self.driver.find_element_by_name("Single Player").click()
        #textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        #self.assertEqual('MATCH SETTINGS', textfields[0].text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
