import requests
import random
import time
import pickle
import sys
import numpy as np

reblath_15 = 4.562
reblath_17 = 5.89
reblath_18 = 6.09
reblath_21 = 8.049 #mil
reblath_24 = 10.549 #mil

db = {}
db['pri_reblath'] = [0, 'duo_reblath', .0769, .0077, 2, 3, 'pri_reblath', 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
db['duo_reblath'] = [41.5, 'tri_reblath', .0625, .00625, 2, 4, 'pri_reblath', 102, .00125]
db['tri_reblath'] = [102, 'tet_reblath', .02, .002, 2, 5, 'duo_reblath', 340, 0]
db['tet_reblath'] = [455, 'pen_reblath', .003, .0003, 2, 6, 'tri_reblath', 2324, 0]
db['pen_reblath'] = [2840, 'NA', 0, 0, 0, 0, None]

db['pri_boss'] = [0, 'duo_boss', .0769, .0077, 2 + 10*1.5, 3, 'pri_boss', 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
db['duo_boss'] = [41.5, 'tri_boss', .0625, .00625, 2 + 10*1.5, 4, 'pri_boss', 102, .00125]
db['tri_boss'] = [102, 'tet_boss', .02, .002, 2 + 10*1.5, 5, 'duo_boss', 340, 0]
db['tet_boss'] = [455, 'pen_boss', .003, .0003, 2 + 10*1.5, 6, 'tri_boss', 2324, 0]
db['pen_boss'] = [17000, 'NA', 0, 0, 0, 0, None]

#db['pri_reblath'] = [7, 'duo_reblath', .0769, .0077, 2, 3, None, 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain
#db['duo_reblath'] = [11.56, 'tri_reblath', .0625, .00625, 2, 4, 'pri_reblath', 102, .00125]
#db['tri_reblath'] = [18.08, 'tet_reblath', .02, .002, 2, 5, 'duo_reblath', 340, 0]
#db['tet_reblath'] = [50.47, 'pen_reblath', .003, .0003, 2, 6, 'tri_reblath', 2324, 0]
#db['pen_reblath'] = [3500, 'NA', 0, 0, 0, 0, None]

db['pri_leebur'] = [520, 'duo_leebur', .077, .0077, 2+10*1.3, 3, None, 82, .00155] #cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth
db['pri_dimtree'] = [520, 'duo_dimtree', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_bheg'] = [520, 'duo_bheg', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_giath'] = [520, 'duo_giath', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_urugon'] = [520, 'duo_rednose', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_rednose'] = [520, 'duo_rednose', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_muskan'] = [520, 'duo_muskan', .077, .0077, 2+10*1.3, 3, None, 82, .00155]
db['pri_griffon'] = [520, 'duo_muskan', .077, .0077, 2+10*1.3, 3, None, 82, .00155]

db['duo_leebur'] = [615, 'tri_leebur', .0625, .00625, 2+10*1.3, 4, 'pri_leebur', 102, .00125]
db['duo_dimtree'] = [615, 'tri_dimtree', .0625, .00625, 2+10*1.3, 4, 'pri_dimtree', 102, .00125]
db['duo_bheg'] = [615, 'tri_bheg', .0625, .00625, 2+10*1.3, 4, 'pri_bheg', 102, .00125]
db['duo_giath'] = [615, 'tri_giath', .0625, .00625, 2+10*1.3, 4, 'pri_giath', 102, .00125]
db['duo_urugon'] = [615, 'tri_urugon', .0625, .00625, 2+10*1.3, 4, 'pri_urugon', 102, .00125]
db['duo_rednose'] = [615, 'tri_rednose', .0625, .00625, 2+10*1.3, 4, 'pri_rednose', 102, .00125]
db['duo_muskan'] = [615, 'tri_muskan', .0625, .00625, 2+10*1.3, 4, 'pri_muskan', 102, .00125]
db['duo_griffon'] = [615, 'tri_muskan', .0625, .00625, 2+10*1.3, 4, 'pri_muskan', 102, .00125]

db['tri_leebur'] = [720, 'tet_leebur', .02, .002, 2+10*1.3, 5, 'duo_leebur', 340, 0]
db['tri_dimtree'] = [720, 'tet_dimtree', .02, .002, 2+10*1.3, 5, 'duo_dimtree', 340, 0]
db['tri_bheg'] = [720, 'tet_bheg', .02, .002, 2+10*1.3, 5, 'duo_bheg', 340, 0]
db['tri_giath'] = [720, 'tet_giath', .02, .002, 2+10*1.3, 5, 'duo_giath', 340, 0]
db['tri_urugon'] = [720, 'tet_urugon', .02, .002, 2+10*1.3, 5, 'duo_urugon', 340, 0]
db['tri_rednose'] = [720, 'tet_rednose', .02, .002, 2+10*1.3, 5, 'duo_rednose', 340, 0]
db['tri_muskan'] = [720, 'tet_muskan', .02, .002, 2+10*1.3, 5, 'duo_muskan', 340, 0]
db['tri_griffon'] = [720, 'tet_muskan', .02, .002, 2+10*1.3, 5, 'duo_muskan', 340, 0]

db['tet_leebur'] = [1990, 'pen_leebur', .003, .0003, 2+10*1.3, 6, 'tri_leebur', 2324, 0]
db['tet_dimtree'] = [1990, 'pen_dimtree', .003, .0003, 2+10*1.3, 6, 'tri_dimtree', 2324, 0]
db['tet_bheg'] = [1990, 'pen_bheg', .003, .0003, 2+10*1.3, 6, 'tri_bheg', 2324, 0]
db['tet_giath'] = [1990, 'pen_giath', .003, .0003, 2+10*1.3, 6, 'tri_giath', 2324, 0]
db['tet_urugon'] = [1990, 'pen_urugon', .003, .0003, 2+10*1.3, 6, 'tri_urugon', 2324, 0]
db['tet_rednose'] = [1990, 'pen_rednose', .003, .0003, 2+10*1.3, 6, 'tri_rednose', 2324, 0]
db['tet_muskan'] = [1990, 'pen_muskan', .003, .0003, 2+10*1.3, 6, 'tri_muskan', 2324, 0]
db['tet_griffon'] = [1990, 'pen_muskan', .003, .0003, 2+10*1.3, 6, 'tri_muskan', 2324, 0]

db['pen_leebur'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_dimtree'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_bheg'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_giath'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_urugon'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_rednose'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_muskan'] = [17900, 'NA', 0, 0, 0, 0]
db['pen_griffon'] = [17900, 'NA', 0, 0, 0, 0]


pen_db = {}
#cost, name_of_success, base_chance, chance_growth, click_cost, stack_growth, down-grade name, stack softcap, post softcap gfain, pen price, cron(mil)
pen_db['tet_leebur'] = [1850, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 17700, -429*.8725]
pen_db['tet_urugon'] = [2390, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 17200, -493*.8725]
pen_db['tet_muskan'] = [1550, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 15700, -429*.8725]
pen_db['tet_dimtree'] = [2010, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 18400, -493*.8725]
pen_db['tet_rednose'] = [1630, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 17300, -429*.8725]
pen_db['tet_kzarka'] = [1430, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 16100, -531*.8725]
pen_db['tet_dande'] = [1670, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 15500, -611*.8725]
pen_db['tet_kutum'] = [1800, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 18600, -531*.8725]
pen_db['tet_nouver'] = [1590, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 14100, -531*.8725]
pen_db['tet_griffon'] = [1590, 'pen_boss', .003, .0003, 2+10*1.3*1.3, 6, 'tri_boss', 2324, 0, 14100, -429*.8725]
pen_db['tri_blackstar'] = [3000, 'pen_boss', .0051, .0005, 2+20*1.3, 5, 'duo_blackstar', 2324, 0, 15000, -591*.8725]


acc_db = {}
#price, 'success_name', 'down_grade_name', 'upgrade name', base chance, chance_growth, softcap, post-softcap growth, crons
acc_db['base_ogre'] = [0, 'pri_ogre', 'NA', 'base_ogre', .25, .025, 18, .0005, 0]
acc_db['pri_ogre'] = [0, 'duo_ogre', 'base_ogre', 'base_ogre', .1, .01, 40, .0002, -142]
acc_db['duo_ogre'] = [0, 'tri_ogre', 'pri_ogre', 'base_ogre', .075, .0075, 44, .00015, -427]
acc_db['tri_ogre'] = [0, 'tet_ogre', 'duo_ogre', 'base_ogre', .025, .0025, 110, .00005, -1187]
acc_db['tet_ogre'] = [0, 'pen_ogre', 'tri_ogre', 'base_ogre', .005, .0005, 2340, .00005, -5699]
acc_db['pen_ogre'] = [0, 'NA', 'NA', 'NA', 0, 0, 0, 0]

acc_db['base_distortion'] = [0, 'pri_distortion', 'NA', 'base_distortion', .25, .025, 18, .0005, 0]
acc_db['pri_distortion'] = [0, 'duo_distortion', 'base_distortion', 'base_distortion', .1, .01, 40, .0002, -187]
acc_db['duo_distortion'] = [0, 'tri_distortion', 'pri_distortion', 'base_distortion', .075, .0075, 44, .00015, -562]
acc_db['tri_distortion'] = [0, 'tet_distortion', 'duo_distortion', 'base_distortion', .025, .0025, 110, .00005, -1562]
acc_db['tet_distortion'] = [0, 'pen_distortion', 'tri_distortion', 'base_distortion', .005, .0005, 2340, .00005, -7499]
acc_db['pen_distortion'] = [0, 'NA', 'NA', 'NA', 0, 0, 0, 0]

acc_db['base_laytenn'] = [0, 'pri_laytenn', 'NA', 'base_laytenn', .25, .025, 18, .0005, 0]
acc_db['pri_laytenn'] = [0, 'duo_laytenn', 'base_laytenn', 'base_laytenn', .1, .01, 40, .0002, -142]
acc_db['duo_laytenn'] = [0, 'tri_laytenn', 'pri_laytenn', 'base_laytenn', .075, .0075, 44, .00015, -427]
acc_db['tri_laytenn'] = [0, 'tet_laytenn', 'duo_laytenn', 'base_laytenn', .025, .0025, 110, .00005, -1187]
acc_db['tet_laytenn'] = [0, 'pen_laytenn', 'tri_laytenn', 'base_laytenn', .005, .0005, 2340, .00005, -5699]
acc_db['pen_laytenn'] = [0, 'NA', 'NA', 'NA', 0, 0, 0, 0]

acc_db['base_tungrad_ring'] = [0, 'pri_tungrad_ring', 'NA', 'base_tungrad_ring', .25, .025, 18, .0005, 0]
acc_db['pri_tungrad_ring'] = [0, 'duo_tungrad_ring', 'base_tungrad_ring', 'base_tungrad_ring', .1, .01, 40, .0002, -187]
acc_db['duo_tungrad_ring'] = [0, 'tri_tungrad_ring', 'pri_tungrad_ring', 'base_tungrad_ring', .075, .0075, 44, .00015, -562]
acc_db['tri_tungrad_ring'] = [0, 'tet_tungrad_ring', 'duo_tungrad_ring', 'base_tungrad_ring', .025, .0025, 110, .00005, -1562]
acc_db['tet_tungrad_ring'] = [0, 'pen_tungrad_ring', 'tri_tungrad_ring', 'base_tungrad_ring', .005, .0005, 2340, .00005, -7499]
acc_db['pen_tungrad_ring'] = [0, 'NA', 'NA', 'NA', 0, 0, 0, 0]

acc_db['base_tungrad_belt'] = [0, 'pri_tungrad_belt', 'NA', 'base_tungrad_belt', .25, .025, 18, .0005, 0]
acc_db['pri_tungrad_belt'] = [0, 'duo_tungrad_belt', 'base_tungrad_belt', 'base_tungrad_belt', .1, .01, 40, .0002, -187]
acc_db['duo_tungrad_belt'] = [0, 'tri_tungrad_belt', 'pri_tungrad_belt', 'base_tungrad_belt', .075, .0075, 44, .00015, -562]
acc_db['tri_tungrad_belt'] = [0, 'tet_tungrad_belt', 'duo_tungrad_belt', 'base_tungrad_belt', .025, .0025, 110, .00005, -1562]
acc_db['tet_tungrad_belt'] = [0, 'pen_tungrad_belt', 'tri_tungrad_belt', 'base_tungrad_belt', .005, .0005, 2340, .00005, -7499]
acc_db['pen_tungrad_belt'] = [0, 'NA', 'NA', 'NA', 0, 0, 0, 0]

def update_db(database, prices):
	'''
	database = db variable above
	prices = prices dictionary from udpate_prices
	'''
	for i in database.keys():
		#print(i)
		if i in prices:
			database[i][0] = prices[i]/1000000

def update_pen_db(database, prices):
	for i in database.keys():
		if i in prices:
			database[i][0] = prices[i]/1000000
		if i[4:] != 'blackstar':
			pen = 'pen_'+i[4:]
			if pen in prices:
				database[i][9] = prices[pen]/1000000

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

	print("Updating ogre ring prices")
	prices['base_ogre'] = requests.get("https://omegapepega.com/na/11607/0", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pri_ogre'] = requests.get("https://omegapepega.com/na/11607/1", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_ogre'] = requests.get("https://omegapepega.com/na/11607/2", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_ogre'] = requests.get("https://omegapepega.com/na/11607/3", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_ogre'] = requests.get("https://omegapepega.com/na/11607/4", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_ogre'] = requests.get("https://omegapepega.com/na/11607/5", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Layten prices")
	prices['base_laytenn'] = requests.get("https://omegapepega.com/na/11630/0", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pri_laytenn'] = requests.get("https://omegapepega.com/na/11630/1", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_laytenn'] = requests.get("https://omegapepega.com/na/11630/2", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_laytenn'] = requests.get("https://omegapepega.com/na/11630/3", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_laytenn'] = requests.get("https://omegapepega.com/na/11630/4", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_laytenn'] = requests.get("https://omegapepega.com/na/11630/5", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating distortion prices")
	prices['base_distortion'] = requests.get("https://omegapepega.com/na/11853/0", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pri_distortion'] = requests.get("https://omegapepega.com/na/11853/1", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_distortion'] = requests.get("https://omegapepega.com/na/11853/2", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_distortion'] = requests.get("https://omegapepega.com/na/11853/3", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_distortion'] = requests.get("https://omegapepega.com/na/11853/4", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_distortion'] = requests.get("https://omegapepega.com/na/11853/5", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating Tungrad ring prices")
	prices['base_tungrad_ring'] = requests.get("https://omegapepega.com/na/12061/0", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pri_tungrad_ring'] = requests.get("https://omegapepega.com/na/12061/1", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_tungrad_ring'] = requests.get("https://omegapepega.com/na/12061/2", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_tungrad_ring'] = requests.get("https://omegapepega.com/na/12061/3", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_tungrad_ring'] = requests.get("https://omegapepega.com/na/12061/4", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_tungrad_ring'] = requests.get("https://omegapepega.com/na/12061/5", headers={'Connection': 'close'}).json()['pricePerOne']

	print("Updating tungrad_belt prices")
	prices['base_tungrad_belt'] = requests.get("https://omegapepega.com/na/12237/0", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pri_tungrad_belt'] = requests.get("https://omegapepega.com/na/12237/1", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['duo_tungrad_belt'] = requests.get("https://omegapepega.com/na/12237/2", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tri_tungrad_belt'] = requests.get("https://omegapepega.com/na/12237/3", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['tet_tungrad_belt'] = requests.get("https://omegapepega.com/na/12237/4", headers={'Connection': 'close'}).json()['pricePerOne']
	prices['pen_tungrad_belt'] = requests.get("https://omegapepega.com/na/12237/5", headers={'Connection': 'close'}).json()['pricePerOne']

	with open(filename, 'wb') as file_handler:
	    pickle.dump(prices, file_handler)

	#print(prices)

#prices_file = 'prices.pk'
# ONLY RUN TO UPDATE STALE PRICES
#update_prices(prices_file) #API is SLOW ~1 min to fetch all prices




def grunil_break_points(order):
	tax = 0.85
	conc_cost = 2
	fail_repair_cost = 0.34
	cur_stack = 18
	stack_cost = reblath_18
	cost_dict = {}
	current_index = 0
	just_incremented = True
	while(cur_stack < 200):
		best_index = 0
		best_cost = 0
		best_list = []
		i = current_index
		while(i < i + 1):
			#change it so it only attempts the current item and the item next to it
			if "grunil" not in order[i] or "pen_" in order[i]:
				i += 1
				continue
			current_list = db[order[i]]
			over_soft_cap = max(0,cur_stack - current_list[7])
			current_success_chance = over_soft_cap*current_list[8] + (cur_stack-over_soft_cap)*current_list[3] + current_list[2]
			if just_incremented == True:
				db[order[current_index+1]][0] = current_list[0] + stack_cost + (conc_cost+fail_repair_cost)/current_success_chance
			success_gain = -1 * (db[current_list[1]][0]*tax - current_list[0])
			current_success_cost = current_list[4] + stack_cost + success_gain
			#print("succ: cost", current_success_cost)
			current_fail_cost = current_list[4]

			if current_list[6] != None: #aka item can downgrade upon failure
				current_fail_cost += (current_list[0] - db[current_list[6]][0])
			#print("fail: cost", current_fail_cost)
			#cost_to_add = (stack_cost + current_fail_cost)/(1-current_success_chance) - (current_success_chance/(1-current_success_chance)*current_success_cost)
			current_cost = round(((current_success_chance*current_success_cost + (1 - current_success_chance)*current_fail_cost))/(1-current_success_chance)/current_list[5],2)
			if current_cost < 0:
				current_cost = 2
			#if order[current_index] == 'pri_grunil':
			#print("")
			print(" name: ", order[i], " cost: ", round(current_cost,2))
			print("item price: ", current_list[0])
			print("success price: ", db[current_list[1]][0])
			print("success_gain: ", success_gain * current_success_chance)
			print(" succ_chance: ", current_success_chance)
			print(" succ_cost: ", current_success_cost)
			print(" fail_cost: ", current_fail_cost)
			if current_index == 0:
				best_index = 0
				best_cost = current_cost
				best_list = current_list
				just_incremented = False
			else:
				if current_cost < best_cost:
					#print("swapping ", order[best_index], " for ", order[current_index])
					best_cost = current_cost
					best_index = i
					best_list = current_list
					current_index += 1
					break
					#best_cost_to_add = cost_to_add
			i += 1

		print(cur_stack, " costs: ", round(stack_cost,2), " || ", order[best_index], "= ", round(best_cost,2), "mil per stack ||")
		if cur_stack > 0:
			cost_dict[cur_stack] = stack_cost
		cur_stack += best_list[5]
		stack_cost += best_cost*best_list[5]
	return cost_dict

#cost_dict = grunil_break_points(order = ['pri_boss', 'duo_boss', 'tet_boss','pri_grunil', 'duo_grunil', 'tri_grunil', 'tet_grunil'])

def item_fs_cost(start_stack, start_cost, db, stop_points):
	tax = 0.85
	conc_cost = 2
	reblath_repair_cost = 0.012
	boss_repair_cost = 10*1.3
	repair_cost = 0
	cur_stack = start_stack
	stack_cost = start_cost
	#reblath_15 = 4.562
	#order = ['pri_reblath', 'pri_boss', 'duo_reblath', 'duo_boss', 'tri_reblath', 'tri_boss', 'tet_reblath', 'tet_boss', 'pen_reblath', 'pen_boss']
	order = ['pri_reblath', 'pri_boss']
	#PRI grunil || db['pri_grunil'] = [30.2, 'duo_grunil', .0769, .0077, 2, 3, None, 82, .00155]
	for i in range(len(stop_points)):
		if 'reblath' in order[i]:
			repair_cost = reblath_repair_cost
		elif 'boss' in order[i]:
			repair_cost = boss_repair_cost

		if "pen_" in order[i]:
			break
		if order[i] == 'valks':
			cur_stack += 10
			continue

		#computing the cost of the next item from enhancement
		success_name = db[order[i]][1]
		fail_name = db[order[i]][6]
		#print("aa", order[i])
		#print("**", db['duo_grunil'])
		stack_gain = db[order[i]][5]
		base_chance = db[order[i]][2]
		growth_chance = db[order[i]][3]
		stop_stack = stop_points[i][1]
		num_simulations = 1000
		#simulate making 1000 of the next enhance
		num_stacks_1 = 0
		num_item_1 = 0
		accumulated_cost_1 = 0
		while(num_item_1 < num_simulations):
			cur_sim_stack = cur_stack
			cur_stack_cost = stack_cost
			while(cur_sim_stack < stop_stack):
				chance = base_chance + cur_sim_stack*growth_chance
				roll = random.random()
				if (roll < 1 - chance): #failed enhancement
					cur_sim_stack += stack_gain
					accumulated_cost_1 += repair_cost + conc_cost
				else: #enhancement succeeded
					accumulated_cost_1 += cur_stack_cost
					num_item_1 += 1
			num_stacks_1 += 1
			#print(num_item)
		print("-----------------------------------------")
		print("repair cost: ", repair_cost)
		print("creating items simulation results: ")
		print("number of created items: ", num_item_1)
		print("number of created stacks: ", num_stacks_1)
		print("overall silver spent (mil) ", accumulated_cost_1)
		num_stacks_2 = 0
		num_item_2 = 0
		accumulated_cost_2 = 0
		while(num_stacks_2 < num_simulations):
			cur_sim_stack = cur_stack
			cur_stack_cost = stack_cost
			while(cur_sim_stack < stop_stack):
				chance = base_chance + cur_sim_stack*growth_chance
				roll = random.random()
				if (roll < 1 - chance):
					cur_sim_stack += stack_gain
					accumulated_cost_2 += repair_cost + conc_cost
				else:
					accumulated_cost_2 += cur_stack_cost
					num_item_2 += 1
			num_stacks_2 += 1
			#print(num_item)
		print("")
		print("creating stacks simulation results: ")
		print("number of created items: ", num_item_2)
		print("number of created stacks: ", num_stacks_2)
		print("overall silver spent (mil) ", accumulated_cost_2)
		A = np.asarray([[num_item_1, num_stacks_1], [num_item_2, num_stacks_2]])
		b = np.asarray([accumulated_cost_1, accumulated_cost_2])
		print("")
		print("Solving system of EQ results: ")
		print("A: ", A)
		print("b: ", b)

		x = np.linalg.solve(A, b)
		print("Cost of ", success_name, " is ", x[0])
		print("Cost of ", stop_stack, " stack is ", x[1])


	#testing
	for i in order:
		if i != 'valks':
			print(i, db[i])
pri_reblath = (15, 27)
pri_boss = (pri_reblath[1], 32)
duo_reblath = (pri_boss[1], 44)
duo_boss = (duo_reblath[1], 48)
tri_reblath = (duo_boss[1], 78)
valks = (tri_reblath[1], tri_reblath[1]+10)
tri_boss = (tri_reblath[1]+10, 98)
tet_reblath = (tri_boss[1], 116)
item_fs_cost(15, reblath_15, db, [pri_reblath, pri_boss, duo_reblath, duo_boss, tri_reblath, valks, tri_boss, tet_reblath])
exit(1)

def cron_pen(cost_dict, pen_details):
	#db['tet_boss'] = [1990, 'pen_boss', .003, .0003, 2+10*1.3, 6, 'tri_boss', 2324, 0]
	best_stack = 0
	best_profit = 0
	best_clicks = 0
	best_cost = 0
	first = True
	for i in cost_dict.keys():
		cur_odds = i*pen_details[3] + pen_details[2]
		#print(i)
		cost = pen_details[10] - 2 - 13
		reward = pen_details[-2]

		expected_cost = cost / cur_odds

		additional_expenses = -cost_dict[i] - pen_details[0]*.85

		overall_cost = expected_cost + additional_expenses

		#print("cost: ", overall_cost)

		profit = reward * .85  + overall_cost

		#print("profit: ", profit)

		if first == True:
			best_stack = i
			best_profit = profit
			best_clicks = 1/cur_odds
			best_cost = -1*overall_cost
			first = False
		else:
			if best_profit < profit:
				#print(best_profit, profit)
				best_profit = profit
				best_stack = i
				best_clicks = 1/cur_odds
				best_cost = -1*overall_cost
	return best_profit, best_cost, best_clicks, best_stack



def rank_pens(pen_db, cost_dict):
	over_all_list = []
	for i in pen_db.keys():
		profit, cost, clicks, stack = cron_pen(cost_dict, pen_db[i])
		cur_list = [i, profit, cost, clicks, stack]
		over_all_list.append(cur_list)
	over_all_list.sort(key = lambda x: x[1])
	over_all_list.reverse()

	for i in over_all_list:
		print(i)

#price, 'success_name', 'down_grade_name', 'upgrade name', base chance, chance_growth, softcap, post-softcap growth, crons
def acc(cost_dict, details, acc_dict,cron=False):
	tax = 0.85
	best_stack = 0
	best_profit = 0
	best_clicks = 0
	best_cost = 0
	first = True
	#print(cost_dict)
	for i in cost_dict.keys():
		#print(details)
		cur_stack = i
		#cur_odds = i*details[5] + details[4]
		over_soft_cap = max(0,cur_stack - details[6])
		cur_odds = over_soft_cap*details[7] + (cur_stack-over_soft_cap)*details[5] + details[4]
		#print("--------------------")
		#print("cur_stack: ", i)
		#print("over soft cap: ", over_soft_cap)
		#print("growth: ", details[5])
		#print("base: ", details[4])
		#print("cur_odds: ", cur_odds)
		#print(i)
		cost = acc_dict[details[3]][0]+details[0] #cost of base + cost of current acc * tax
		#print("cost: ", cost)
		if cron == True:
			cost += -0.7*(acc_dict[details[3]][0] + details[0]) + 0.3*(acc_dict[details[2]][0])

		reward = -acc_dict[details[1]][0] #cost of reward * tax


		expected_cost = cost 

		overall_cost = expected_cost

		#print("cost: ", overall_cost)

		profit = -1*(cur_odds*(reward * tax)  + (overall_cost + cost_dict[i]))

		#print("--------------------")
		#print("cur_stack: ", i)
		#print("over soft cap: ", over_soft_cap)
		#print("growth: ", details[5])
		#print("base: ", details[4])
		#print("cur_odds: ", cur_odds)
		#print(i)
		#print("cost: ", cost)
		#print("reward: ", reward)
		#print("profit: ", profit)

		if first == True:
			best_stack = i
			best_profit = profit
			best_clicks = 1/cur_odds
			best_cost = -1*overall_cost
			first = False
		else:
			if best_profit < profit:
				#print(best_profit, profit)
				best_profit = profit
				best_stack = i
				best_clicks = 1/cur_odds
				best_cost = -1*overall_cost
	return best_profit, best_cost, best_clicks, best_stack

def rank_acc(cost_dict,acc_dict,cron=False):
	over_all_list = []
	#print(acc_dict)
	for i in acc_dict.keys():
		#print(acc_dict[i])
		#exit(1)
		if "pen" in i or "base" in i:
			continue
		profit, cost, clicks, stack = acc(cost_dict, acc_dict[i], acc_dict,cron)
		cur_list = [i, profit, cost, clicks, stack]
		over_all_list.append(cur_list)
	over_all_list.sort(key = lambda x: x[1])
	over_all_list.reverse()

	for i in over_all_list:
		print(i)

def main():
	command = sys.argv[1]
	prices = {}
	if command == "update_prices":
		update_prices('prices.pk')
		exit(1)
	prices_file = 'prices.pk'
	with open(prices_file, 'rb') as file_handler:
		prices = pickle.load(file_handler)
	#print(pen_db)
	if command == "rank_pens":
		#print(list(db.keys()))
		update_db(db,prices)
		update_pen_db(pen_db, prices)
		cost_dict = grunil_break_points(order = list(db.keys()))
		rank_pens(pen_db,cost_dict)
	if command == "rank_acc":
		update_db(db,prices)
		update_db(acc_db, prices)
		cost_dict = grunil_break_points(order = list(db.keys()))
		rank_acc(cost_dict, acc_db)
main()