import requests
import pickle

armor_dict = {
    "giath": 11013,
    "grunil": 10933,
    "griffon": 11101,
    "rednose": 11014,
    "dimtree": 11017,
    "muskan": 11016,
    "urugon": 11103,
    "bheg": 11015,
    "leeburs": 11102,
    "bsarmor": 719902,
    "bshelmet": 719901,
    "bsshoes": 719904,
    "bsgloves": 719903,
}

accessories_dict = {
    "layten": 11630,
    "distortion": 11853,
    "tungradring": 12061,
    "tungradbelt": 12237,
    "ogre": 11607,
    "ruins": 12060,
    "crescent": 12031,
    "valtarra": 12236,
    "turos": 12257,
    "tungradnecklace": 11629,
    "ominous": 12068
}

# Grab up to date prices from API
def update_prices(filename):
    prices = {}
    armor_weapon_enhancement_levels = {"16", "17", "18", "19", "20"}
    acc_enhancement_levels = {"0", "1", "2", "3", "4", "5"}

    print("Updating Grunil prices...")
    grunil_prices = get_prices_for_levels(10933, armor_weapon_enhancement_levels)
    prices['pri_grunil'] = grunil_prices["16"]
    prices['duo_grunil'] = grunil_prices["17"]
    prices['tri_grunil'] = grunil_prices["18"]
    prices['tet_grunil'] = grunil_prices["19"]
    prices['pen_grunil'] = grunil_prices["20"]
    
    with open(filename, 'wb') as file_handler:
        pickle.dump(prices, file_handler)


def get_prices_for_levels(itemid, levels):
    json_response = requests.get(f"http://bdomarketapi.com/market/NA/items?id={itemid}", headers={'Connection': 'close'}).json()

    level_price_dict = {}
    for item in json_response:
        if item["level"] in levels:
            level_price_dict[item["level"]] = item["price"]

    return level_price_dict

prices_file = 'prices.pk'
# ONLY RUN TO UPDATE STALE PRICES
update_prices(prices_file) #API is SLOW ~1 min to fetch all prices

with open(prices_file, 'rb') as file_handler:
    prices = pickle.load(file_handler)

FREE_FAILSTACK = 1
BLACK_STONE_PRICE = 120000
#All numbers in MILLIONS
REBLATH_18 = BLACK_STONE_PRICE * (18-FREE_FAILSTACK)
REBLATH_21 = BLACK_STONE_PRICE * (21-FREE_FAILSTACK)
REBLATH_24 = BLACK_STONE_PRICE * (24-FREE_FAILSTACK)

#BASE CHANCES
#base_chance, increase_per_fs, softcap_increase_per_fs, softcap_fs, added_fs, downgrade_name, upgrade_name
duo_base = 0.0769
duo_increase = 0.0077