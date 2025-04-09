import discord
from discord.ext import commands
import requests
import pickle
import os
from dotenv import load_dotenv
from flask import Flask, request

# Załaduj zmienne środowiskowe z .env
load_dotenv()

# Tworzymy aplikację Flask do nasłuchiwania na odpowiednim porcie
app = Flask(__name__)

# Tworzymy bota Discorda
intents = discord.Intents.default()
intents.message_content = True  # Włączenie uprawnień do treści wiadomości
bot = commands.Bot(command_prefix="!", intents=intents)

# Ładowanie cookies
def load_cookies():
    cookies_file = "cookies.pkl"

    # Sprawdź, czy plik cookies.pkl istnieje
    if not os.path.exists(cookies_file):
        print(f"❌ Plik {cookies_file} nie istnieje!")
        return {}

    try:
        # Otwórz i załaduj dane z cookies.pkl
        with open(cookies_file, "rb") as f:
            cookies = pickle.load(f)

        # Jeżeli cookies to lista obiektów, zamień ją na słownik
        if isinstance(cookies, list):
            cookies = {cookie["name"]: cookie["value"] for cookie in cookies}

        return cookies

    except Exception as e:
        print(f"❌ Błąd podczas ładowania ciasteczek: {e}")
        return {}

# Tworzenie linku
def create_linkvertise_link(original_url):
    session = requests.Session()
    cookies = load_cookies()  # Użycie funkcji load_cookies() tutaj
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
        await ctx.send(f"Oto Twój link Linkvertise:\n{generated_link}")
    else:
        await ctx.send("❌ Wystąpił problem przy tworzeniu linku.")

# Start bota
TOKEN = os.getenv("DISCORD_TOKEN") or "WSTAW_TU_TOKEN"
bot.run(TOKEN)

# Nasłuchuj na porcie dla aplikacji Flask (Render wymaga tego)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))
