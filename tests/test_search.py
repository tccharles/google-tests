#!/usr/bin/env python

from random import randrange

import pytest
from unittestzero import Assert
import requests

from pages.home_page import Home
from pages.profile import Profile

class TestSearch:

    @pytest.mark.credentials
    @pytest.mark.nondestructive
    @pytest.mark.xfail("config.getvalue('base_url') == 'https://www.google.com'")
    def test_that_search_returns_relevant_results(self, Google):
	    #query = u'Boulder'
	    home_page = Home(Google)
	    #search_page = home_page.header.search_for(query)
	    search_page = home_page.header.search_for(u'Boulder')
	    Assert.true(search_page.results_count > 0)
