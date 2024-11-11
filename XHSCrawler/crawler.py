# crawler.py
import requests
from bs4 import BeautifulSoup

def crawl_data(url):
    """Scrape data from the specified URL and return parsed results."""
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Parse title
        detail_title = soup.find('div', id='detail-title')
        title_text = detail_title.text.strip() if detail_title else "No Title Found"
        
        # Parse description
        detail_desc = soup.find('div', id='detail-desc')
        desc_text = detail_desc.text.strip() if detail_desc else "No Description Found"
        
        # Parse images
        og_images = soup.find_all('meta', attrs={'name': 'og:image'})
        image_urls = [img.get('content') for img in og_images if img.get('content')]
        
        return title_text, desc_text, image_urls
    else:
        raise ValueError(f"Failed to retrieve data. Status code: {response.status_code}")
