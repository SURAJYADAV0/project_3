import pandas as pd
import requests
from tabulate import tabulate

# Function to scrape BBC Africa news
def scrape_bbc_africa_news():
    base_url = "https://web-cdn.api.bbci.co.uk/xd/content-collection/f7905f4a-3031-4e07-ac0c-ad31eeb6a08e?country=ke&page={}"
    news_data = []
    
    for page in range(10):  # Iterate over 10 pages
        url = base_url.format(page)
        try:
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                news_items = data.get('data', [])

                for item in news_items:
                    title = item.get('title', '')
                    date = item.get('firstPublishedAt', '')
                    link = f"https://www.bbc.com{item.get('path', '')}"
                    
                    # Append data to list
                    news_data.append([date, title, link])

            else:
                print(f"Failed to fetch BBC Africa news for page {page}. Status code: {response.status_code}")

        except requests.RequestException as e:
            print(f"Error fetching BBC Africa news for page {page}: {e}")
    
    # Create DataFrame
    df = pd.DataFrame(news_data, columns=['Date', 'Title', 'Link'])

    # Display data in tabular format
    print(tabulate(df, headers='keys', tablefmt='psql'))

    # Save DataFrame to CSV file
    filename = "africa_news.csv"
    df.to_csv(filename, index=False)
    print(f"Data saved to '{filename}'")

# Execute scraping function
scrape_bbc_africa_news()
