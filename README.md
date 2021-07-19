# Amazon-Web-Scraper
Amazon.com Web Scraper
Problem: Amazon has good deals, but scrolling through their website/app takes a substantial amount of time to do.
Solution: Web Scrape Amazon to obtain products and their repsective prices, prime availability, shipping cost, etc.

How To Use:
As this is my first web scraping project, I used ( https://www.youtube.com/watch?v=_AeudsbKYG8 ) as an initial frame of reference. As a result the project requires you to install BeautifulSoup (pip install bs4), Selenium (pip install selenium), and ChromeDriver (https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/) for Google Chrome.
Once this is done, download the amazonwebscraper.py in the same location as your ChromeDriver Download location and run the program. 1st enter a desired amazon search (ex. ps4 games, cleaning supplies, etc) and after hitting enter, then type in a name for your csv file as well as the number of product results you wish to process. This is linearizable for any Amazon search; there are no limits. Once this is done, the resulting .csv will be created in the same file location as the .py file. The resulting .csv will have product names, prices, shipping costs, prime availability, rating count and stars for all Amazon products within the selected page result. A future SQL script will be added to create a SQL database and copy over the .csv items.

![searchresults](searchresults.png)
