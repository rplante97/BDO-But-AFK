import requests
import random
import time
import pickle

# Grab up to date prices from API
def update_prices(filename):
    prices = {}

    print("Updating Grunil prices...")
    prices['pri_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_grunil'] = requests.get("https://omegapepega.com/na/Grunil%20Helmet/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Griffon prices...")
    prices['pri_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_griffon'] = requests.get("https://omegapepega.com/na/Griffon's%20Helmet/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Giath prices...")
    prices['pri_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_giath'] = requests.get("https://omegapepega.com/na/Giath's%20Helmet/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Red Nose prices...")
    prices['pri_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_rednose'] = requests.get("https://omegapepega.com/na/Red%20Nose's%20Armor/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Dim Tree prices...")
    prices['pri_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_dimtree'] = requests.get("https://omegapepega.com/na/Dim%20Tree%20Spirit's%20Armor/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Muskan prices...")
    prices['pri_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_muskan'] = requests.get("https://omegapepega.com/na/Muskan's%20Shoes/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Urugon prices...")
    prices['pri_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_urugon'] = requests.get("https://omegapepega.com/na/Urugon's%20Shoes/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Bheg prices...")
    prices['pri_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_bheg'] = requests.get("https://omegapepega.com/na/Bheg's%20Gloves/20", headers={'Connection': 'close'}).json()['pricePerOne']

    print("Updating Leebur prices...")
    prices['pri_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/16", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['duo_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/17", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tri_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/18", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['tet_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/19", headers={'Connection': 'close'}).json()['pricePerOne']
    prices['pen_leebur'] = requests.get("https://omegapepega.com/na/Leebur's%20Gloves/20", headers={'Connection': 'close'}).json()['pricePerOne']
    
    with open(filename, 'wb') as file_handler:
        pickle.dump(prices, file_handler)

    #print(prices)

prices_file = 'prices.pk'
# ONLY RUN TO UPDATE STALE PRICES
#update_prices(prices_file) #API is SLOW ~1 min to fetch all prices

with open(prices_file, 'rb') as file_handler:
    prices = pickle.load(file_handler)

#All numbers in MILLIONS
REBLATH_18 = 6.09
REBLATH_21 = 8.049
REBLATH_24 = 10.549

#BASE CHANCES
#base_chance, increase_per_fs, softcap_increase_per_fs, softcap_fs, added_fs, downgrade_name, upgrade_name
duo_base = 0.0769
duo_increase = 0.0077
