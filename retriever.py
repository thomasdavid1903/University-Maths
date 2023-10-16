import requests
from bs4 import BeautifulSoup
import numpy as np

# A program used to fetch all the prime numbers off the website at the variable url

def retrieve():# Define the URL with the start and stop parameters
    url = "https://t5k.org/curios/index.php?start=12&stop=15"

    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing the numbers
        number_elements = soup.find_all(class_='mono',title="prime")  # You may need to inspect the HTML to find the correct element

        # Extract the numbers from the elements
        numbers = [element.get_text() for element in number_elements]

        # Print the list of numbers
        print(numbers)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")

    num = []
    for x in numbers:
        num.append(int(x))


    return(num)