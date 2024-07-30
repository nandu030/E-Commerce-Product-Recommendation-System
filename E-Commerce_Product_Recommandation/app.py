from flask import Flask, request, render_template
import pandas as pd
import random
from flask_sqlalchemy import SQLAlchemy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

trending_products = pd.read_csv("models/trending_products.csv")
train_data = pd.read_csv("models/clean_data.csv")

def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text


random_image_urls = [
    "static/img/img_1.png",
    "static/img/img_2.png",
    "static/img/img_3.png",
    "static/img/img_4.png",
    "static/img/img_5.png",
    "static/img/img_6.png",
    "static/img/img_7.png",
    "static/img/img_8.png",
]

def index():
    # Create a list of random image URLs for each product
    random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
    price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
    return render_template('index.html',trending_products=trending_products.head(8),truncate = truncate(),
                           random_product_image_urls=random_product_image_urls,
                           random_price = random.choice(price))

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/index")
def index_redirect():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)