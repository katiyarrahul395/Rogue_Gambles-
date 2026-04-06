from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "YOUR_ACTUAL_KEY_HERE"
API_URL = "https://api.roulobets.com/v1/external/affiliates"

@app.route('/')
def index():
    # Parameters for the API (adjust dates as needed)
    params = {
        "start_at": "2025-11-01",
        "end_at": "2025-11-30",
        "key": API_KEY
    }
    
    try:
        response = requests.get(API_URL, params=params)
        data = response.json()
        
        # Assuming the API returns a list of players/affiliates
        # Sort by wager amount descending and take the top 10
        raw_list = data.get('data', []) 
        sorted_players = sorted(raw_list, key=lambda x: x.get('wager', 0), reverse=True)
        top_10 = sorted_players[:10]
        
    except Exception as e:
        top_10 = []
        print(f"Error fetching data: {e}")

    return render_template('index.html', players=top_10)

if __name__ == '__main__':
    app.run(debug=True)