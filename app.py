from flask import Flask, render_template, request
import requests
import random

app = Flask(__name__)

PEXELS_API_KEY = "NG9pCjeQouHiLVTYiRsYT0s4phWVZgutyz5z4oM1SjjkbU4RFER9y5nc"  # Replace with your actual Pexels API key

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    if request.method == "POST":
        gender = request.form.get("gender")
        occasion = request.form.get("occasion")
        season = request.form.get("season")
        wear_type = request.form.get("wear_type")

        # Construct a query for more accurate image results
        query = f"{gender} {occasion} {season} {wear_type} fashion clothing"

        # Pexels API request
        response = requests.get(
            f"https://api.pexels.com/v1/search?query={query}&per_page=5",
            headers={"Authorization": "NG9pCjeQouHiLVTYiRsYT0s4phWVZgutyz5z4oM1SjjkbU4RFER9y5nc"}
        )
        data = response.json()

        if data["photos"]:
            # Randomly select an image from the search results
            image_url = random.choice(data["photos"])["src"]["medium"]
        else:
            image_url = "https://via.placeholder.com/512?text=No+Outfit+Found"

    return render_template("index.html", image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
