import os
import logging
from urllib.parse import urljoin, urlparse
import requests
import pdfkit
from bs4 import BeautifulSoup

# Set up logging to capture errors
logging.basicConfig(filename='error.log', level=logging.INFO)

# Set up wkhtmltopdf path to work with pdfkit
path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

# Determine if the URL is valid for processing
def is_valid_url(url):
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)

# Get all site links from the start page
def get_all_site_links(url):
    links = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            for link in soup.find_all('a', class_='page-link', href=True):
                full_link = urljoin(url, link['href'])
                if is_valid_url(full_link) and full_link not in links:
                    links.append(full_link)
        else:
            logging.error(f"Failed to retrieve {url}. Status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Exception occurred while retrieving {url}: {e}")
    return links

# Scrape content from the URL and create a PDF
def scrape_to_pdf(url, file_path):
    try:
        pdfkit.from_url(url, file_path, configuration=config)
        logging.info(f"Successfully created PDF for: {url}")
    except Exception as e:
        logging.error(f"Error occurred while creating PDF for {url}: {e}")

# Main execution sequence
base_url = 'https://www.tradingview.com/pine-script-docs/index.html'
output_directory = 'docs'

links = get_all_site_links(base_url)

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for link in links:
    file_name = os.path.basename(urlparse(link).path)
    if not file_name or file_name == 'index.html':
        file_name = 'index'

    file_extension = '.pdf'
    if not file_name.endswith(file_extension):
        file_name += file_extension
    file_path = os.path.join(output_directory, file_name)

    if not os.path.exists(file_path):  # Avoid duplication
        scrape_to_pdf(link, file_path)

