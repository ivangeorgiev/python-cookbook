# %%
"""To use Selenium, we need to download and install a webdriver."""
from selenium import webdriver
from webdrivermanager import ChromeDriverManager

ChromeDriverManager().download_and_install()


# %%


from selenium.webdriver.common.by import By  # noqa
from selenium.webdriver.common.keys import Keys  # noqa

DUCKDUCKGO_HOME_URL = "https://www.duckduckgo.com"
SEARCH_INPUT_HOME = (By.ID, "search_form_input_homepage")
SEARCH_INPUT = (By.ID, "search_form_input")
RESULT_LINKS = (By.CSS_SELECTOR, "a.result__a")
SEARCH_PHRASE = "panda"

browser = webdriver.Chrome()

try:
    # Browser calls should wait up to 10 seconds for elements to appear
    browser.implicitly_wait(10)

    # Given the DuckDuckGo Homepage is displayed
    browser.get(DUCKDUCKGO_HOME_URL)
    # When the user searches for "panda"
    search_input = browser.find_element(*SEARCH_INPUT_HOME)
    search_input.send_keys(SEARCH_PHRASE + Keys.RETURN)
    # Then the search result title contains "panda"
    assert SEARCH_PHRASE in browser.title
    # And the search result query is "panda"
    input_element = browser.find_element(*SEARCH_INPUT)
    assert SEARCH_PHRASE == input_element.get_attribute("value")
    # And the search result links pertain to "panda"
    links = browser.find_elements(*RESULT_LINKS)
    link_texts = [link.text for link in links]
    matches = [t for t in link_texts if SEARCH_PHRASE.lower() in t.lower()]
    assert len(matches) > 0
finally:
    browser.quit()
