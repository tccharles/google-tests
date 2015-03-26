#!/usr/bin/env python
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from pages.page import Page


class Base(Page):
    """
    Base class for global project specific functions
    """

    @property
    def header(self):
        return self.Header(self.testsetup)    

    @property
    def footer(self):
        """Return the common Footer region."""
        return self.Footer(self.testsetup)

    class Header(Page):

        _search_box_locator = (By.ID, 'lst-ib')
       # _profile_menu_locator = (By.CSS_SELECTOR, '#nav-main > a.dropdown-toggle')


        @property
        def is_search_box_present(self):
            return self.is_element_present(*self._search_box_locator)

        def search_for(self, search_term):
            search_field = self.selenium.find_element(*self._search_box_locator)
            search_field.send_keys(search_term)
            search_field.send_keys(Keys.RETURN)
            from pages.search import Search
            return Search(self.testsetup)

        def click_options(self):
            self.selenium.find_element(*self._profile_menu_locator).click()
            WebDriverWait(self.selenium, self.timeout).until(lambda s: self.selenium.find_element(*self._dropdown_menu_locator))

        @property
        def is_logout_menu_item_present(self):
            return self.is_element_present(*self._logout_menu_item_locator)

        # menu items
        def click_view_profile_menu_item(self):
            self.click_options()
            self.selenium.find_element(*self._view_profile_menu_item_locator).click()
            from pages.profile import Profile
            return Profile(self.testsetup)

        def click_invite_menu_item(self):
            self.click_options()
            self.selenium.find_element(*self._invite_menu_item_locator).click()
            from pages.invite import Invite
            return Invite(self.testsetup)

        def click_edit_profile_menu_item(self):
            self.click_options()
            self.selenium.find_element(*self._edit_profile_menu_item_locator).click()
            from pages.edit_profile import EditProfile
            return EditProfile(self.testsetup)

        def click_logout_menu_item(self):
            self.click_options()
            self.selenium.find_element(*self._logout_menu_item_locator).click()
            WebDriverWait(self.selenium, self.timeout).until(lambda s: not self.is_logout_menu_item_present)
        

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
