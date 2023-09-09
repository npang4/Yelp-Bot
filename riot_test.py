import requests
from dotenv import load_dotenv
import os 

load_dotenv()

RIOT_KEY = os.getenv("RIOT_KEY") 
get_summoner_link = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/dis bao'
headers = {
    'X-Riot-Token': RIOT_KEY,
}

response = requests.get(get_summoner_link, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("data: ", data)
else:
    print(f"Error: {response.status_code} - {response.text}")