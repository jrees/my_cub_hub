from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_visit_account_section_prompts_login(self):
        self.browser.get('http://localhost:8000/account')
        self.assertIn('Log-in', self.browser.title)
        self.fail('finished the test')

        # test creating new user

if __name__ == 'main':
    unittest.main(warnings='ignore')
