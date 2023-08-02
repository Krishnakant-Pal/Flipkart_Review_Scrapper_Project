# Flipkart Review Scraper
It is a flask based web application that will scrap all the review of the product from the flipkart when provided with product review link.
It will store name,rating,title & review data in the csv file with

## Features
* Scrapes user reviews for a given product review url from Flipkart.
* Retrieves name,rating,title and review.
* Supports fetching of  multiple pages of reviews.
## Getting Started
1. Clone the repository to your local machine.
2. Install the required Python packages by running: pip install -r requirements.txt.
3. Run the app.py script to start the scraping process.
4. Provide the Flipkart product review URL for which you want to fetch reviews.
   The scraper will save the review data in a CSV file named productname_reviews.csv in the same directory.

## Usage
1. Paste the review url in the search box and hit submit.
2. The scraper will visit the product page, extract review data, and store it in a CSV file which can be accessed in review folder.

## Example Output
The CSV file productname_reviews.csv will contain the following columns:
* Name
* Rating
* Title
* Review

## Technologies Used
* Python'
* Flask
* BeautifulSoup (for web scraping)
* HTML, CSS (for the user interface)
