class Product:
    def __init__(self, site, title, link, rating, reviews, price, img):
        self.site = site
        self.title = title
        self.link = link
        self.rating = rating
        self.reviews = reviews
        self.price = price
        self.img = img
        
    def to_dict(self):
        return {
            'site': self.site,
            'title': self.title,
            'link': self.link,
            'rating': self.rating,
            'reviews': self.reviews,
            'price': self.price,
            'img': self.img
        }
        
    def display(self):
        print(self.site)
        print(self.title)
        print(self.link)
        print(self.rating)
        print(self.reviews)
        print(self.price)
        print(self.img)