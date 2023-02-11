import requests
import random

class Cat():
    embedColor = 0x3498DB
    subList = ['IllegallySmolCats', 'cats', 'Catloaf', 'Catswithjobs', 'WhatsWrongWithYourCat', 'blackcats', 'CatSlaps', 'SupermodelCats', 'CatsStandingUp', 'bigcatgifs', 'catbellies', 'catpictures', 'catpranks', 'catsareliquid', 'catsinsinks', 'catsinbusinessattire', 'catswhoyell', 'catswithjobs', 'cattaps', 'catsisuottafo', 'blep', 'fromkittentocat', 'holdmycatnip', 'jellybeantoes', 'kittens', 'kitting', 'kneadycats', 'mainecoons', 'murdermittens', 'nebelung', 'petthedamncat', 'pocketpussy', 'ragdolls', 'startledcats', 'stuffoncats', 'teefies', 'thecattrapisworking', 'tightpussy', 'toebeans', 'tuckedinkitties']
    keyList = []

    def getKey(self):
        return random.choice(Cat.keyList)
    
    def image(self, *breed):
        try:
            breed = str(breed[0])
        except IndexError:
            breed = None

        if breed:
            r = requests.get(f'https://api.thecatapi.com/v1/images/search?mime_types=jpg,png&breed_ids={breed}', headers={'x-api-key': Cat.getKey(self)})
            return r.json()[0]['url']
        else:
            r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=jpg,png', headers={'x-api-key': Cat.getKey(self)})
            return r.json()[0]['url']
    
    def gif(self):
        randomNum = random.randint(1, 2)
        
        if randomNum == 1:
            r = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif', headers={'x-api-key': Cat.getKey(self)})
            return r.json()[0]['url']
        else:
            r = requests.get('https://edgecats.net/all')
            gifLinks = [i.split('href="')[1].split('"')[0] for i in r.text.splitlines() if 'href="' in i]
            return random.choice(gifLinks)
    
    def get_breeds(self):
        r = requests.get('https://api.thecatapi.com/v1/breeds', headers={'x-api-key': Cat.getKey(self)})
        return r.json()
    
    def get_breed_info(self, breedid):
        r = requests.get(f'https://api.thecatapi.com/v1/breeds/{breedid}', headers={'x-api-key': Cat.getKey(self)})
        return r.json()