from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import re
#reference: https://www.youtube.com/watch?v=_AeudsbKYG8

def get_url(search_term):
    
    website = 'https://www.amazon.com/s?k={}&ref=nb_sb_noss'
    search_term = search_term.replace(' ', '+')
    url = website.format(search_term)
    url += '&page{}'
    return url


def extract_product(item):
    
    totalCost = None
    shipping = None
    shippingCost = 0
    primeAvailability = 'Y'
    atag = item.h2.a
    url = 'https://amazon.com' + atag.get('href')

    product = atag.text.rstrip()

    prime = item.find('span','aok-relative s-icon-text-medium s-prime')
    if prime == None:
        primeAvailability = 'N'
        try:
            shipping = item.find('div','a-row a-size-base a-color-secondary s-align-children-center').text
            numbers = re.findall('[0-9]+', shipping)

            if (len(numbers) > 1):
                shippingArray = '.'.join(numbers)
                shippingCost = float(shippingArray)
            
        except AttributeError:
            shipping = None
        
    try:
        rating = item.find('div', 'a-row a-size-small').text
        rate = float(rating[0:3])
        numRates = rating[19:-1].rstrip()
        
        if(len(numRates) > 3):
            numRates = numRates.replace(',','')
        numRates = int(numRates)
        
    except AttributeError:
        rate = None
        numRates = None
    
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span','a-offscreen').text
        price = float(price.replace('$',''))
       
    except AttributeError:
        price = None
        shippingCost = None

    if(price != None):
        totalCost = price + shippingCost

    result = (product, url, rate,numRates, primeAvailability, price, shipping, totalCost)
    
    return result


def main(search_term, numPages, filename):
    itemCtr = 0
    driver = webdriver.Chrome() 
    url = get_url(search_term)
    
    items = []
    for pages in range(numPages):
        driver.get(url.format(pages))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        page = soup.find_all('div',{'data-component-type': 's-search-result'})
       
        for product in page:
            itemCtr += 1
            print("________Processing item #" + str(itemCtr) + "___________")
            item = extract_product(product)
            #print(item)
            if item:
                items.append(item)
    driver.close()
    filename += '.csv'
    with open(filename, 'w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Product','Link','Stars','Reviews', 'Prime Availability','Price', 'Shipping', 'Total Cost'])
        writer.writerows(items)



if __name__ == '__main__':
    
    keyword = input('Enter a amazon search keyword: ')

    while(True):

        try:
            filename = str(input('Enter a name for your .csv file: '))
            if(not filename.isalpha() and not filename.isdigit()):
                print("Please enter letters and numbers only.")
                continue
            
        except NameError:
            print("?")
            continue

        try:
            numPages = int(input('Enter a positive page number to search to: '))
            if(numPages <= 0):
                print('Please enter a number > 0')
                continue
            
            break

        except ValueError:
            print('Please enter a integer.')
            continue

        
        
    print("____________Working...________________")
    main(keyword, numPages, filename)
    print("___________Done. " + filename + ".csv ready for viewing________")
