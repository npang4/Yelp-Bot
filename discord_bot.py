import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
from yelpapi import YelpAPI
import random

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") 
YELP_KEY = os.getenv("YELP_KEY")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Restaurants
@bot.command()
async def res(ctx, *, city):
    try:
        yelp_api = YelpAPI(YELP_KEY)
        response = yelp_api.search_query(location=city, term='restaurant',  sort_by='rating', limit=5)
       
        for business in response['businesses']:
            await ctx.send(f"{business['name']}\nRating: {business['rating']}\nAddress: {', '.join(business['location']['display_address'])}\n-------------------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"Error: {e}")

    

bot.run(BOT_TOKEN)
