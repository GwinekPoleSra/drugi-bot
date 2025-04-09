import discord
from discord.ext import commands
import requests
import pickle

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Załaduj cookies jako słownik
def load_cookies():
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
        try:
            return {cookie.name: cookie.value for cookie in cookies}  # obiekty cookies
        except Exception as e:
            print("❗ Błąd parsowania cookies:", e)
            return cookies  # może już jest dict

# Tworzenie linku
def create_linkvertise_link(original_url):
    session = requests.Session()
    cookies = load_cookies()
    session.cookies.update(cookies)

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
        data = response.json()
        return data["data"]["fullLink"]
    else:
        print(f"❌ Błąd: {response.status_code} - {response.text}")
        return None

# Komenda bota
@bot.command()
async def link(ctx, *, url):
    await ctx.send("🔗 Tworzę link...")

    generated_link = create_linkvertise_link(url)

    if generated_link:
        await ctx.send(f"Oto Twój link Linkvertise:\n{generated_link}")
    else:
        await ctx.send("❌ Wystąpił problem przy tworzeniu linku.")

bot.run(os.getenv("DISCORD_TOKEN"))
