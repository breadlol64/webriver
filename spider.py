import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# Initialize the list of seed URLs to crawl
with open("seed.txt") as seeds:
    seed_urls = seeds.readlines()

with open("found_links.txt", 'a') as f:
    for url in seed_urls:
        f.write(url)
to_crawl = seed_urls.copy()
crawled = set()

# Function to crawl a URL
def crawl(url):
    global to_crawl, crawled

    try:
        # Send an HTTP GET request
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.text, "html.parser")

            # Process the page here (e.g., extract data, store information)

            # Find all the links on the page
            links = soup.find_all("a", href=True)
            for link in links:
                new_url = urljoin(url, link['href'])  # Convert relative URLs to absolute URLs

                # Ensure new_url is within the same domain as the seed_urls
                if any(urlparse(new_url).netloc == urlparse(seed_url).netloc for seed_url in seed_urls) and new_url not in crawled and new_url not in to_crawl:
                    print("Found link:", new_url)
                    with open("found_links.txt", "a") as f:
                        f.write(new_url + "\n")
                    to_crawl.append(new_url)

    except Exception as e:
        print(f"Error crawling {url}: {e}")

# Main crawling loop
def main():
    global to_crawl, crawled

    while to_crawl:
        url = to_crawl.pop(0)  # Get the next URL to crawl
        crawled.add(url)       # Add URL to crawled set
        crawl(url)

    print("Crawling completed. Found links saved to 'found_links.txt'.")

if __name__ == "__main__":
    main()
