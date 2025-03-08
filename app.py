from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import requests
import os
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
MAPMYINDIA_API_KEY = os.getenv("MAPMYINDIA_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

def get_ai_response(query):
    model = genai.GenerativeModel("gemini-2.0-pro-exp")
    response = model.generate_content(f"Answer in pure Lucknowi Nawabi style without any English translation but in hinglish: {query}")
    return response.text.replace("*", "").strip()  # Remove * symbols


def search_tavily(query):
    url = "https://api.tavily.com/search"
    params = {"query": query, "api_key": TAVILY_API_KEY}
    response = requests.get(url, params=params)
    return response.json().get("results", [])

def get_places(query):
    url = "https://atlas.mapmyindia.com/api/places/search/json"
    headers = {"Authorization": f"Bearer {MAPMYINDIA_API_KEY}"}
    params = {"query": query}
    response = requests.get(url, headers=headers, params=params)
    return response.json().get("suggestedLocations", [])

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index copy.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    ai_response = get_ai_response(user_input)
    search_results = search_tavily(user_input)
    places = get_places(user_input)
    return jsonify({"response": ai_response, "search": search_results, "places": places})

if __name__ == '__main__':
    app.run(debug=True)
