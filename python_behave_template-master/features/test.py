'''
Created on 21-Jul-2018

@author: admin
'''
import unittest

@CucumberOptions(
        
        features= "D:\\byj\\bdd\\python_behave_template-master\\features",
        glue= {"first_behave"},
        tags= {"@MCQ_Varient"},
        monochrome= true,
        plugin={"html:target/cucumber-html-report","json:target/cucumber.json", "pretty:target/cucumber-pretty.txt", "usage:target/cucumber-usage.json","junit:target/cucumber-results.xml"}
                
        )

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()