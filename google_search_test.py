#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestWebsite:

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.implicitly_wait(10)
        self.browser.get("https://www.google.com/")

        yield

        self.browser.close()
        self.browser.quit()

    def test_search(self):
        search = "Selenium is fun"
        search_bar = self.browser.find_element(By.XPATH, "//textarea[@name='q']")
        search_bar.send_keys(search + Keys.ENTER)
        assert self.browser.title.__contains__(search), f"Title does not contains {search}"
