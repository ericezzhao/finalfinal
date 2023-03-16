from flask import Flask, render_template, request
import config
import requests

app = Flask(__name__)
# Hides api keys via config.py
api_key = config.googlemapsAPI
yelp_key = config.yelpfusionAPI

@app.route("/")
def index():
    return render_template("index.html", api_key=config.googlemapsAPI, yelp_key=config.yelpfusionAPI)

@app.route("/search")
def search():
    query = request.args.get("query")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {"key": api_key, "query": query}
    response = requests.get(url, params=params)
    data = response.json()

    yelp_url = "https://api.yelp.com/v3/businesses/search"
    yelp_params = {"term": query, "location": "Seattle", "limit": 10}
    yelp_headers = {"Authorization": f"Bearer {yelp_key}"}
    yelp_response = requests.get(yelp_url, params=yelp_params, headers=yelp_headers)
    yelp_data = yelp_response.json()



    # Extracts location information for each restaurant result via google maps places
    locations = []
    for result in data["results"]:
        name = result["name"]
        lat = result["geometry"]["location"]["lat"]
        lng = result["geometry"]["location"]["lng"]
        locations.append({"name": name, "lat": lat, "lng": lng})

    # Extracts location information for each restaurant result via yelp fusion
    yelp_locations = []
    for result in yelp_data["businesses"]:
        name = result["name"]
        lat = result["coordinates"]["latitude"]
        lng = result["coordinates"]["longitude"]
        yelp_locations.append({"name": name, "lat": lat, "lng": lng})
    
    merged = locations + yelp_locations

    return {"locations": merged}

if __name__ == "__main__":
    app.run(debug=True)
