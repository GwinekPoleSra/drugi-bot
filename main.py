import discord
from discord.ext import commands
import requests
import pickle
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Ładowanie cookies
def load_cookies():
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        return {cookie["name"]: cookie["value"] for cookie in cookies}

# Tworzenie linku
def create_linkvertise_link(original_url):
    session = requests.Session()
    cookies = load_cookies()
    session.cookies.update(cookies)

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json",
        "Origin": "https://publisher.linkvertise.com",
        "Referer": "https://publisher.linkvertise.com/links"
    }

    api_url = "https://publisher.linkvertise.com/api/v1/links"
    payload = {
        "title": "Kliknij tutaj!",
        "link": original_url,
        "domain": "link-center.net",
        "description": "Opis linku",
        "creator": "BotLink",
        "advertising_type": "article"
    }

    response = session.post(api_url, json=payload, headers=headers)
    if response.status_code == 201:
        data = response.json()
        return data["data"]["fullLink"]
    else:
        print(f"❌ Błąd {response.status_code} - {response.text}")
        return None

# Komenda !link
@bot.command()
async def link(ctx, *, url):
    await ctx.send("🔗 Tworzę link...")

    generated_link = create_linkvertise_link(url)

    if generated_link:
        await ctx.send(f"Oto Twój link Linkvertise:
{generated_link}")
    else:
        await ctx.send("❌ Wystąpił problem przy tworzeniu linku.")

# Start bota
TOKEN = os.getenv("DISCORD_TOKEN") or "WSTAW_TU_TOKEN"
bot.run(TOKEN)