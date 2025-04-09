from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pickle
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://publisher.linkvertise.com/login")

print("🔐 Zaloguj się ręcznie (60 sekund)...")
time.sleep(60)

with open("cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ Cookies zapisane do cookies.pkl")
driver.quit()