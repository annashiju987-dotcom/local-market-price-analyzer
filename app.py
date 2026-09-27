
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        product = request.form["product"]

        shop1 = request.form["shop1"]
        price1 = float(request.form["price1"])

        shop2 = request.form["shop2"]
        price2 = float(request.form["price2"])

        shop3 = request.form["shop3"]
        price3 = float(request.form["price3"])

        # Store the shop names and prices in a Pandas DataFrame
        prices = pd.DataFrame({
            "Shop": [shop1, shop2, shop3],
            "Price": [price1, price2, price3]
        })

        # Analyze the prices
        lowest = prices["Price"].min()

        cheapest_shop = prices.loc[
            prices["Price"].idxmin(), "Shop"
        ]

        average = prices["Price"].mean()
        highest = prices["Price"].max()
        saving = highest - lowest

        # Send the results to the webpage
        result = {
            "product": product,
            "shop": cheapest_shop,
            "lowest": lowest,
            "average": average,
            "saving": saving,
            "shop1": shop1,
            "shop2": shop2,
            "shop3": shop3,
            "price1": price1,
            "price2": price2,
            "price3": price3
        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True, port=5001)