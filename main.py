import discord
from discord.ext import commands
import requests
import pickle
import os
from dotenv import load_dotenv
from flask import Flask

# Załaduj zmienne środowiskowe z .env
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # Włączenie uprawnień do treści wiadomości
bot = commands.Bot(command_prefix="!", intents=intents)

# Inicjalizacja aplikacji Flask
app = Flask(__name__)

# Ładowanie cookies
def load_cookies():
    if not os.path.exists("cookies.pkl"):
        print("❌ Plik cookies.pkl nie istnieje.")
        return {}
    
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        return {cookie["name"]: cookie["value"] for cookie in cookies}

# Tworzenie linku
def create_linkvertise_link(original_url):
    session = requests.Session()
    cookies = load_cookies()
    
    if not cookies:
        print("❌ Brak ciasteczek do załadowania.")
        return None
    
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

# Strona do uruchomienia w Flasku (jeśli potrzebujesz)
@app.route('/')
def home():
    return "Aplikacja działa!"

# Start bota i aplikacji webowej
if __name__ == "__main__":
    # Pobierz port z zmiennej środowiskowej lub ustaw domyślnie na 5000
    port = int(os.getenv("PORT", 5000))  # Port z zmiennej środowiskowej lub 5000
    # Uruchom Flask w tle
    from threading import Thread
    def run_flask():
        app.run(host='0.0.0.0', port=port)

    thread = Thread(target=run_flask)
    thread.start()
    
    # Uruchom bota
    TOKEN = os.getenv("DISCORD_TOKEN") or "WSTAW_TU_TOKEN"
    bot.run(TOKEN)
