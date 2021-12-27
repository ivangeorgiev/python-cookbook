import pytest
from pytest_bdd import given, parsers, scenario, then, when
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DUCKDUCKGO_HOME_URL = "https://www.duckduckgo.com"
SEARCH_INPUT_HOME = (By.ID, "search_form_input_homepage")
SEARCH_INPUT = (By.ID, "search_form_input")
RESULT_LINKS = (By.CSS_SELECTOR, "a.result__a")
SEARCH_PHRASE = "panda"


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@scenario("duckduckgo_search.feature", "Basic DuckDuckGo Search")
def test_duckduckgo_basic_search(browser):
    pass


@given("the DuckDuckGo Homepage is displayed")
def duckduckgo_homepage(browser):
    browser.get(DUCKDUCKGO_HOME_URL)
    return browser


@when(parsers.parse('the user searches for "{query}"'))
def search_for_query(browser, query):
    search_input = browser.find_element(*SEARCH_INPUT_HOME)
    search_input.send_keys(query + Keys.RETURN)


@then(parsers.parse('the search result title contains "{text}"'))
def assert_text_in_title(browser: WebDriver, text):
    assert text in browser.title


@then(parsers.parse('the search result query is "{query}"'))
def assert_search_result_query(browser: WebDriver, query):
    assert query == browser.find_element(*SEARCH_INPUT).get_attribute("value")


@then(parsers.parse('the search result links pertain to "{query}"'))
def assert_search_result_links_pertain_to_query(browser, query):
    links = browser.find_elements(*RESULT_LINKS)
    link_texts = [link.text for link in links]
    matches = [t for t in link_texts if query.lower() in t.lower()]
    assert len(matches) > 0
