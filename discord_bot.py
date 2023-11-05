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


@bot.event
async def on_greeting(message):
    if message.content.startswith("$hello"):
        await message.channel.send("Hello ", message.author)

# Restaurants
@bot.command()
async def res(ctx, *, city):
    try:
        yelp_api = YelpAPI(YELP_KEY)
        response = yelp_api.search_query(location=city, term='restaurant', limit=5)
        for restaurant in response['businesses']:
            await ctx.send(f"{restaurant['name']}\nRating: {restaurant['rating']}\nAddress: {', '.join(restaurant['location']['display_address'])}\nURL: {restaurant['url']}\n-------------------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"Error: {e}")

@bot.command()
async def food(ctx, *, cuisine):
    try:
        yelp_api = YelpAPI(YELP_KEY)
        response = yelp_api.search_query(location="San Jose, CA", term=cuisine, limit=5)
        for restaurant in response['businesses']:
            await ctx.send(f"{restaurant['name']}\nRating: {restaurant['rating']}\nAddress: {', '.join(restaurant['location']['display_address'])}\nURL: {restaurant['url']}\n-------------------------------------")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"Error: {e}") 



bot.run(BOT_TOKEN)





# Command to run
#py -3 .\discord_bot.py
