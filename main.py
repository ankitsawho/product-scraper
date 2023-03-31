from utils.scraper import amazon_scraper_1, flipkart_scraper_1, flipkart_scraper_2, amazon_scraper_1, amazon_scraper_2, amazon_details, flipkart_details
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/list', methods=['GET'])
def product_list():
    product = request.args.get('product')
    ad1 = amazon_scraper_1(product)
    ad2 = amazon_scraper_2(product)
    fd1 = flipkart_scraper_1(product)
    fd2 = flipkart_scraper_2(product)
    data = ad1 + ad2 + fd1 + fd2
    record = [product.to_dict() for product in data]
    return jsonify({'data' : record})

@app.route('/details', methods=['GET'])
def product_details():
    site = request.json['site']
    link = request.json['link']
    if site == 'amazon':
        data = amazon_details(link)
    else:
        data = flipkart_details(link)
    return jsonify({'data' : data})

if __name__ == '__main__':
    app.run(debug=True)