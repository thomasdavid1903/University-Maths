## This is just a collection of mathematical operations turned into functions so I can import them into other programs
#factorial
#integration
#fibonacci
#statistics - mean, median, variance
# Show the central limit theorem
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Initialize the driver
driver = webdriver.Chrome()  # You can use other drivers like Firefox, Edge, etc.

# Navigate to the website
driver.get("https://www.instagram.com/manlikedavetrains/?hl=om-et")

# Find an element by its CSS selector (you can also use other locators)
element = driver.find_element_by_css_selector("#some-element")

# Perform a "click" action on the element
element.click()

# Close the browser
driver.quit()