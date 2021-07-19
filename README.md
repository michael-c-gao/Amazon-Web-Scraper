# Amazon-Web-Scraper

Problem: Amazon has good deals, but scrolling through their website/app takes a substantial amount of time to do.
Solution: Web Scrape Amazon to obtain products and their respective prices, prime availability, shipping cost, etc.

How To Use:
As this is my first web scraping project, I used ( https://www.youtube.com/watch?v=_AeudsbKYG8 ) as a frame of reference. As a result the project requires you to install BeautifulSoup (pip install bs4), Selenium (pip install selenium), and ChromeDriver (https://chromedriver.storage.googleapis.com/index.html?path=91.0.4472.101/) for Google Chrome.
Once this is done, download the amazonwebscraper.py in the same location as your ChromeDriver Download location and run the program. 1st enter a desired Amazon search (ex. ps4 games, cleaning supplies, etc), then a name for your csv file as well as the number of product result pages you wish to process. Once this is done, the resulting .csv will be created in the same file location as the .py file and will be populated with the product names, prices, shipping costs, prime availability, rating count and stars for all Amazon products within the search. A SQL script is included to create a database and a table to store and manipulate the product data ater it is imported into MySQL Workbench.

Example .csv ouputs can be found at psfourproducts.csv (search word = ps4 video games) and tss.csv (search word = transformers studio series).

![searchresults](searchresults.png)
