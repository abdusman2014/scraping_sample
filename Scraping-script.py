import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
response = requests.get('https://en-pk.svestonwatches.com/collections/mens-wrist-watches')

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

specific_div = soup.find('div',class_='collection-grid__wrapper')
if specific_div:
    products = specific_div.find_all('div', class_='grid__item')
    if products:
        data = []
        headings = ["Product Name","Product Line","Image Source", "Rating","Original Price","OFF","Price"]
        data.append(headings)
        for product in products:
            child_element = product.find('div',class_='grid-product__content text-center')

            if child_element:
                product_name = child_element.find('p',class_='product__title')
                product_image = child_element.find('span',class_='quick-product__label')
                img_tag = product_image.find('img')
                img_src = img_tag.get('src')
                product_line = child_element.find('p',class_='grid__metafield')
                product_rating = child_element.find('div',class_='loox-rating')
                product_price = child_element.find('div',class_='grid__price')
                product_sale_percentage = child_element.find('span',class_='grid__saleOff')
                product_original_price = child_element.find('span',class_='grid-product__price--original')
                rating_value = product_rating.get('data-rating')
                
                if product_name:
                    print('Extracting Product: ', product_name.text)
                    prod = [product_name.text,product_line.text,img_src,rating_value,product_original_price.text,product_sale_percentage.text,product_price.text]
                    data.append(prod)
                else:
                    print('Name not found')
            else:
                print('Product was not found')
        # Open (or create) a CSV file in write mode
        with open('output.csv', mode='w', newline='') as file:
            writer = csv.writer(file)

            # Write each row to the CSV file
            writer.writerows(data)
        print("Data saved to output.csv")




