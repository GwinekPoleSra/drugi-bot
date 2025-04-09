import discord
from discord.ext import commands
import requests
import pickle
import os

intents = discord.Intents.default()
intents.message_content = True  # Dodaj to, jeśli chcesz obsługiwać wiadomości
bot = commands.Bot(command_prefix="!", intents=intents)

def load_cookies():
    with open("cookies.pkl", "rb") as f:
        return pickle.load(f)

def create_linkvertise_link(original_url):
    session = requests.Session()
    session.cookies.update(load_cookies())

    api_url = "https://publisher.linkvertise.com/api/v1/links"
    payload = {
        "title": "Kliknij tutaj!",
        "link": original_url,
        "domain": "link-center.net",
        "description": "Opis linku",
        "creator": "TwójNick",
        "advertising_type": "article"
    }

    response = session.post(api_url, json=payload)
    if response.status_code == 201:
        return response.json()["data"]["fullLink"]
    else:
        print(f"Błąd: {response.status_code} - {response.text}")
        return None

@bot.command()
async def link(ctx, *, url):
    await ctx.send("🔗 Tworzę link...")
    generated_link = create_linkvertise_link(url)
    if generated_link:
        await ctx.send(f"Oto Twój link Linkvertise:\n{generated_link}")
    else:
        await ctx.send("❌ Wystąpił problem przy tworzeniu linku.")

bot.run(os.getenv("DISCORD_TOKEN"))
