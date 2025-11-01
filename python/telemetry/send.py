# --- IMPORTS ---
import requests as rq
from bs4 import BeautifulSoup

# --- LINK TO GIST ---
GIST_LINK = "https://gist.githubusercontent.com/Silletr/8f539cb32c31232d1c1f5129d34b6292/raw/9b80d2bc0ab922624f9873f00bf1cd7fc0095a99/telemetry_data.txt"


# --- LOGGING MESSAGE ---
def log_message(message: str, level: str = "info") -> None:
    prefixes = {"info": "[INFO]", "success": "[OK]", "error": "[ERR]"}
    print(f"{prefixes.get(level, '📍')} {message}")


# --- CONNECTING ---
query = rq.get(GIST_LINK)
if query.status_code == 200:
    log_message("Connection is ok!", "success")


responce = query.text
soup = BeautifulSoup(responce, "html.parser")
print(soup)
