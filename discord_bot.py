import discord
from discord.ext import commands
from dotenv import load_dotenv
import os 
import requests
from yelpapi import YelpAPI


load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN") 
YELP_KEY = os.getenv("YELP_KEY")


intents = discord.Intents.default()
intents.message_content = True

# client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command()
async def restaurant(ctx, city):
    try:
        yelp_api = YelpAPI(YELP_KEY)
        response = yelp_api.search_query(location=city, term='restaurant', limit=5)
       
        for business in response['businesses']:
            await ctx.send(f"Name: {business['name']}\nRating: {business['rating']}\nAddress: {', '.join(business['location']['display_address'])}\n")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"Error: {e}")

    

bot.run(BOT_TOKEN)
