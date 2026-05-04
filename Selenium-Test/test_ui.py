# Selenium UI Tests
# Focus: Frontend interaction validation

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class SeleniumUITests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def test_home_page_title(self):
        self.driver.get("http://localhost:3000")
        self.assertIn("Product Store Admin", self.driver.title)

    def tearDown(self):
        self.driver.quit()
