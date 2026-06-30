import math
import os
import serpapi
import webbrowser as wb
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("SERPAPI_KEY")

class Product:
    def __init__(self, title, price, rating, review_count, source, link, extracted_price):
        self.title = title
        self.price = price
        self.rating = rating
        self.review_count = review_count
        self.source = source
        self.link = link
        self.extracted_price = extracted_price

        self.trust_score = 0.0
        self.value_score = 0.0

    def user_link(self):
        if self.link and self.link != "#":
            wb.open(self.link)
        else:
            print("No link available.")

    def __repr__(self):
        return f"{self.source} | Price: {self.price} | Trust: {self.trust_score:.2f}/5.00 | Value Rank: {self.value_score:.2f} | {self.title} \n"
    
class ProductSorter:
    @staticmethod
    def sort_price(products):
        return sorted(
            products,
            key=lambda p: p.extracted_price
        )
        
    @staticmethod
    def min_rating(products, rating):
        return [
            p for p in products
            if p.rating >= rating
        ]

    @staticmethod
    def filter_out_buyback_sites(products):
        blacklist = ["sell", "trade-in", "buyback", "recycle", "exchange value", "ubuy", "Case", "Cover", "Silicone", "Protective", "Bumper"]
        clean_list = []
        for p in products:
            text_to_check = f"{p.title} {p.source}".lower()
            is_buyback = any(word in text_to_check for word in blacklist)
            if not is_buyback:
                clean_list.append(p)        
        return clean_list

    @staticmethod
    def sort_by_trust(products):
        return sorted(products, key=lambda p: p.trust_score, reverse=True)

    @staticmethod
    def sort_by_recommendation(products):
        return sorted(products, key=lambda p: p.value_score, reverse=True)
    
class Scoring:
    @staticmethod
    def evaluate_products(products):
        valid_ratings = [p.rating for p in products if p.rating > 0]
        if not valid_ratings:
            return products 
            
        global_mean = sum(valid_ratings) / len(valid_ratings)
        m = 50 
        
        for p in products:
            v = p.review_count
            R = p.rating
            
            # bayesian trust score
            p.trust_score = ((v * R) + (m * global_mean)) / (v + m)
            
            # recomendation
            if p.extracted_price > 1.0:
                p.value_score = p.trust_score / math.log10(p.extracted_price)
            else:
                p.value_score = 0.0
                
        return products
    
class SERPAPI:
    def __init__(self):
        self.client = serpapi.Client(api_key=key)

    def google(self, query):
        results = self.client.search({
            "engine": "google_shopping",
            "q": query,
            "gl": "in"
        })
        shop = results.get("shopping_results", [])
        Products = []
        for pr in shop:
            title = pr.get("title", "Unknown")
            price = pr.get("price", "0")
            rating = pr.get("rating", 0.0)
            review_count = pr.get("reviews", 0)
            source = pr.get("source", "Unknown Source")
            link = pr.get("product_link", "#")
            extracted_price = pr.get("extracted_price", 0)

            product = Product(title, price, rating, review_count, source, link, extracted_price)
            Products.append(product)
        return Products

    def amazon(self, query):
        results = self.client.search({
            "engine": "amazon",
            "k": query,     
            "amazon_domain": "amazon.in"
        })
        amazon_items = results.get("amazon_results", [])
        products = []
        for pr in amazon_items:
            title = pr.get("title", "Unknown")            
            price_data = pr.get("price", {})
            price = price_data.get("raw", "₹0")
            extracted_price = price_data.get("value", 0.0)    
            rating = pr.get("rating", 0.0)
            review_count = pr.get("reviews", 0)
            source = "Amazon.in"
            link = pr.get("link", "#")

            products.append(Product(title, price, rating, review_count, source, link, extracted_price))
        return products
