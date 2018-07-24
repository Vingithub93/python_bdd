from behave import *
from appium import webdriver
import os
from time import sleep
import unittest
#from appium import webdriver
from altunityrunner import AltrunUnityDriver
from altunityrunner import AltElement

use_step_matcher("re")

@given(u'Application should launch')
def step_impl(self):
    self.desired_caps = {}    
    self.platform='Android'
    self.desired_caps['platformName'] = 'Android'
    self.desired_caps['deviceName'] = 'device'
    self.desired_caps['newCommandTimeout'] = 90
    self.desired_caps['app'] ='D:\\byj\\bdd\\python_behave_template-master\\game.apk'    
    self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
    self.altdriver = AltrunUnityDriver(self.driver, self.platform) 


@given(u'Tap on Launch MCQ button')
def step_impl(self):
    self.altdriver.wait_for_current_scene_to_be('LaunchPad')
    sleep(10)
    self.altdriver.wait_for_element('MCQ').tap()

@then(u'It should load MCQ Scene')
def step_impl(self):
    self.altdriver.wait_for_current_scene_to_be('MCQ')
    sleep(10)

@when(u'Tap on the correct answer')
def step_impl(self):
    self.altdriver.wait_for_element('Option 1').tap()
    sleep(10)

@then(u'Pop up message should be display as Awesome and next Level question2 should load')
def step_impl(self):
    print"fist level"
    
@when(u'Tap on the correct answer2')
def step_impl(self):
    self.altdriver.wait_for_element('Option 1').tap()
    sleep(10)

@then(u'Pop up message should be display as Superb and next Level question3 should load')
def step_impl(self):
    print"second level"

@when(u'Tap on the correct answer3')
def step_impl(self):
    self.altdriver.wait_for_element('Option 2').tap()
    sleep(10)

@then(u'Pop up message should be display as Clever')
def step_impl(self):
    print "third level"
    
