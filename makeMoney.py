import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from random import randint
from subprocess import call, Popen
import os
import getpass

class emulatorSetup():
    def turn_on_the_emulator(self):
        arg1 = " -avd Nexus_5X_API_28_x86 -netdelay none -netspeed full"
        username = getpass.getuser()
        command = "C:\\Users\\" + username + "\\AppData\\Local\\Android\\Sdk\\emulator\\emulator.exe" + arg1
        #result = call(command)  # This will block until cmd is complete
        p = Popen(command)
        sleep(10)
        print("emualtor is on")

    def start_appium(self):
        os.system("start /B start cmd.exe @cmd /k appium -a 127.0.0.1 -p 4723")
        sleep(10)
        print("appium is started")


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
                self.driver.implicitly_wait(5)
                element = self.driver.find_element_by_id("proxima.makemoney.android:id/button1")
                element.click()
            except:
                pass
            sleep(randint(3, 10))
            try:
                self.driver.implicitly_wait(5)
                element = self.driver.find_element_by_id("proxima.makemoney.android:id/okbutton")
                element.click()
            except:
                pass
            sleep(randint(3, 10))

            TouchAction(self.driver).tap(None, 450, 320, 1).perform()
            sleep(randint(3, 10))
            element = self.driver.find_element_by_id("proxima.makemoney.android:id/okbutton")
            element.click()
            try:
                sleep(randint(3, 5))
                element = self.driver.find_element_by_id("android:id/button2")
                element.click()
            except:
                sleep(randint(30, 45))
                self.driver.back()

            n += 1

        #self.driver.find_element_by_name("Single Player").click()
        #textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        #self.assertEqual('MATCH SETTINGS', textfields[0].text)


if __name__ == '__main__':
    emulatorSetup().turn_on_the_emulator()
    emulatorSetup().start_appium()
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
