import requests
from dotenv import load_dotenv
import os
import json
from yelpapi import YelpAPI

load_dotenv()
YELP_KEY = os.getenv("YELP_KEY") 

# url = "https://api.yelp.com/v3/businesses/search?location=San%20Jose&sort_by=best_match&limit=5"

# headers = {"accept": "application/json",
#            "Authorization": YELP_KEY
#            }

# response = requests.get(url, headers=headers)

# json_string = response.text
# data = json.loads(json_string)

# businesses = data['businesses']

# for business in businesses:
#     print(f"Name: {business['name']}")
#     print(f"Rating: {business['rating']}")
#     print(f"Categories: {', '.join([category['title'] for category in business['categories']])}")
#     print(f"Address: {business['location']['display_address'][0]}")
#     print(f"URL: {business['url']}")

try:
    yelp_api = YelpAPI(YELP_KEY)
    search_results = yelp_api.search_query(location="San Jose", term='restaurant', limit=5)
    print(search_results)
finally:
    yelp_api.close()