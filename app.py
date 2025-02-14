from flask import Flask, render_template, request, jsonify
import json
import random

app = Flask(__name__)

# Load the predefined dataset
with open('dataset.json') as file:
    outfit_dataset = json.load(file)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_image = None
    if request.method == 'POST':
        gender = request.form.get('gender')
        occasion = request.form.get('occasion')
        season = request.form.get('season')
        wear_type = request.form.get('wear_type')

        # Filter the dataset based on user input
        filtered_outfits = [
            outfit for outfit in outfit_dataset
            if outfit['gender'] == gender and outfit['occasion'] == occasion and outfit['season'] == season and outfit['wear_type'] == wear_type
        ]

        # Randomly select an outfit if available
        if filtered_outfits:
            recommended_image = random.choice(filtered_outfits)['image_url']
        else:
            recommended_image = 'https://via.placeholder.com/512?text=No+Outfit+Found'

    return render_template('index.html', image_url=recommended_image)

if __name__ == '__main__':
    app.run(debug=True, port = '5001')
