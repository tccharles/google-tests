#!/usr/bin/env python

from random import randrange

import pytest
from unittestzero import Assert
import requests

from pages.home_page import Home
from pages.profile import Profile


class TestSearch:

	#@pytest.mark.nondestructive
	 @pytest.mark.xfail("config.getvalue('base_url') == 'https://www.google.com'")
		def test_that_search_returns_relevant_results(self, Google):
			query = u'Boulder'
			home_page = Home(Google)
			search_page = home_page.header.search_for(query)
			Assert.true(search_page.results_count > 0)

			element_search = browser.find_element_by_id('lst-ib') # id of search field
			#element_search.send_keys('Boulder') # input 'Boulder' into search field
			search_term = 'Boulder'
			element_search.send_keys(search_term)
			element_search.send_keys(Keys.RETURN) # hits return after you enter search text
		
			browser.close()