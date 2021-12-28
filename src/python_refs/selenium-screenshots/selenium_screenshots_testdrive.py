# %%
import contextlib
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By  # noqa

SCREENSHOTS_DIR = Path(__file__).resolve().parent / ".dev"

# %%
URL = "https://igeorgiev.eu/"
with contextlib.closing(webdriver.Chrome()) as driver:
    driver.get(URL)
    driver.save_screenshot(str(SCREENSHOTS_DIR / "igeorgiev-home.png"))


# %%
URL = "https://igeorgiev.eu/"
with contextlib.closing(webdriver.Chrome()) as driver:
    driver.get(URL)
    logo = driver.find_element(By.CSS_SELECTOR, ".md-content")
    logo.screenshot(str(SCREENSHOTS_DIR / "igeorgiev-content.png"))
