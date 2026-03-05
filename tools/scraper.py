import requests
from bs4 import BeautifulSoup
import markdownify

def scrape_to_md(kb_num):
    url = f"https://support.microsoft.com/help/{kb_num}"
    headers = {'User-Agent': 'EiJack-Lab-Crawler/1.0'}
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove all images and script tags before processing
        for img in soup.find_all('img'):
            img.decompose()
        for script in soup.find_all('script'):
            script.decompose()
            
        content = soup.find('div', {'id': 'main-content'})
        md = markdownify.markdownify(str(content), heading_style="ATX")
        
        with open(f"kb-data/KB{kb_num}.md", "w", encoding="utf-8") as f:
            f.write(md)

# Example: scrape_to_md("130510")
