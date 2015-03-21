#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from pages.page import Page


class Base(Page):
    """
    Base class for global project specific functions
    """

    @property
    def footer(self):
        """Return the common Footer region."""
        return self.Footer(self.testsetup)

    class Footer(Page):
        """The common Footer region that is present on every page."""

        copyright_links_list = [
            {
                'locator': (By.LINK_TEXT, 'Privacy'),
                'url_suffix': '//www.google.com/intl/en/policies/privacy/?fg=1',
            }, {
                'locator': (By.LINK_TEXT, 'Terms'),
                'url_suffix': '//www.google.com/intl/en/terms/privacy/?fg=1'
            }
        ]
