from selenium import webdriver
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import requests

def listing_dow(all_case_names, cookies):
    # Funkcja do pobierania ceny pojemnika z API Steam
    def fetch_container_price(appid, market_hash_name):
        url = "https://steamcommunity.com/market/pricehistory/"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
        }

        params = {
            "appid": appid,
            "market_hash_name": market_hash_name
        }

        with requests.Session() as session:
            session.headers.update(headers)
            session.cookies.update(cookies)
            response = session.get(url, params=params)

            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    price = data['prices']
                    return price
            elif response.status_code == 429:
                while response.status_code == 429:
                    print("błąd 429, czekam 5 min...")
                    for i in tqdm(range(5 * 60)):
                        time.sleep(1)
                    response = session.get(url, params=params)
                data = response.json()
                if data.get("success"):
                    price = data['prices']
                    return price
            else:
                print(f'błąd: {response.status_code}')
        return None

    # Lista nazw pojemników (należy zastąpić rzeczywistymi nazwami)
    containers = list(set(all_case_names))
    print(f"liczba przedmiotów: {len(containers)}")

    case_listing = []
    i = 0
    for container in containers:
        i += 1
        print(i)
        price = fetch_container_price(appid=730, market_hash_name=container)
        if price is not None:
            case_listing.append([container] + price)
            print(f"Cena produktu '{container}': {price[-1][0]} {price[-1][1]}")
        else:
            print(f"Nie udało się pobrać ceny dla '{container}'")
    return case_listing



def labels_dow(url, pages):
    # Inicjalizacja WebDriver
    driver = webdriver.Chrome()

    # Ustawienie ciasteczka języka na angielski
    driver.get("https://steamcommunity.com/market")
    driver.add_cookie({"name": "Steam_Language", "value": "english"})
    time.sleep(1)  # Krótkie opóźnienie, aby upewnić się, że ciasteczko zostało ustawione

    # skrzynki:
    # url = f"https://steamcommunity.com/market/search?category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730&l=english"
    # pages = 40
    # naklejki:
    # url = f"https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Tool_Sticker&category_730_Weapon%5B%5D=any&appid=730&l=english#p{page_number}_popular_desc"
    # karabin
    # url = f"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Rifle&category_730_Weapon%5B%5D=any&appid=730#p{page_number}_popular_desc"
    # snajperki
    # url = f"https://steamcommunity.com/market/search?q=&category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_SniperRifle&category_730_Weapon%5B%5D=any&appid=730#p{page_number}_popular_desc"
    # pistolety
    # url = f"https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_Tournament%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_Pistol&category_730_Weapon%5B%5D=any&appid=730#p{page_number}_popular_desc"


    # Funkcja do pobrania nazw skrzynek z danej strony
    def get_case_names(page_number, url):
        driver.get(url +f'#p{page_number}_popular_desc"')
        time.sleep(2)  # Czekamy na załadowanie strony
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        case_names = []
        for item in soup.find_all("span", class_="market_listing_item_name"):
            case_names.append(item.text.strip())

        return case_names

    # Pobieranie nazw skrzynek z wielu stron
    all_case_names = []

    for i in tqdm(range(1, pages +1)):
        case_names = get_case_names(i, url)
        while all(name in all_case_names[-20:] for name in case_names):
            print("błąd 429, czekam 5 min...")
            print(f"jak na razie pobrano: {len(all_case_names)}/{( i -1 ) *10}")
            for i in tqdm(range( 5 *60)):
                time.sleep(1)
            driver.refresh()
            case_names = get_case_names(i, url)
        all_case_names.extend(case_names)
    driver.quit()
    return all_case_names