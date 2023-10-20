import requests
from bs4 import BeautifulSoup




def instaStats(url):
    # Specify the URL of the webpage you want to scrape
    # Replace with the URL of the target website
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all meta tags in the HTML
        meta_tags = soup.find_all('meta',{"name":"description"})
        # Extract and print the content of each meta tag
        meta_content = meta_tags[0].get('content')
        stats = meta_content.split(", ")[0:2]
        followers = int(stats[0].split(" ")[0])
        following = int(stats[1].split(" ")[0])
        return [followers,following]

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

print(instaStats("https://www.instagram.com/rhul_golf/similar_accounts/"))