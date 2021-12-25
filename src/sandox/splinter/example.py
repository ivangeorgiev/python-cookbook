# from splinter import Browser

# with Browser("chrome") as browser:
#     # Visit URL
#     url = "http://www.google.com"
#     browser.visit(url)
#     browser.fill("q", "splinter - python acceptance testing for web applications")  # noqa
#     # Find and click the 'search' button
#     button = browser.find_by_name("btnG")
#     # Interact with elements
#     button.click()
#     if browser.is_text_present("splinter.readthedocs.io"):
#         print("Yes, the official website was found!")
#     else:
#         print("No, it wasn't found... We need to improve our SEO techniques")


from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser = Service(r"C:\apps\bin\webdriver\chromedriver\v96\chromedriver.exe")
op = webdriver.ChromeOptions()
browser = webdriver.Chrome(service=ser, options=op)
browser.get("http://techstepacademy.com/training-ground")
browser.quit()
