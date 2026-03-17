from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_URL = "https://api-football.com/standings"
API_KEY = "your_api_key_here"  # Replace with your actual API key

@app.route('/standings', methods=['GET'])
def get_standings():
    league = request.args.get('league')
    season = request.args.get('season')
    
    if not league or not season:
        return jsonify({"error": "League and season are required"}), 400
    
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': API_KEY
    }
    
    response = requests.get(f"{API_URL}?league={{league}}&season={{season}}", headers=headers)
    
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Could not fetch standings"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)