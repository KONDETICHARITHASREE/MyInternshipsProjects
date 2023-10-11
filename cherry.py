import requests
import csv
from bs4 import BeautifulSoup

# Replace 'https://example.com' with the URL of the website you want to scrape
url = 'https://example.com'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser') 
    
    # Extract data from the website (replace with your specific data)
    data_to_scrape = soup.find_all('div', class_='data-class')  # Example
    
    # Create a list to store the scraped data
    scraped_data = []
    
    for item in data_to_scrape:
        # Process the data as needed (e.g., extract text, clean, format)
        data_point = item.text.strip()  # Example
        
        # Append the data to the list
        scraped_data.append(data_point)
    
    # Save the scraped data to a CSV file
    with open('scraped_data.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Data'])  # Add appropriate column headers
        csv_writer.writerows(scraped_data)

    print('Data successfully scraped and saved to scraped_data.csv')
else:
    print('Failed to retrieve data from the website')