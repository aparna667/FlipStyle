import requests
from bs4 import BeautifulSoup

def scrape_pinterest_tags(search_query):
    url = f"https://www.pinterest.com/search/pins/?q={search_query}"
    response = requests.get(url)
    print(response)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html5lib')
        # print(soup)
        tag_elements = soup.find_all('div', class_='Yl- MIw Hb7')
        print(tag_elements)
        
        tags = []
        for tag_element in tag_elements:
            tag = tag_element.get_text()
            tags.append(tag)
        
        return tags
    else:
        print("Failed to retrieve the page.")
        return None

search_query = "fashion"
tags = scrape_pinterest_tags(search_query)

if tags:
    print("Tags:")
    for tag in tags:
        print(tag)

