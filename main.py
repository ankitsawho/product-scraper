from utils.product import Product
from utils.scraper import amazon_scraper_1, flipkart_scraper_1, flipkart_scraper_2, amazon_scraper_1, amazon_scraper_2
import pandas as pd

product = "smartphone"

ad1 = amazon_scraper_1(product)
ad2 = amazon_scraper_2(product)
fd1 = flipkart_scraper_1(product)
fd2 = flipkart_scraper_2(product)

data = ad1 + ad2 + fd1 + fd2

record = [product.to_dict() for product in data]
df = pd.DataFrame.from_records(record)
print(df)