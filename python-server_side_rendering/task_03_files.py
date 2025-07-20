#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv


app = Flask(__name__)


def json_conv():
    try:
        with open('products.json', 'r', encoding='itf-8') as f:
            data = json.load(f)
            products_list = data.get('products', [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        products_list = []

    return render_template('product_display.html', products=products_list)


def csv_conv():
    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product = {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                }
                products.append(product)
    except Exception:
        return []
    return products


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = json_conv()
    elif source == 'csv':
        data = csv_conv()
    else:
        return render_template('product_dispay.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html',
                                   error="Invalid I format")
        for product in data:
            if product.get("id") == product_id:
                return render_template('product_display.html',
                                       products=[product])
        return render_template('product_display.html',
                               error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
