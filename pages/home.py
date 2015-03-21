#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import time
import datetime

from selenium.webdriver.common.by import By

from base import Base
from page import PageRegion


class HomePage(Base):
    """This Page Object models the Google Home Page (https://www.google.com/)."""

    # The title of this page, which is used by is_the_current_page() in page.py
    _page_title = u'Google'

    # Locators for the home page
    # Put locators here located on the home page, like the search bar, search button, or profile button

    def go_to_page(self):
        """Open the home page."""
        self.open('/')
